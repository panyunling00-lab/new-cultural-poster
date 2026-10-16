"""Persistent HG1/HG2 and final-version confirmation checks for cultural-poster-generator.

python human_gate.py --state /task/hg-state.json --request /task/hg-request.json
Requests are JSON, never interactive stdin. Exit 0=accepted/allowed, 2=blocked.
This records human evidence supplied by Codex; it cannot authenticate chat replies.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import uuid
from preflight import validate as validate_preflight
from build_prompt import candidate_pool, ROOT


class GateError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise GateError(message)


def image_record(value):
    path = Path(str(value)).expanduser().resolve()
    require(path.is_file(), '图片不存在：' + str(path))
    require(path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp'), '仅登记 PNG/JPEG/WebP 图片')
    require(path.stat().st_size > 0, '图片文件为空')
    return {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def unchanged(record):
    require(image_record(record['path']) == record, '图片已变更，必须重新展示并确认')


def evidence(request):
    # The host must supply an actual human message, not model-generated consent.
    value = request.get('human_message')
    require(isinstance(value, str) and bool(value.strip()), '必须记录真实用户回复原文')
    return value.strip()


def transition(previous, request):
    action = request.get('action')
    if action == 'init':
        require(previous is None, '状态已存在，请使用现有任务或另建状态文件')
        return {'schema': 1, 'task_id': str(uuid.uuid4()), 'revision': 0,
                'stage': 'analyze_content', 'brief': {}, 'directions': {},
                'selected': None, 'poster': None, 'approval': None, 'history': []}
    require(previous is not None, '请先初始化任务')
    state = copy.deepcopy(previous)
    if action == 'status':
        return state
    require(request.get('revision') == state['revision'], '记录版本过期，请先读取 status')
    stage = state['stage']
    event = {'action': action}

    if action == 'brief':
        brief = request.get('brief')
        require(isinstance(brief, dict), 'brief 必须是对象')
        theme_status = request.get('theme_status')
        require(theme_status in ('clear', 'missing', 'unclear', 'conflict'), '须由内容分析给出主题状态')
        clear = theme_status == 'clear' and isinstance(brief.get('theme'), str) and bool(brief['theme'].strip())
        if clear:
            validate_preflight(brief)
        state.update(brief=brief, stage='plan_directions' if clear else 'awaiting_theme',
                     theme_status=theme_status, directions={}, selected=None, poster=None, approval=None)
        # Missing task facts stay absent, but complete extraction and canvas evidence are mandatory.
    elif action == 'directions':
        require(stage == 'plan_directions', '仅在主题明确并允许规划时登记方向')
        items = request.get('directions')
        require(isinstance(items, list) and len(items) == 3, '必须登记三张 A/B/C 独立图片')
        require({d.get('id') for d in items} == {'A', 'B', 'C'}, '编号必须恰好为 A/B/C')
        ratio = validate_preflight(state['brief'])
        require(len({d.get('style_id') for d in items}) == 3, 'A/B/C 必须是三个不同画风')
        require(len({d.get('layout_id') for d in items}) == 3, 'A/B/C 必须是三个不同构图')
        pool = candidate_pool(state['brief'])
        from PIL import Image
        for d in items:
            require((ROOT/'references/style'/str(d.get('style_id')+'.md')).is_file(), '画风定义不存在')
            require(d.get('layout_id') in pool, '构图不符合本次活动分类池')
            require(d.get('fit_evidence'), '缺少画风、构图适配本次主题与素材的依据')
            with Image.open(d['path']) as im:
                w,h=im.size
            require(w*ratio[1] == h*ratio[0], '预览实际画幅不符合任务比例')
        directions = {d['id']: dict(image=image_record(d.get('path', '')),
                                    version=str(uuid.uuid4()),
                                    style_id=d.get('style_id'), layout_id=d.get('layout_id')) for d in items}
        require(len({d['image']['sha256'] for d in directions.values()}) == 3, '三张图片内容不能完全相同')
        state.update(directions=directions, stage='awaiting_direction', selected=None, poster=None, approval=None)
    elif action == 'select':
        require(stage == 'awaiting_direction', '当前不在 HG2')
        key = request.get('direction')
        require(key in state['directions'], '须选择当前 A/B/C')
        candidate = state['directions'][key]
        require(request.get('version') == candidate['version'], '所选方向版本已过期')
        unchanged(candidate['image'])
        event['human_message'] = evidence(request)
        state.update(selected={'id': key, **candidate}, stage='complete_poster', approval=None)
        state['refinement_feedback'] = request.get('refinement_feedback', '')
    elif action == 'poster':
        require(stage in ('complete_poster', 'review_poster'), '先通过 HG2 或提出局部修改')
        unchanged(state['selected']['image'])
        require(request.get('selected_version') == state['selected']['version'], '成稿必须关联当前选中预览')
        require(request.get('production_mode') in ('edit', 'composite'), '新生图片须返回 HG2，不能替代已选图')
        state.update(poster={'image': image_record(request.get('path', '')),
                             'version': str(uuid.uuid4()), 'review': None},
                     stage='review_poster', approval=None)
    elif action == 'review':
        require(stage == 'review_poster' and state['poster'], '尚无待质检成稿')
        require(request.get('version') == state['poster']['version'], '质检版本不匹配')
        unchanged(state['poster']['image'])
        decision = request.get('decision')
        require(decision in ('pass', 'revise', 'rework direction', 'needs verification', 'not assessed'), '无效质检结论')
        require(bool(str(request.get('review_evidence', '')).strip()), '须记录质检依据或报告路径')
        state['poster']['review'] = {'decision': decision, 'evidence': request['review_evidence']}
        state['stage'] = 'awaiting_export_approval' if decision == 'pass' else 'review_poster'
    elif action in ('confirm_final', 'approve'):
        require(stage == 'awaiting_export_approval', '成稿通过质检后才能询问是否终版')
        require(request.get('confirm') is True, '必须明确确认当前图片为终版')
        require(request.get('version') == state['poster']['version'], '不能批准旧成稿')
        unchanged(state['poster']['image'])
        event['human_message'] = evidence(request)
        state.update(approval={'version': state['poster']['version'],
                               'sha256': state['poster']['image']['sha256'],
                               'human_message': event['human_message']}, stage='export_allowed')
    elif action == 'feedback':
        require(stage in ('awaiting_direction', 'awaiting_export_approval', 'export_allowed', 'exported', 'review_poster'), '当前不接受此反馈操作')
        event['human_message'] = evidence(request)
        route = request.get('route')
        require(route in ('new_directions', 'local_revision'), '请选择重选方向或局部修改')
        if route == 'new_directions':
            state.update(stage='plan_directions', directions={}, selected=None, poster=None, approval=None)
        else:
            require(state['selected'] and state['poster'], '局部修改需要已有选中方向和成稿')
            state.update(stage='complete_poster', approval=None)
            state['refinement_feedback'] = event['human_message']
    elif action == 'check':
        target = request.get('target')
        allowed = {'directions': 'plan_directions', 'complete': 'complete_poster', 'export': 'export_allowed'}
        require(target in allowed and stage == allowed[target], '当前阶段不允许该操作：' + str(target))
        if target == 'complete':
            unchanged(state['selected']['image'])
        if target == 'export':
            unchanged(state['poster']['image'])
            require(state['approval']['version'] == state['poster']['version'], '导出批准版本不匹配')
        return state
    elif action == 'exported':
        require(stage == 'export_allowed', '尚未允许导出')
        unchanged(state['poster']['image'])
        require(request.get('version') == state['approval']['version'], '导出版本不匹配')
        exported = image_record(request.get('path', ''))
        require(exported['sha256'] == state['approval']['sha256'], '终版确认后只能交付原文件或逐字节相同副本；格式转换须在确认前完成')
        state.update(stage='exported', export=exported)
    else:
        raise GateError('未知操作')

    state['revision'] += 1
    event.update(revision=state['revision'], stage=state['stage'])
    state['history'].append(event)
    return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', required=True)
    parser.add_argument('--request', required=True)
    args = parser.parse_args()
    try:
        path = Path(args.state).resolve()
        previous = json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else None
        request = json.loads(Path(args.request).read_text(encoding='utf-8-sig'))
        require(isinstance(request, dict), '请求必须为 JSON 对象')
        result = transition(previous, request)
        if request['action'] not in ('status', 'check'):
            path.parent.mkdir(parents=True, exist_ok=True)
            temp = path.with_suffix(path.suffix + '.tmp')
            temp.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
            temp.replace(path)
        print(json.dumps({'ok': True, 'state': result}, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'ok': False, 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
