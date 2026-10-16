"""Render supplied copy/fonts as a separate small-type layer and composed PREVIEW.

python render_text_layers.py --request render-request.json --out-dir task/version
Pillow required; TrueType/OpenType cmap checks use the Python standard library. Outputs are working previews, never approved exports.
"""
import argparse
import hashlib
import json
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typography_policy import (DEFAULT_PROFILE, default_font_sizes, geometry_checks,
                               load_profile, role_name, valid_box)


def glyph_coverage(font_path, text):
    """Check actual SFNT cmap formats 4/12 (TrueType, OpenType, first TTC face)."""
    data = Path(font_path).read_bytes()
    def u16(offset): return struct.unpack_from('>H', data, offset)[0]
    def u32(offset): return struct.unpack_from('>I', data, offset)[0]
    try:
        face = u32(12) if data[:4] == b'ttcf' else 0
        cmap = None
        for table in range(u16(face+4)):
            record = face+12+16*table
            if data[record:record+4] == b'cmap':
                cmap = u32(record+8)
                break
        if cmap is None:
            raise ValueError('Supplied font has no cmap table')
        points = {ord(char) for char in text if not char.isspace()}
        covered, supported = set(), False
        for record in range(u16(cmap+2)):
            entry = cmap+4+8*record
            platform, encoding = u16(entry), u16(entry+2)
            if not (platform == 0 or (platform == 3 and encoding in (1, 10))):
                continue
            sub = cmap+u32(entry+4)
            fmt = u16(sub)
            if fmt == 12:
                supported = True
                for group in range(u32(sub+12)):
                    base = sub+16+12*group
                    first, last, glyph = u32(base), u32(base+4), u32(base+8)
                    covered.update(cp for cp in points if first <= cp <= last and glyph+cp-first != 0)
            elif fmt == 4:
                supported = True
                count = u16(sub+6)//2
                ends = sub+14
                starts = ends+2*count+2
                deltas = starts+2*count
                ranges = deltas+2*count
                limit = sub+u16(sub+2)
                for segment in range(count):
                    first, last = u16(starts+2*segment), u16(ends+2*segment)
                    delta = u16(deltas+2*segment)
                    offset = u16(ranges+2*segment)
                    for cp in points:
                        if not first <= cp <= last or cp > 0xFFFF:
                            continue
                        if offset == 0:
                            glyph = (cp+delta)&0xFFFF
                        else:
                            location = ranges+2*segment+offset+2*(cp-first)
                            glyph = u16(location) if location+2 <= limit else 0
                            if glyph: glyph = (glyph+delta)&0xFFFF
                        if glyph: covered.add(cp)
        if not supported:
            raise ValueError('No supported Unicode cmap format 4/12; use an equivalent verified renderer')
        missing = sorted(points-covered)
        if missing:
            raise ValueError('Missing supplied-font glyphs: ' + ''.join(chr(cp) for cp in missing))
    except (struct.error, IndexError) as error:
        raise ValueError('Invalid supplied font cmap') from error


def wrap(text, font, width):
    lines, widths = [], {}
    def measured_width(value):
        if value not in widths:
            box = font.getbbox(value)
            widths[value] = box[2] - box[0]
        return widths[value]
    for paragraph in text.split('\n'):
        line = ''
        for char in paragraph:
            candidate = line + char
            if measured_width(candidate) > width and line:
                lines.append(line)
                line = char
            else:
                line = candidate
        lines.append(line)
    return '\n'.join(lines)


