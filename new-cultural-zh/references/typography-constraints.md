# 排版档位总入口与 design-free-v1 规则

本文件是排版规则的唯一入口。`references/style/*.md` 与 `references/layout/*.md` 的头部一律引用本文件；换档位只改本文件与配置，不改那 55 个定义文件。

## 两个档位与切换方式

| 档位 id | 数值文件 | 说明 |
|---|---|---|
| `design-free-v1` | `assets/typography-design-free.json` | 默认档。边距/间距填 0，不产生 fail。 |
| `small-type-refined-v1` | `assets/typography-small-type.json` | 16 个数值上限；几何校验按判定执行。 |

默认档为 `design-free-v1`。设计简报通过 `brief.typography_profile` 选择档位。`assets/typography-defaults.json` 是脚本读取的默认指向（默认落到 `design-free-v1`），它只保存基础渲染器的可调起始值，不是设计上限。`scripts/typography_policy.py` 按当前档位从对应的数值文件读取数值。

档位切换后随之切换的规则：

| 随之切换 | `design-free-v1` | `small-type-refined-v1` |
|---|---|---|
| 字号上限 | 无 | 标题 ≤ 0.055S；标题块目标 15%／硬上限 20% |
| 面积上限 | 无 | 文字块合计 ≤ 20% 画布 |
| 留白下限 | 无 | ≥ 30% |
| 边距 | 0（不要求） | ≥ 8% W/H |
| 避让间距 | 0（不要求） | 文字块间距 ≥ 2%、主体避让 ≥ 4% 短边 |
| 几何校验 | 仅描述，不做判定 | 判定（pass/fail） |
| `big-type-only` | 仅经 `user_layout_override`（不属于任何类别池） | 不合格 |
| 负面提示规则 | 人物一条按主题/参考素材条件化（`people_policy`）；分格拼版一条无条件 | 相同（不随档位变化） |

档位专属文件：`references/typography-system.md` 只在 `small-type-refined-v1` 下生效；`references/typography-moves.md` 是可勾选的手法菜单，档位中立。

## design-free-v1 规则

字号、字形、变形、叠压、错落、行距、字距、信息区位置由 AI 按主题、媒介、观看尺寸与内容判断。没有默认小字、默认纸感、默认人物、默认素雅。当前类别候选池内的版式均可使用；`big-type-only` 仅可经明确的 `user_layout_override` 使用，三个分格拼版布局保持排除；历史预览中的数字不是当前硬规则。

仅有两条排版硬底线：
1. 所有必需文字（标题、日期、地点、主办方、注意事项等）逐字正确，在正常观看尺寸下清晰可辨。效果不能改变字义、字符顺序或事实；缺失信息保持缺失。
2. 不出现伪文字、乱码，不编造名称、日期、地点、机构、文化归属、奖项或引语。以 copy_items 原文为准，逐项核对。

满版画面上叠字是允许的、鼓励的构图方式之一；文字被前景局部遮挡是允许的，只要仍可辨认。字与主体叠压、色块穿插、跨层、沿路径或竖排都可选择。必需笔画与文字不得因遮挡、裁切、变形或低对比而无法识别；可裁切装饰性延伸或重复的非信息形态，不能截掉唯一必需文字。图文重叠不是自动失败。

字是设计材料。读 references/typography-moves.md，按主题选 0–2 个手法，不堆砌。标题可以是一级视觉对象，功能信息按真实阅读需求设置，既不强制缩小也不跟随标题无限放大。正常观看尺寸、对比、逐字核验是判断依据，不是字体大小比例或留白面积。

## 渲染与评审

assets/typography-defaults.json 仅保存基础渲染器的可调起始值，不是设计 caps。scripts/render_text_layers.py 是基础横竖排工具，不自动实现扭曲、飞白、沿路径或前景遮罩；需要这些效果时用 integrated 生成、编辑或适当的图层合成，不把基础工具限制误当设计限制。

在当前图像 visual_review.typography 中记录 profile_id=design-free-v1、evidence、intended_size_readable、exact_copy_verified、no_pseudo_text、facts_preserved。每项布尔判断必须来自当前图像、copy_items 及事实清单；缺证据为 unknown，已证实错误为 fail。items 可选，仅记录有效 bbox/字号/方向等测量，不据比例否决设计。key_visual 仅核对已出现的文字，不能冒充完整海报。旧记录仍可保留，须对当前版本按新规范重新评审。
