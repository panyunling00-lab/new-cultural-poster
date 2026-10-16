"""Composite user-supplied logo/QR PNGs onto an unchanged poster canvas.

python overlay_assets.py --request assets-request.json --out-dir task/version
Outputs are working images; this helper never supplies human approval.
"""
import argparse
import hashlib
import io
import json
import math
from pathlib import Path
import sys

from PIL import Image


POSITIONS = {'top-right', 'top-left', 'bottom-left', 'bottom-right', 'center'}


def fraction(value, name, allow_zero=True):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or not 0 <= value <= 1
            or (not allow_zero and value == 0)):
        raise ValueError(name + ' must be a finite fraction in '
                         + ('[0, 1]' if allow_zero else '(0, 1]'))
    return value


def composite(request, out_dir):
    if not isinstance(request, dict):
        raise ValueError('request must be an object')
    background = Path(request['background']).resolve(strict=True)
    entries = request['assets']
    if not isinstance(entries, list) or not entries:
        raise ValueError('assets must be a nonempty list')
    output = Path(out_dir).resolve() / 'assets-overlay.png'
    if output.exists():
        raise FileExistsError('output already exists; use a new out-dir')
    background_bytes = background.read_bytes()
    with Image.open(io.BytesIO(background_bytes)) as source:
        source.load()
        canvas = source.convert('RGBA')
    width, height = canvas.size
    short_side = min(width, height)
    reports = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError('each asset must be an object')
        asset_path = Path(entry['path']).resolve(strict=True)
        if asset_path == output:
            raise ValueError('output must not replace an input asset')
        position = entry.get('position', 'top-right')
        if position not in POSITIONS:
            raise ValueError('unsupported position: ' + str(position))
        scale = fraction(entry.get('scale', 0.08), 'scale', allow_zero=False)
        margin = fraction(entry.get('margin', 0.03), 'margin')
        opacity = fraction(entry.get('opacity', 1.0), 'opacity')
        asset_bytes = asset_path.read_bytes()
        with Image.open(io.BytesIO(asset_bytes)) as source:
            if source.format != 'PNG':
                raise ValueError('asset must be a PNG: ' + str(asset_path))
            source.load()
            asset = source.convert('RGBA')
        longest = max(asset.size)
        target = max(1, round(short_side * scale))
        asset_width = max(1, round(asset.width * target / longest))
        asset_height = max(1, round(asset.height * target / longest))
        asset = asset.resize((asset_width, asset_height), Image.Resampling.LANCZOS)
        if opacity != 1:
            asset.putalpha(asset.getchannel('A').point(lambda alpha: round(alpha * opacity)))
        inset = round(short_side * margin)
        if position == 'center':
            left, top = (width - asset_width) // 2, (height - asset_height) // 2
        else:
            left = width - inset - asset_width if position.endswith('right') else inset
            top = height - inset - asset_height if position.startswith('bottom') else inset
        if left < 0 or top < 0 or left + asset_width > width or top + asset_height > height:
            raise ValueError('asset placement exceeds the actual canvas: ' + str(asset_path))
        canvas.alpha_composite(asset, dest=(left, top))
        reports.append({
            'id': entry.get('id'), 'path': str(asset_path),
            'position': position, 'scale': scale, 'margin': margin, 'opacity': opacity,
            'dimensions': [asset_width, asset_height],
            'bbox': [left, top, left + asset_width, top + asset_height],
            'sha256': hashlib.sha256(asset_bytes).hexdigest(),
        })
    if output == background:
        raise ValueError('output must not replace the background')
    output.parent.mkdir(parents=True, exist_ok=True)
    encoded = io.BytesIO()
    canvas.save(encoded, format='PNG')
    output_bytes = encoded.getvalue()
    # Exclusive creation also prevents overwriting a concurrently created file.
    with output.open('xb') as handle:
        handle.write(output_bytes)
    return {
        'output': str(output), 'format': 'PNG',
        'dimensions': [width, height], 'width': width, 'height': height,
        'sha256': hashlib.sha256(output_bytes).hexdigest(),
        'background': str(background),
        'background_sha256': hashlib.sha256(background_bytes).hexdigest(),
        'assets': reports,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', required=True)
    parser.add_argument('--out-dir', required=True)
    args = parser.parse_args()
    try:
        request = json.loads(Path(args.request).read_text(encoding='utf-8-sig'))
        report = composite(request, args.out_dir)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