def glyph_plan(text, font, size, leading, width, direction):
    draw = ImageDraw.Draw(Image.new('L', (1, 1)))
    if direction == 'horizontal':
        wrapped = wrap(text, font, width)
        spacing = max(0, math.ceil(size * (leading-1)))
        bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=spacing)
        return bbox, [(wrapped, -bbox[0], -bbox[1])], spacing
    columns = text.split('\n')
    cell = math.ceil(size * leading)
    commands, bounds = [], []
    for col, content in enumerate(columns):
        for row, char in enumerate(content):
            x, y = (len(columns)-1-col)*cell, row*cell
            box = draw.textbbox((x, y), char, font=font)
            commands.append((char, x, y))
            if not char.isspace():
                bounds.append(box)
    if not bounds:
        raise ValueError('No visible text glyphs')
    bbox = (min(b[0] for b in bounds), min(b[1] for b in bounds),
            max(b[2] for b in bounds), max(b[3] for b in bounds))
    return bbox, [(t, x-bbox[0], y-bbox[1]) for t, x, y in commands], 0


def render(request, out_dir):
    background_path = Path(request['background']).resolve(strict=True)
    out_dir = Path(out_dir).resolve()
    destinations = [out_dir/name for name in ('text-layer.png', 'composed-preview.png', 'typography-geometry.json')]
    if any(p.exists() for p in destinations) or background_path in destinations:
        raise ValueError('Use a new version directory; do not overwrite input or existing outputs')
    fonts = {Path(p).resolve(strict=True) for p in request.get('supplied_fonts', [])}
    if not fonts:
        raise ValueError('Explicit supplied_fonts required; no system-font fallback')
    with Image.open(background_path) as image:
        background = image.convert('RGBA')
    w, h = background.size
    short = min(w, h)
    profile = request.get('typography_profile') or DEFAULT_PROFILE
    p = load_profile(profile)
    is_small = p['id'] != DEFAULT_PROFILE
    min_size = request.get('min_font_px', p['default_min_font_px'])
    if type(min_size) is not int or min_size < p['default_min_font_px']:
        raise ValueError('min_font_px must be >= default 12px floor')
    subjects = request.get('subject_boxes')
    if not isinstance(subjects, list) or not subjects or any(not valid_box(b, w, h) for b in subjects):
        raise ValueError('Supply actual protected core-subject pixel boxes')
    items = request.get('items')
    if not isinstance(items, list) or not items:
        raise ValueError('Complete copy items required')
    ids = [i.get('id') for i in items]
    if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        raise ValueError('Unique copy IDs required')
    # Titles first so reduced title sizes also reduce subtitle/body caps.
    ordered = sorted(items, key=lambda i: role_name(i.get('role')) != 'title')
    nominal = default_font_sizes(w, h, profile)
    title_sizes, layers, metrics = [], [], []
    for item in ordered:
        text = item.get('text')
        if not isinstance(text, str) or not text.strip():
            raise ValueError('Exact nonempty text required: ' + item['id'])
        font_path = Path(item['font']).resolve(strict=True)
        if font_path not in fonts:
            raise ValueError('Font not in supplied_fonts: ' + item['id'])
        glyph_coverage(font_path, text)
        role = role_name(item.get('role'))
        region = item.get('region')
        if not valid_box(region, w, h):
            raise ValueError('region must be an in-canvas pixel box: ' + item['id'])
        padding = math.ceil(short*p['text_padding_short_side_ratio'])
        left = math.ceil(max(region[0]+padding, w*p['safe_margin_x_ratio']))
        top = math.ceil(max(region[1]+padding, h*p['safe_margin_y_ratio']))
        right = math.floor(min(region[2]-padding, w*(1-p['safe_margin_x_ratio'])))
        bottom = math.floor(min(region[3]-padding, h*(1-p['safe_margin_y_ratio'])))
        if left >= right or top >= bottom:
            raise ValueError('Region has no usable padded space: ' + item['id'])
        direction = item.get('direction', 'horizontal')
        if direction not in ('horizontal', 'vertical'):
            raise ValueError('Invalid writing direction')
        reference = min(title_sizes, default=nominal['title'])
        if is_small:
            default = nominal['title'] if role == 'title' else reference*p[role+'_title_ratio']
            cap = short*p['title_font_short_side_ratio_max'] if role == 'title' else reference*p[role+'_title_ratio_max']
        else:
            default = nominal[role]
            cap = None
        requested = item.get('font_size_px', max(min_size, math.floor(default)))
        if type(requested) is not int or requested < min_size or (cap is not None and requested > cap+1e-6):
            raise ValueError('Requested/default size exceeds role cap or readability floor: ' + item['id'])
        leading = item.get('leading', p['leading'][role])
        if not isinstance(leading, (int, float)) or not math.isfinite(leading) or leading < p['leading'][role]:
            raise ValueError('Leading below profile or invalid')
        limit_w, limit_h = right-left, bottom-top
        if is_small and role == 'title':
            if direction == 'horizontal':
                limit_h = min(limit_h, h*p['title_block_target_ratio'])
            else:
                limit_w = min(limit_w, w*p['title_block_target_ratio'])
        fitted = None
        for size in range(requested, min_size-1, -1):
            font = ImageFont.truetype(str(font_path), size=size)
            bbox, commands, spacing = glyph_plan(text, font, size, leading, limit_w, direction)
            bw, bh = bbox[2]-bbox[0], bbox[3]-bbox[1]
            if 0 < bw <= limit_w and 0 < bh <= limit_h:
                fitted = (size, font, commands, spacing, math.ceil(bw), math.ceil(bh))
                break
        if fitted is None:
            raise ValueError('Complete text cannot fit above readability floor; revise layout/canvas: ' + item['id'])
        size, font, commands, spacing, bw, bh = fitted
        alignment = item.get('align', 'left')
        if alignment not in ('left', 'center', 'right'):
            raise ValueError('align must be left, center or right')
        x = left if alignment == 'left' else right-bw if alignment == 'right' else left+(right-left-bw)//2
        patch = Image.new('RGBA', (bw, bh))
        draw = ImageDraw.Draw(patch)
        color = item.get('color', '#202020')
        for value, dx, dy in commands:
            if direction == 'horizontal':
                draw.multiline_text((dx, dy), value, font=font, spacing=spacing, fill=color)
            else:
                draw.text((dx, dy), value, font=font, fill=color)
        actual = patch.getbbox()
        if actual is None:
            raise ValueError('Text layer has no visible pixels')
        actual_box = [x+actual[0], top+actual[1], x+actual[2], top+actual[3]]
        layers.append((patch, x, top))
        metrics.append({'id':item['id'], 'role':role, 'direction':direction,
                        'bbox':actual_box, 'font_size_px':size, 'text':text,
                        'font':str(font_path), 'leading':leading})
        if role == 'title':
            title_sizes.append(size)
    geometry = geometry_checks(w, h, metrics, subjects, profile)
    if geometry['status'] != 'pass':
        raise ValueError('Typography hard constraints failed: ' + '; '.join(geometry['failures']))
    text_layer = Image.new('RGBA', (w, h))
    for patch, x, y in layers:
        text_layer.alpha_composite(patch, (x, y))
    composed = Image.alpha_composite(background, text_layer)
    out_dir.mkdir(parents=True, exist_ok=True)
    text_layer.save(destinations[0])
    composed.save(destinations[1])
    report = {'profile_id': p['id'], 'image':str(destinations[1]),
              'image_sha256':hashlib.sha256(destinations[1].read_bytes()).hexdigest(),
              'width':w, 'height':h, 'items':metrics, 'subject_boxes':subjects,
              'geometry':geometry, 'status':'working preview; actual visual review and 终版确认 still required',
              'limitations':'Geometry only: graphic priority, negative space, contrast, intended-size readability and required-asset coverage need pixel review.'}
    destinations[2].write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', required=True, type=Path)
    parser.add_argument('--out-dir', required=True, type=Path)
    args = parser.parse_args()
    try:
        request = json.loads(args.request.read_text(encoding='utf-8-sig'))
        print(json.dumps(render(request, args.out_dir), ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'error':str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
