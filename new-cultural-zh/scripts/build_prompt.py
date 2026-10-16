#!/usr/bin/env python3
"""Assemble original cultural prompts from a reviewed JSON design brief."""
import argparse
import json
import re
from pathlib import Path
from typography_policy import DEFAULT_PROFILE, PROFILE_FILES, production_policy, prompt_rules
from preflight import validate as validate_preflight

ROOT = Path(__file__).resolve().parents[1]

# Global content rules: these montage layouts are excluded under EVERY profile.
MONTAGE_LAYOUTS = ('modular-grid', 'split-horizontal', 'split-vertical')
# Candidate pools follow the category mapping (selection-guide.md R7) under BOTH
# profiles: no profile appends layouts across categories. big-type-only stays
# reachable in design-free-v1 only through user_layout_override.

def read(name):
    return (ROOT / "references" / name).read_text(encoding="utf-8")

def mapping():
    rows = {}
    for line in read("selection-guide.md").splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) == 6 and parts[1] in "ABCDEFGH" and len(parts[1]) == 1:
            rows[parts[1]] = {
                "primary": re.findall(r"`([a-z-]+)`", parts[2]),
                "secondary": re.findall(r"`([a-z-]+)`", parts[3]),
                "specialist": re.findall(r"`([a-z-]+)`", parts[4]),
            }
    if set(rows) != set("ABCDEFGH"):
        raise ValueError("category mapping incomplete")
    return rows

def resolve_profile(data, profile=None):
    """Resolve the active typography profile name from an explicit value or the brief."""
    name = profile or (data.get('typography_profile') if isinstance(data, dict) else None) or DEFAULT_PROFILE
    if name not in PROFILE_FILES:
        raise ValueError('unknown typography profile: ' + str(name))
    return name


def candidate_pool(data, profile=None):
    name = resolve_profile(data, profile)
    categories = data.get("categories")
    if not isinstance(categories,list) or not categories or any(c not in mapping() for c in categories):
        raise ValueError("categories must be a nonempty A-H list, main category first; AI must classify")
    table = mapping()
    ids = []
    for c in categories:
        ids.extend(table[c]["primary"] + table[c]["secondary"])
        if (c == "A" and data.get("specialism") in ("calligraphy","seal-carving")) or (c == "C" and data.get("specialism") == "market"):
            ids.extend(table[c]["specialist"])
    excluded = set(MONTAGE_LAYOUTS)
    if name != DEFAULT_PROFILE:
        excluded.add('big-type-only')
    return [identifier for identifier in dict.fromkeys(ids) if identifier not in excluded]

# People rule: performing arts (B) and festivals/carnivals (E) have people in
# their visual core, and so do craft markets; a reference set containing only
# people also allows figures. Everything else defaults to no people.
PEOPLE_CATEGORIES = ('B', 'E')

def people_policy(data):
    """Resolve the people rule from the brief: allowed / avoid / forbidden."""
    explicit = data.get('people_policy')
    if explicit is not None:
        if explicit not in ('allowed', 'avoid', 'forbidden'):
            raise ValueError("people_policy must be allowed, avoid or forbidden")
        return explicit
    categories = data.get('categories') if isinstance(data, dict) else None
    if isinstance(categories, list) and (any(c in PEOPLE_CATEGORIES for c in categories)
                                         or data.get('specialism') == 'market'):
        return 'allowed'
    refs = data.get('reference_people')
    if refs is not None:
        if refs not in ('only-people', 'people-plus-content'):
            raise ValueError("reference_people must be only-people or people-plus-content")
        return 'allowed' if refs == 'only-people' else 'avoid'
    return 'forbidden'

PEOPLE_DIRECTIVES = {
    'forbidden': {
        'zh': '人物规则：默认不生成任何人物形象（真人、插画人物、人体剪影、手部特写、微型人物场景），也不用人物造型素材作主体；原始素材本身含人物且必须展示时不加篡改，先说明冲突并取得决定。',
        'en': 'People rule: by default generate no human figures (real people, illustrated characters, human silhouettes, hand close-ups, miniature-figure scenes) and use no human-shaped asset as the subject; when a supplied asset itself contains people and must be shown, do not alter it — state the conflict and get a decision first.'},
    'avoid': {
        'zh': '人物规则：参考素材同时包含人物与其他内容，尽量不以人物作视觉主体，优先用素材中的非人物内容表达主题；确需人物时先说明理由并取得决定。',
        'en': 'People rule: the reference material contains people alongside other content, so prefer non-people subjects and express the theme through the non-people material; use figures only when nothing else can carry the theme, and state the reason and get a decision first.'},
    'allowed': {
        'zh': '人物规则：本主题（演出、节庆/嘉年华、集市类，或参考素材仅含人物）允许人物；不得生成可辨认的真实或名人形象，提供的含人物素材必须保持忠实。',
        'en': 'People rule: people are allowed for this theme (performing arts, festivals/carnivals, a market, or reference material containing only people); do not generate recognizable real or celebrity likenesses, and keep supplied people-bearing assets faithful.'},
}

