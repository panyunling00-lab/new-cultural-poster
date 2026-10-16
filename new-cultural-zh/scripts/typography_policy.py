"""Typography policy: profile-aware defaults, prompt blocks and quality checks.

Two pluggable profiles share this module:

* ``design-free-v1`` (default) -- no numeric design caps; geometry checks only
  describe the measurement and never fail on size, overlap or whitespace.
* ``small-type-refined-v1`` -- the measured small-type caps enforced as
  pass/fail verdicts.

``assets/typography-defaults.json`` is a pointer file; the numbers live in the
per-profile files listed under ``profiles``. Every public helper accepts an
optional ``profile`` argument; ``None`` selects ``default_profile``.
"""
import copy
import json
import math
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
DEFAULTS = json.loads((ASSETS / 'typography-defaults.json').read_text(encoding='utf-8'))
DEFAULT_PROFILE = DEFAULTS['default_profile']
PROFILE_FILES = DEFAULTS['profiles']

DESIGN_FREE = 'design-free-v1'
SMALL_TYPE = 'small-type-refined-v1'

_PROFILE_CACHE = {}


def _resolve(profile):
    name = profile or DEFAULT_PROFILE
    if name not in PROFILE_FILES:
        raise ValueError('unknown typography profile: ' + str(name))
    return name


def load_profile(profile=None):
    """Load the numeric profile file for ``profile`` and verify its ``id``."""
    name = _resolve(profile)
    if name not in _PROFILE_CACHE:
        path = ASSETS / PROFILE_FILES[name]
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('id') != name:
            raise ValueError('typography profile id mismatch: ' + str(data.get('id')) + ' != ' + name)
        _PROFILE_CACHE[name] = data
    return _PROFILE_CACHE[name]


def profile_id(profile=None):
    return load_profile(profile)['id']


def role_name(role):
    return role if role in ('title', 'subtitle') else 'body'


def default_font_sizes(width, height, profile=None):
    """Profile-specific adjustable renderer starting sizes."""
    p = load_profile(profile)
    short = min(width, height)
    if p['id'] == DESIGN_FREE:
        return {role: short * p['renderer_' + role + '_short_side_ratio'] for role in ('title', 'subtitle', 'body')}
    title = short * p['title_base_font_short_side_ratio'] * p['text_scale_weight']
    return {'title': title, 'subtitle': title * p['subtitle_title_ratio'],
            'body': title * p['body_title_ratio']}


def production_policy(profile=None):
    return copy.deepcopy(load_profile(profile))


