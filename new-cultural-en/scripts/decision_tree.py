#!/usr/bin/env python3
"""Deterministic candidate routing; does not inspect images or judge aesthetics."""
import argparse
import json
from pathlib import Path
from build_prompt import MONTAGE_LAYOUTS, DEFAULT_PROFILE, mapping, candidate_pool, resolve_profile, ROOT

RELATIONS = {
    'single':['centered-hero','off-center-hero'], 'many':['modular-grid'],
    'process':['layered-depth','frame-within-frame'],
    'comparison':['split-horizontal','split-vertical'],
    'space':['axonometric-spatial','large-geometry','layered-depth'],
    'transformation':['folded-space','layered-depth'],
    'movement':['diagonal-dynamic','radial-composition'],
    'gathering':['radial-composition','modular-grid'], 'framed':['frame-within-frame'],
    'symbol':['minimal-white-space','large-geometry'],
    'reading':['editorial-column','split-vertical'],
    'immersive':['full-bleed-image-overlay'],
    'experimental':['disorder-layout','folded-space'],
}

def decide(d):
    if not isinstance(d, dict):
        raise ValueError('输入必须是 JSON 对象')
    missing = [k for k in ('categories','relation','motion','copy_density','mood') if not d.get(k)]
    if missing:
        return {'status':'needs_analysis','missing':missing,'candidates':[]}
    for k, choices in {'relation':RELATIONS, 'motion':('static','dynamic'),
                       'copy_density':('low','high'), 'mood':('quiet','expressive')}.items():
        if not isinstance(d[k],str) or d[k] not in choices:
            raise ValueError('无效字段：'+k)
    pool = candidate_pool(d)
    profile = resolve_profile(d)
    known = {p.stem for p in (ROOT/'references/layout').glob('*.md')}
    excluded = d.get('excluded_layouts',[])
    if not isinstance(excluded,list) or any(not isinstance(x,str) or x not in known for x in excluded):
        raise ValueError('excluded_layouts 必须是真实布局 ID 数组')
    # Global rules plus the active profile's ineligible layouts.
    global_excluded = set(MONTAGE_LAYOUTS)
    if profile != DEFAULT_PROFILE:
        global_excluded.add('big-type-only')
    chosen = d.get('user_layout') or d.get('confirmed_layout')
    if chosen:
        if chosen not in known or chosen in global_excluded:
            return {'status':'conflict','reason':'指定布局不存在或违反当前文字规则','candidates':[]}
        if chosen in excluded:
            return {'status':'conflict','reason':'指定布局已确认不可用，需要明确调整','candidates':[]}
        return {'status':'fixed_layout','candidates':[chosen],
                'reason':'遵循用户指定或已确认方向；其他维度需另行设计三个预览',
                'category_override':chosen not in pool,'requires_visual_validation':True}
    primary = set(mapping()[d['categories'][0]]['primary'])
    relation = RELATIONS[d['relation']]
    ranked=[]
    for layout in pool:
        if layout in excluded:
            continue
        score=0; reasons=[]
        if layout in relation:
            score+=10;reasons.append('符合主要表达关系')
        if layout in primary:
            score+=5;reasons.append('主活动类别首选')
        if d['copy_density']=='high' and layout in ('editorial-column','modular-grid','split-vertical','split-horizontal'):
            score+=2;reasons.append('优先检查较多文案的容量')
        if d['motion']=='dynamic' and layout in ('diagonal-dynamic','radial-composition'):
            score+=2;reasons.append('符合动态表达')
        ranked.append({'layout':layout,'score':score,'reasons':reasons or ['类别允许的备选']})
    ranked.sort(key=lambda x:-x['score'])
    # Cover distinct main-category primaries before choosing a third alternative.
    suggestions=[x['layout'] for x in ranked if x['layout'] in primary][:2]
    suggestions += [x['layout'] for x in ranked if x['layout'] not in suggestions][:3-len(suggestions)]
    status='conflict' if not ranked else ('ready_for_design' if len(suggestions)==3 else 'needs_adjustment')
    return {'status':status,'categories':d['categories'],'candidates':ranked,
            'suggested_layouts':suggestions,'mood':d['mood'],
            'requires_visual_validation':True,
            'note':'排序分数是规则优先级，不是美学评分。检查参考、文案容量、文字区差异和风格适配后再生成。'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('brief',type=Path);a=p.parse_args()
    try:
        print(json.dumps(decide(json.loads(a.brief.read_text(encoding='utf-8-sig'))),ensure_ascii=False,indent=2))
    except (ValueError,TypeError,KeyError,OSError) as e:
        p.exit(2,str(e)+'\n')

if __name__=='__main__':main()