def people_directive(policy, language=None):
    language = language or 'zh'
    if language not in ('zh', 'en'):
        raise ValueError("language must be zh or en")
    if policy not in PEOPLE_DIRECTIVES:
        raise ValueError("unknown people policy: " + str(policy))
    return PEOPLE_DIRECTIVES[policy][language]

def definition(kind, identifier):
    if not isinstance(identifier,str) or not re.fullmatch(r"[a-z]+(?:-[a-z]+)*",identifier):
        raise ValueError("invalid definition ID")
    return read(kind + "/" + identifier + ".md")

def visual_sections(md):
    sections = re.split(r"(?m)^## ",md)
    return "\n".join(s for s in sections[1:] if not s.startswith(("Typography","Avoid")))

def negative_rules(language):
    """Read assets/negative-prompt.txt and return one language's half of each rule."""
    if language not in ("zh","en"):
        raise ValueError("language must be zh or en")
    lines=[]
    for raw in (ROOT/"assets"/"negative-prompt.txt").read_text(encoding="utf-8").splitlines():
        line=raw.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            raise ValueError("negative-prompt.txt rule lacks a 中文|English split: "+line)
        zh,en=[part.strip() for part in line.split("|",1)]
        if not zh or not en:
            raise ValueError("negative-prompt.txt rule has an empty side: "+line)
        lines.append(zh if language=="zh" else en)
    if len(lines) < 10:
        raise ValueError("negative-prompt.txt is truncated or over-commented")
    return lines

def pairing(number):
    guide = read("typography-system.md")
    pattern = r"(?ms)^### " + str(number) + r"\. .*?(?=^### |^## |\Z)"
    found = re.search(pattern,guide)
    if not found:
        raise ValueError("pairing must be 1-8")
    description = re.search(r"(?:Prompt-ready visual description|提示词字形描述)[^:：\n]*[:：]\s*(.+)",found.group())
    if not description:
        raise ValueError("pairing %d has no prompt-ready visual description" % number)
    return description.group(1)

def is_landscape(canvas):
    """Detect a wide canvas from a W:H ratio or an explicit orientation word."""
    text = str(canvas or "")
    m = re.search(r"(\d+)\s*:\s*(\d+)", text)
    if m:
        w, h = int(m.group(1)), int(m.group(2))
        if w > h:
            return True
        if h > w:
            return False
    return bool(re.search(r"landscape|horizontal|横", text, re.I))

def reference_plan(data):
    mode = data.get('reference_mode')
    if mode not in ('direct', 'features'):
        raise ValueError('reference_mode must be direct or features')
    refs = data.get('references')
    if not isinstance(refs, list) or not refs:
        raise ValueError('references must contain inspected style and layout images')
    result = []
    for item in refs:
        if not isinstance(item, dict) or item.get('role') not in ('style', 'layout'):
            raise ValueError('reference role must be style or layout')
        role = item['role']
        if item.get('definition_id') != data.get(role):
            raise ValueError('reference definition_id does not match selected ' + role)
        path = Path(str(item.get('path', ''))).expanduser()
        if not path.is_absolute():
            path = ROOT / path
        path = path.resolve()
        if not path.is_file() or path.suffix.lower() not in ('.jpg','.jpeg','.png','.webp'):
            raise ValueError('reference image missing or unsupported: ' + str(path))
        if item.get('inspected') is not True:
            raise ValueError('host must inspect the actual reference before assembly')
        features = item.get('borrowed_features')
        if not isinstance(features, list) or not features or any(not isinstance(x,str) or not x.strip() for x in features):
            raise ValueError('reference needs concrete borrowed_features')
        result.append(dict(role=role, definition_id=item['definition_id'], path=str(path),
                           borrowed_features=features, inspection_claim='host-reported; not script-verified'))
    if {x['role'] for x in result} != {'style','layout'}:
        raise ValueError('both style and layout reference roles required')
    return {'mode':mode, 'references':result,
            'attachment_plan':result if mode=='direct' else [],
            'submission_status':'not_submitted',
            'note':'Attach through the actual image tool, record returned invocation/image identifiers. Paths are not image inputs.'}


def template(name, values):
    md = read('base-prompt-EN.md')
    match = re.search(r'<!-- TEMPLATE:' + re.escape(name) + r' -->\s*```text\n(.*?)\n```', md, re.S)
    if not match:
        raise ValueError('MD template missing: ' + name)
    def replace(m):
        key = m.group(1)
        if key not in values:
            raise ValueError('Unresolved template field: ' + key)
        return str(values[key])
    return re.sub(r'\{\{([a-z_]+)\}\}', replace, match.group(1))