def prompt_rules(profile=None, language=None):
    """Return the active profile's constraint block for ``language`` (zh default)."""
    name = _resolve(profile)
    language = 'zh' if language is None else language
    if language not in ('zh', 'en'):
        raise ValueError('language must be zh or en')
    p = load_profile(name)
    if name == DESIGN_FREE:
        if language == 'zh':
            return (
                'design-free-v1：字是设计材料，鼓励按主题选择变形、错落、叠压、遮断、立体、网点、飞白、竖排或沿路径；选0–2个手法，不堆砌。'
                '满版画面上叠字、与主体穿插、被前景局部遮挡均可，只要所有必需文字仍清晰可辨。'
                '避免板正字库感、机械均匀排版、伪文字与硬塞小人；功能信息可以稳定排版，以清晰为准。'
                '没有固定字号、面积、留白、字距行距、角色比例或安全角落；媒介按主题选择，不默认纸感或素雅。人物仅在主题需要时出现，尺度自然，不强制微缩。'
                '两条硬底线：copy_items中全部必需文字逐字正确且正常观看尺寸下清晰可读；不出现伪文字、乱码，不编造事实或文化归属。'
                '不能裁掉唯一必需字、改笔画成别字、添加未提供口号；缺失事实保持缺失。必须检查实际图像，不能凭提示词宣称通过。'
                '画面满版出血，不出现底部纯色横带或边框。')
        return (
            'design-free-v1: type is design material. By theme, choose deformation, stagger, overprint, interruption, '
            'dimensional form, halftone, flying-white, vertical setting or along-path; pick 0-2 moves, do not pile them up. '
            'Overprinting type on a full-bleed image, interleaving with the subject, or partial occlusion by a foreground '
            'element are all allowed, as long as every required string stays clearly legible. '
            'Avoid a rigid font-library feel, mechanically even typesetting, pseudo-text and forced small figures; '
            'functional information may use stable typesetting, prioritising clarity. '
            'There is no fixed font size, area, negative space, tracking, leading, role ratio or safe corner; choose the '
            'medium by theme, without defaulting to paper feel or restraint. People appear only when the theme needs them, '
            'at a natural scale, not forced miniature. '
            'Two hard baselines: every required string in copy_items is character-accurate and clearly legible at normal '
            'viewing size; no pseudo-text or gibberish, and no invented facts or cultural attribution. '
            'Do not crop the only required characters, change strokes into wrong characters, or add slogans not supplied; '
            'missing facts stay missing. Inspect the actual image; prompt wording alone never proves compliance. '
            'Full-bleed composition; no solid colour bottom band or border.')
    if language == 'en':
        return (
            'Mandatory small-type refinement for this image and every variant/edit: modern minimal, refined, spacious composition. '
            'Graphics/illustration are the first visual focus and support the canvas; event text is a separate restrained accent placed in the selected layout\'s own Text Placement zone. Minimum edge margins are whitespace constraints, not a fixed safe corner; each A/B/C direction and each variant must place title/information in spatially different regions. Three images sharing one text zone count as the same composition. '
            f'Internal Text Scale weight {p["text_scale_weight"]}; title nominal size {p["title_base_font_short_side_ratio"] * p["text_scale_weight"]:.3f} of the short canvas side, hard maximum {p["title_font_short_side_ratio_max"]:.3f}. '
            f'Measure the whole title block including all lines, bilingual titles and effects: horizontal block height targets <= {p["title_block_target_ratio"]:.0%} of canvas height, absolute cap {p["title_block_max_ratio"]:.0%}; '
            f'vertical block width targets <= {p["title_block_target_ratio"]:.0%} of canvas width, absolute cap {p["title_block_max_ratio"]:.0%}. '
            f'Subtitle nominal size {p["subtitle_title_ratio"]:.0%} of title, maximum {p["subtitle_title_ratio_max"]:.0%}; '
            f'body and ALL functional copy {p["body_title_ratio"]:.0%}, maximum {p["body_title_ratio_max"]:.0%}. '
            'Use fine small text, readable strokes and precise alignment; never large display paragraphs or giant/cropped/repeated event titles. '
            f'Edge margins >= {p["safe_margin_x_ratio"]:.0%} of canvas width and {p["safe_margin_y_ratio"]:.0%} of canvas height; '
            f'clear text-block gaps >= {p["text_padding_short_side_ratio"]:.0%} of short side; core-subject clearance >= {p["subject_clearance_short_side_ratio"]:.0%}. '
            f'Purposeful low-detail negative space >= {p["negative_space_ratio_min"]:.0%} of canvas area; combined text-block area <= {p["text_block_area_ratio_max"]:.0%}. '
            'Preserve every required string and asset. If copy cannot fit legibly, revise layout/canvas; do not omit copy or break caps. '
            'These rules override conflicting library scale/density instructions. For text-free generation reserve these regions without drawing any letters; apply the same caps in later typesetting. '
            'Inspect actual pixels; prompt wording alone is not compliance.'
        )
    return (
        '本次成图及每一版衍生/编辑都必须执行小字精修：现代极简、精致、留白充分的构图。'
        '图形/插画是第一视觉焦点并支撑画面；活动文字是独立的克制点缀，放在所选版式自身的文字放置区。最小边距是留白约束，不是固定的安全角落；A/B/C 每个方向及每一版都必须把标题/信息放在空间上不同的区域。三张图共用同一个文字区视为同一构图。'
        f'内部文字尺度权重 {p["text_scale_weight"]}；标题名义字号 {p["title_base_font_short_side_ratio"] * p["text_scale_weight"]:.3f} × 画布短边，硬上限 {p["title_font_short_side_ratio_max"]:.3f}。'
        f'测量包含所有行、双语标题和效果的整个标题块：横排块高目标 ≤ 画布高 {p["title_block_target_ratio"]:.0%}，绝对上限 {p["title_block_max_ratio"]:.0%}；'
        f'竖排块宽目标 ≤ 画布宽 {p["title_block_target_ratio"]:.0%}，绝对上限 {p["title_block_max_ratio"]:.0%}。'
        f'副标题名义字号 {p["subtitle_title_ratio"]:.0%} × 标题，上限 {p["subtitle_title_ratio_max"]:.0%}；'
        f'正文及全部功能信息 {p["body_title_ratio"]:.0%}，上限 {p["body_title_ratio_max"]:.0%}。'
        '使用精细小字、可读笔画和精确对齐；绝不使用大段展示文字或巨大/裁切/重复的活动标题。'
        f'边距 ≥ 画布宽 {p["safe_margin_x_ratio"]:.0%}、画布高 {p["safe_margin_y_ratio"]:.0%}；'
        f'文字块之间净距 ≥ 短边 {p["text_padding_short_side_ratio"]:.0%}；主体让位 ≥ {p["subject_clearance_short_side_ratio"]:.0%}。'
        f'有意图的低细节留白 ≥ 画布面积 {p["negative_space_ratio_min"]:.0%}；文字块合计面积 ≤ {p["text_block_area_ratio_max"]:.0%}。'
        '保留全部必需字符串与资产。文案放不下时调整版式/画布，不得删减文案或突破上限。'
        '这些规则优先于素材库中冲突的字号/密度指令。无字生成时预留这些区域但不绘制任何字母；后期排版沿用同一上限。'
        '必须检查实际像素；仅凭提示词声明不算达标。'
    )


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def valid_box(box, width, height):
    return (isinstance(box, (list, tuple)) and len(box) == 4 and all(number(v) for v in box)
            and 0 <= box[0] < box[2] <= width and 0 <= box[1] < box[3] <= height)


