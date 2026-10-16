"""Evaluate recorded visual evidence against cultural quality-rubric v1.2.

python check_poster.py --request quality-request.json --out quality-report.json
Exit 0: pass; 2: assessed but not passed; 1: invalid request.
Pillow enables actual decode and dimensions; missing Pillow yields unknown.
No OCR, model calls, or automatic human approval are performed.
"""
import argparse
import hashlib
import json
from pathlib import Path
from typography_policy import DEFAULT_PROFILE, PROFILE_FILES, review_typography

WEIGHTS = {'key_visual': dict(zip('ABCDEFG', (25, 20, 20, 15, 10, 10, 0))),
           'final_poster': dict(zip('ABCDEFG', (20, 15, 20, 10, 10, 20, 5)))}


def inspect_image(path):
    try:
        from PIL import Image
    except ImportError:
        return {'status': 'unknown', 'reason': '缺少 Pillow，未解码图片或检查尺寸'}
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            image.load()
            return {'status': 'pass', 'width': image.width, 'height': image.height,
                    'format': image.format, 'mode': image.mode}
    except Exception as error:
        return {'status': 'fail', 'reason': '图片解码失败：' + str(error)}


def active_profile(request):
    """Active typography profile: request field, then recorded id, then default."""
    review = request.get('visual_review') if isinstance(request.get('visual_review'), dict) else {}
    recorded = review.get('typography') if isinstance(review.get('typography'), dict) else {}
    name = request.get('typography_profile') or recorded.get('profile_id') or DEFAULT_PROFILE
    if name not in PROFILE_FILES:
        raise ValueError('unknown typography profile: ' + str(name))
    return name


def evaluate(request, inspector=inspect_image):
    stage = request.get('stage')
    if stage not in WEIGHTS:
        raise ValueError('stage 必须为 key_visual 或 final_poster')
    path = Path(request.get('image', '')).resolve()
    if not path.is_file():
        return {'decision': 'not assessed', 'stage': stage, 'image': str(path),
                'total': None, 'reason': '未找到实际图片', 'human_approval': False}
    image_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    inspection = inspector(path)
    spec = request.get('spec', {})
    technical = []
    technical_unknown = inspection['status'] == 'unknown'
    technical_fail = inspection['status'] == 'fail'
    if inspection['status'] == 'pass':
        w, h = inspection['width'], inspection['height']
        for key, actual in (('width', w), ('height', h)):
            if key in spec:
                ok = actual == spec[key]
                technical.append({'check': key, 'expected': spec[key], 'actual': actual, 'status': 'pass' if ok else 'fail'})
                technical_fail |= not ok
        if 'format' in spec:
            normalize = lambda v: 'JPEG' if str(v).upper() in ('JPG', 'JPEG') else str(v).upper()
            ok = normalize(inspection['format']) == normalize(spec['format'])
            technical.append({'check': 'format', 'expected': spec['format'], 'actual': inspection['format'], 'status': 'pass' if ok else 'fail'})
            technical_fail |= not ok
        if 'ratio' in spec:
            a, b = (int(x) for x in spec['ratio'].split(':'))
            if a <= 0 or b <= 0:
                raise ValueError('比例必须为正整数，例如 2:3')
            ok = w * b == h * a
            technical.append({'check': 'ratio', 'expected': spec['ratio'], 'actual': f'{w}:{h}', 'status': 'pass' if ok else 'fail'})
            technical_fail |= not ok

    review = request.get('visual_review', {})
    profile = active_profile(request)
    bound = review.get('image_sha256') == image_hash and review.get('stage') == stage
    gates = {}
    for key in ('H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'):
        item = review.get('hard_gates', {}).get(key, {}) if bound else {}
        status = item.get('status', 'unknown')
        if status not in ('pass', 'fail', 'unknown', 'not_applicable'):
            raise ValueError('无效硬门槛状态：' + key)
        evidence = str(item.get('evidence', '')).strip()
        if not evidence:
            status, evidence = 'unknown', '缺少当前图片的检查依据'
        if stage == 'final_poster' and key in ('H1', 'H5', 'H7') and status == 'not_applicable':
            status, evidence = 'unknown', '成稿的核心需求、使用要求和材料覆盖必须核验'
        gates[key] = {'status': status, 'evidence': evidence}
    if technical_fail:
        gates['H5'] = {'status': 'fail', 'evidence': '技术检查失败，详见 inspection/technical_checks'}
    elif technical_unknown and gates['H5']['status'] != 'fail':
        gates['H5'] = {'status': 'unknown', 'evidence': inspection['reason']}
    if stage == 'key_visual':
        gates['H7'] = {'status': 'not_applicable', 'evidence': 'pending final poster verification'}

    typography = review_typography(review.get('typography') if bound else None,
                                   inspection.get('width', 0), inspection.get('height', 0), stage,
                                   profile=profile) if inspection['status'] == 'pass' else {
                                       'status': 'unknown', 'evidence': 'Cannot inspect typography without decoded canvas dimensions'}
    if typography['status'] != 'pass':
        if gates['H1']['status'] != 'fail' or typography['status'] == 'fail':
            gates['H1'] = {'status': typography['status'],
                           'evidence': 'Typography profile: ' + json.dumps(typography, ensure_ascii=False)}

    dimensions = {}
    complete = bound
    for key, weight in WEIGHTS[stage].items():
        if weight == 0:
            continue
        item = review.get('dimensions', {}).get(key, {}) if bound else {}
        score, evidence = item.get('score'), str(item.get('evidence', '')).strip()
        valid = type(score) is int and 0 <= score <= 5 and bool(evidence)
        complete &= valid
        dimensions[key] = {'score': score if valid else None, 'weight': weight,
                           'evidence': evidence if valid else 'not assessed'}
    total = round(sum(d['score'] / 5 * d['weight'] for d in dimensions.values()), 1) if complete else None
    unknown = any(g['status'] == 'unknown' for g in gates.values())
    failed = any(g['status'] == 'fail' for g in gates.values())
    if not complete:
        decision = 'not assessed'
    elif unknown:
        decision = 'needs verification'
    elif total < 70:
        decision = 'rework direction'
    elif failed or total < 85 or any(d['score'] < 3 for d in dimensions.values()):
        decision = 'revise'
    else:
        decision = 'pass'
    return {'rubric_version': '1.2', 'stage': stage, 'image': str(path),
            'image_sha256': image_hash, 'inspection': inspection, 'technical_checks': technical,
            'visual_review_bound_to_image': bound, 'typography_profile': profile, 'hard_gates': gates,
            'typography_checks': typography,
            'dimensions': dimensions, 'total': total, 'decision': decision,
            'known_failures': [k for k, v in gates.items() if v['status'] == 'fail'],
            'human_approval': False,
            'limitations': '评分与文化结论来自提交的看图证据；脚本只核算规则，不认证证据真实性。未执行 OCR、二维码或印刷检查。'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    try:
        request = json.loads(Path(args.request).read_text(encoding='utf-8-sig'))
        report = evaluate(request)
        destination = Path(args.out).resolve()
        if destination == Path(request.get('image', '')).resolve() or destination == Path(args.request).resolve():
            raise ValueError('报告路径不能覆盖原图或输入文件')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report['decision'] == 'pass' else 2
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