def build(data):
    validate_preflight(data)
    def need(obj, key):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError('缺少具体字段：' + key)
        return value.strip()
    profile = resolve_profile(data)
    language = data.get('language','zh')
    theme = need(data, 'theme')
    canvas = need(data, 'canvas')
    ratio = re.search(r'(\d+(?:\.\d+)?)\s*[:：]\s*(\d+(?:\.\d+)?)', canvas)
    if not ratio or min(map(float, ratio.groups())) <= 0:
        raise ValueError('canvas 必须明确有效比例，如横版 16:9 或竖版 3:4')
    w,h = map(float, ratio.groups())
    orientation = '横版' if w>h else ('竖版' if h>w else '方形')
    if ('portrait' in canvas.lower() or '竖' in canvas) and w>h or ('landscape' in canvas.lower() or '横' in canvas) and h>w:
        raise ValueError('画幅方向与比例矛盾')
    refs = reference_plan(data)
    pool = candidate_pool(data, profile)
    layout = data.get('layout')
    if layout in MONTAGE_LAYOUTS:
        raise ValueError('布局属于全局排除的可见分格拼版')
    if profile != DEFAULT_PROFILE and layout == 'big-type-only':
        raise ValueError('small-type-refined-v1 档不接受 big-type-only 布局')
    if layout not in pool and not data.get('user_layout_override'):
        raise ValueError('布局不符合候选池或当前档位规则')
    definition('style', data.get('style')); definition('layout', data.get('layout'))
    design = data.get('design', {})
    for key in ('motif','theme_basis','subject','spatial_structure','title_relationship','light_material','information_region'):
        need(design,key)
    items = data.get('copy_items')
    if not isinstance(items,list) or not items:
        raise ValueError('需要完整准确文案')
    for item in items:
        for key in ('id','role','text','region'):need(item,key)
    if len({x['id'] for x in items}) != len(items):
        raise ValueError('文案 ID 重复')
    pairs = data.get('pairings',[7,1])
    if not isinstance(pairs,list) or not 1<=len(pairs)<=2:
        raise ValueError('需要一至两组配对')
    typography = '\n'.join(pairing(n) for n in pairs)
    mode = data.get('text_mode','integrated')
    stage = data.get('stage','generate')
    route = data.get('visual_route','general')
    if mode not in ('integrated','overlay','composite') or stage not in ('generate','edit') or route not in ('general','color_micro'):
        raise ValueError('无效文字模式、阶段或视觉路线')
    assets = data.get('assets',[])
    if not isinstance(assets,list):raise ValueError('assets 必须是数组')
    observations = '\n'.join(x['role']+'：'+'；'.join(x['borrowed_features']) for x in refs['references'])
    values = dict(theme=theme, canvas=canvas, orientation=orientation,
        motif=design['motif'], theme_basis=design['theme_basis'], subject=design['subject'],
        spatial_structure=design['spatial_structure'], material=design['light_material'],
        references=observations, cultural=data.get('cultural_context','仅概念性表达，不编造文化归属、展品或真实现场。'),
        typography=typography, title_relationship=design['title_relationship'], information_region=design['information_region'],
        copy='\n'.join(x['region']+'：'+x['text'] for x in items),
        assets=json.dumps(assets,ensure_ascii=False))
    if route=='color_micro':
        for key in ('main_color','micro_scene','action','cultural_elements'):values[key]=need(design,key)
    selected = None
    if stage=='edit':
        selected = Path(need(data,'selected_image')).expanduser().resolve()
        if not selected.is_file():raise ValueError('选中图片不存在')
        changes = data.get('changes')
        if not isinstance(changes,list) or not 1<=len(changes)<=3:raise ValueError('编辑需要一至三项修改')
        for c in changes:
            for key in ('location','action','expected'):need(c,key)
        values['changes']='\n'.join(c['location']+'：'+c['action']+'；预期：'+c['expected'] for c in changes)
        image = template('edit',values)
    else:image = template(route,values)
    image += '\n\n'+template('integrated' if mode=='integrated' else 'text_free',values)
    image += '\n\n参考转译：\n'+observations+'\n\n素材角色与操作：'+values['assets']
    image += '\n\n'+prompt_rules(profile, language)
    image += '\n\n'+people_directive(people_policy(data), language)
    negative = negative_rules(language)
    image += '\n\n避免：\n'+'\n'.join(negative)
    attachments = list(refs['attachment_plan'])
    if selected:attachments.insert(0,dict(role='edit_target',path=str(selected)))
    notes = dict(mode=mode,profile=profile,people_policy=people_policy(data),
                 typesetting_items=items,typography_visual_description=typography,
                 information_region=design['information_region'],assets=assets)
    if mode=='composite':
        notes['typography_layer_prompt']=template('type_layer',values)+'\n'+prompt_rules(profile, language)
        notes['compositor']='scripts/composite_text_layer.py'
    return dict(image_prompt=image,reference_plan=refs,image_input_plan=attachments,
                production_notes=notes,copy_manifest=items,candidate_pool=pool,
                rendering_policy=production_policy(profile),typography_profile=profile,
                orientation=orientation,language=language,negative_prompt=negative,
                review_note='组装与路径检查不证明看图、提交、生图质量或文化真实性。')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("brief",type=Path)
    p.add_argument("--candidates",action="store_true",help="Only return layout pool from reviewed categories")
    args=p.parse_args()
    try:
        data=json.loads(args.brief.read_text(encoding="utf-8-sig"))
        result={"candidate_pool":candidate_pool(data)} if args.candidates else build(data)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,FileNotFoundError,TypeError) as exc:
        p.exit(2,str(exc)+"\n")

if __name__ == "__main__":
    main()