def too_close(a, b, gap):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0]
                or a[3] + gap <= b[1] or b[3] + gap <= a[1])


def _validate_measurements(width, height, items, subject_boxes, directions):
    """Common validation shared by both profiles; raises on malformed data."""
    if not number(width) or not number(height) or min(width, height) <= 0:
        raise ValueError('positive canvas dimensions required')
    if not isinstance(items, list):
        raise ValueError('typography items must be a list')
    ids = set()
    prepared, titles = [], []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id'].strip():
            raise ValueError('each measured item requires a nonempty id')
        if item['id'] in ids:
            raise ValueError('duplicate typography item id')
        ids.add(item['id'])
        if not valid_box(item.get('bbox'), width, height):
            raise ValueError('invalid actual glyph bbox: ' + item['id'])
        size = item.get('font_size_px')
        if not number(size) or size <= 0:
            raise ValueError('positive font_size_px required: ' + item['id'])
        if item.get('direction', 'horizontal') not in directions:
            raise ValueError('direction must be one of: ' + ', '.join(directions))
        if item.get('role') not in ('title', 'subtitle', 'body'):
            raise ValueError('measured role must be title, subtitle or body')
        prepared.append(item)
        if item['role'] == 'title':
            titles.append(item)
    for box in subject_boxes:
        if not valid_box(box, width, height):
            raise ValueError('invalid protected subject box')
    return prepared, titles


