"""生成前的材料、画幅与文案完整性检查。不能自动证明提取忠实。"""
import re

def validate(brief):
    def require(ok, msg):
        if not ok: raise ValueError(msg)
    require(isinstance(brief,dict), '缺少分析后的 brief')
    source=brief.get('source_audit',{})
    require(source.get('complete') is True, '任务书和全部材料尚未完成逐页识别')
    docs=source.get('documents')
    require(isinstance(docs,list) and bool(docs), '缺少已读取材料清单')
    for d in docs:
        require(isinstance(d,dict) and d.get('path') and type(d.get('pages')) is int and d['pages']>0 and d.get('read_pages')==list(range(1,d['pages']+1)), '文档必须记录全部已读取页码')
    require(not source.get('unresolved'), '存在未识别、冲突或未读内容，不得生图')
    spec=brief.get('canvas_spec',{})
    require(spec.get('source') and spec.get('verbatim'), '缺少画幅原文和来源')
    ratio=spec.get('ratio','')
    require(isinstance(ratio,str) and re.fullmatch(r'[1-9][0-9]*:[1-9][0-9]*',ratio), '缺少有效画幅比例')
    actual=re.search(r'(\d+)\s*[:：]\s*(\d+)',str(brief.get('canvas','')))
    require(actual and tuple(map(int,actual.groups()))==tuple(map(int,ratio.split(':'))), 'canvas 与任务画幅不一致')
    manifest=brief.get('source_copy')
    require(isinstance(manifest,list) and bool(manifest), '缺少全部原文清单 source_copy')
    ids=set(); expected={}
    for item in manifest:
        require(isinstance(item,dict) and all(isinstance(item.get(k),str) and item[k].strip() for k in ('id','text','source')), '每段原文必须有编号、准确文字及来源')
        require(item['id'] not in ids, '原文编号重复');ids.add(item['id'])
        require(type(item.get('required')) is bool, '每段原文须明确是否必需')
        if item['required']:expected[item['id']]=item['text']
        else:require(item.get('omission_reason'), '未展示原文必须说明依据，不能直接丢弃')
    displayed=brief.get('copy_items',[])
    require(isinstance(displayed,list), 'copy_items 必须为数组')
    got={x.get('id'):x.get('text') for x in displayed}
    require(len(got)==len(displayed),'显示文案编号重复')
    require(all(got.get(k)==v for k,v in expected.items()), '必需原文遗漏或被改写')
    require(all(x in ids for x in got), '出现无原文来源的新增文案')
    return tuple(map(int,ratio.split(':')))