def geometry_checks(width, height, items, subject_boxes=(), profile=None):
    """Measure typography items under the active profile.

    ``design-free-v1`` only describes the geometry: overlaps, huge sizes and any
    whitespace are never a failure, though malformed measurements still raise.
    ``small-type-refined-v1`` enforces the profile's numeric caps as pass/fail.
    """
    name = _resolve(profile)
    p = load_profile(name)
    if name == DESIGN_FREE:
        prepared, _ = _validate_measurements(width, height, items, subject_boxes,
                                              ('horizontal', 'vertical', 'path', 'mixed'))
        area = sum((i['bbox'][2] - i['bbox'][0]) * (i['bbox'][3] - i['bbox'][1]) for i in prepared) / (width * height)
        return {'status': 'pass', 'failures': [], 'title_block_ratio': None,
                'text_block_area_ratio': area, 'profile_id': p['id'],
                'note': 'Geometry is descriptive; actual copy and readability require visual evidence.'}

    prepared, titles = _validate_measurements(width, height, items, subject_boxes, ('horizontal', 'vertical'))
    short = min(width, height)
    failures = []
    for item in prepared:
        box = item['bbox']
        if (box[0] < width * p['safe_margin_x_ratio'] or box[2] > width * (1 - p['safe_margin_x_ratio'])
                or box[1] < height * p['safe_margin_y_ratio'] or box[3] > height * (1 - p['safe_margin_y_ratio'])):
            failures.append(item['id'] + ': text outside 8% safe margins')
    reference = min((i['font_size_px'] for i in titles), default=default_font_sizes(width, height, name)['title'])
    for item in prepared:
        role = item['role']
        cap = (short * p['title_font_short_side_ratio_max'] if role == 'title'
               else reference * p[role + '_title_ratio_max'])
        if item['font_size_px'] > cap + 1e-6:
            failures.append(item['id'] + ': role font size exceeds hard cap')
    title_ratio = None
    if titles:
        directions = {i.get('direction', 'horizontal') for i in titles}
        if len(directions) != 1:
            failures.append('mixed title directions require a new layout')
        else:
            axis = 1 if directions == {'horizontal'} else 0
            title_ratio = (max(i['bbox'][axis + 2] for i in titles) - min(i['bbox'][axis] for i in titles)) / (height if axis == 1 else width)
            if title_ratio > p['title_block_max_ratio'] + 1e-6:
                failures.append('combined title block exceeds 20% cap')
    area = sum((i['bbox'][2] - i['bbox'][0]) * (i['bbox'][3] - i['bbox'][1]) for i in prepared) / (width * height)
    if area > p['text_block_area_ratio_max'] + 1e-6:
        failures.append('combined text-block area exceeds 20%')
    for index, item in enumerate(prepared):
        for other in prepared[index + 1:]:
            if too_close(item['bbox'], other['bbox'], short * p['text_padding_short_side_ratio']):
                failures.append(item['id'] + '/' + other['id'] + ': insufficient text breathing room')
        for box in subject_boxes:
            if too_close(item['bbox'], box, short * p['subject_clearance_short_side_ratio']):
                failures.append(item['id'] + ': core-subject clearance below 4%')
    return {'status': 'fail' if failures else 'pass', 'failures': failures,
            'title_block_ratio': title_ratio, 'text_block_area_ratio': area,
            'profile_id': p['id']}


def review_typography(review, width, height, stage, profile=None):
    """Validate recorded ``visual_review.typography`` evidence for the profile."""
    name = _resolve(profile)
    p = load_profile(name)
    if not isinstance(review, dict) or review.get('profile_id') != p['id'] or not str(review.get('evidence', '')).strip():
        label = 'Missing current-image design-free-v1 review evidence' if name == DESIGN_FREE else 'Missing current-image small-type profile evidence'
        return {'status': 'unknown', 'evidence': label}
    failures, missing = [], []
    if name == DESIGN_FREE:
        for flag in ('intended_size_readable', 'exact_copy_verified', 'no_pseudo_text', 'facts_preserved'):
            value = review.get(flag)
            if value is False:
                failures.append(flag + ' failed actual-image review')
            elif value is not True:
                missing.append(flag)
        geometry = None
        if 'items' in review:
            try:
                geometry = geometry_checks(width, height, review['items'], profile=name)
            except ValueError as error:
                missing.append(str(error))
        status = 'fail' if failures else 'unknown' if missing else 'pass'
        return {'status': status, 'evidence': review['evidence'], 'failures': failures,
                'missing': missing, 'geometry': geometry, 'profile_id': p['id']}

    for flag in ('graphic_primary', 'subject_clearance_verified', 'intended_size_readable'):
        value = review.get(flag)
        if value is False:
            failures.append(flag + ' failed actual-image review')
        elif value is not True:
            missing.append(flag)
    space = review.get('negative_space_ratio')
    if not number(space) or not 0 <= space <= 1:
        missing.append('negative_space_ratio')
    elif space < p['negative_space_ratio_min']:
        failures.append('negative space below 30%')
    items = review.get('items')
    geometry = None
    if items is None and stage == 'key_visual':
        items = []
    if items is None or (stage == 'final_poster' and not items and not review.get('text_free_confirmed', False)):
        missing.append('actual text geometry or confirmed text-free brief')
    else:
        try:
            geometry = geometry_checks(width, height, items, profile=name)
            failures.extend(geometry['failures'])
        except ValueError as error:
            missing.append(str(error))
    status = 'fail' if failures else 'unknown' if missing else 'pass'
    return {'status': status, 'evidence': review['evidence'], 'failures': failures,
            'missing': missing, 'geometry': geometry, 'profile_id': p['id']}
