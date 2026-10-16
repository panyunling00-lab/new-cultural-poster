---
name: new-cultural-zh
description: 基于所提供内容与已核实的文化语境，创作文化展览、演出、非遗手工艺、工作坊与节庆海报，包含三个视觉方向、人工选择、迭代细化、分级质量审查与终版确认。不含普通商品广告。
---

# 文化活动海报生成器

本包用于创作文化展览、演出、非遗手工艺、工作坊与节庆海报，并保持文化通用性：不把任何测试案例、画幅或单一画风设为默认。

## 文件解析与参考资料阅读

所有路径都相对于包含本 SKILL.md 的目录解析，而非任务工作目录。参考文档使用同一根目录。目录名一律按所写保留：复数 `assets/`、小写 `references/style/` 与 `references/layout/`，以及 `base-prompt-EN.md` 的大小写。ID 即去掉 `.md` 的文件名，将其代入所示路径。完整阅读每个所选定义；切勿仅凭文件名推断，也不要无差别加载整个库。例如 `organic-craft` 需要 `references/style/organic-craft.md`，`editorial-column` 需要 `references/layout/editorial-column.md`。

| 阅读时机 | 路径 | 用途 |
|---|---|---|
| 步骤 1 之前 | `references/content-analysis-en.md` | 事实、完整文案、素材角色、层级、preflight 字段契约与创意转译简报 |
| 步骤 4 开始时 | `references/event-layout-map.md` | 先按内容处境路由到视觉关系，再确定具有约束力的分类版式池 |
| 步骤 4 开始时 | `references/selection-guide.md` | 分类候选池、决策树规则、画风谱系与参考图使用模式；其 R7 表被脚本解析 |
| 任何方向或生成之前 | `references/typography-constraints.md` | 档位总入口、切换表与 `design-free-v1` 规则 |
| 仅当当前档位为 `small-type-refined-v1` 时 | `references/typography-system.md` | 该档位的数值、配对与图文关系 |
| 选择字形手法时 | `references/typography-moves.md` | 可选字形手法菜单；档位中立，故 `small-type-refined-v1` 下任何冲突手法须服从该档位的上限 |
| 步骤 4 候选选择期间 | `references/style/<style_id>.md` | 字体排印、配色、材质、图像、限制 |
| 步骤 4 候选选择期间 | `references/layout/<layout_id>.md` | 构图、阅读顺序、文字位置、比例适配 |
| 步骤 4 候选选择期间 | `assets/style-references/previews/<style_id>-contact-sheet.jpg` | 每个画风一张视觉证据拼版图 |
| 步骤 4 和 5 的候选选择与提示词组装期间 | `assets/composition-references/<group>/<layout_id>/` | 所选版式的构图证据 |
| 步骤 3 和 6 之前 | `references/quality-rubric-en.md` | 文化核查、硬门槛、图像审查与评分 |
| 步骤 2 文字选风格时，以及步骤 4 和 5 撰写提示词之前 | `references/font-pairing-guide.md` | 8 组字形描述配对；无需字体文件 |
| 步骤 4 和 5 撰写提示词之前 | `references/base-prompt-EN.md` | 提示词组装；其 `<!-- TEMPLATE:... -->` 标记块由 `scripts/build_prompt.py` 读取 |
| 步骤 4 和 5 组装提示词之前 | `assets/negative-prompt.txt` | 全局禁令清单；每行 `<中文> \| <英文>`，按语言注入一次 |
| overlay 排版之前 | `references/text-layer-rendering.md` | `scripts/render_text_layers.py` 的输入契约与 `scripts/overlay_assets.py` 用法 |
| 制作 composite 文字之前 | `references/composite-text-layer.md` | 模型绘制文字层与本地 screen/multiply 混合规则 |
| 步骤 5 开始时、HG3 之后 | `references/design-refinement-en.md` | 针对性精修与对已批准方向的保持 |
| 首次使用 `scripts/check_poster.py` 之前 | `references/quality-script-usage.md` | 质检请求/报告契约与退出码 |
| 首次门控操作之前 | `references/human-gate-usage.md` | 门状态脚本动作参考 |
| 维护本 skill 时 | `references/test-learnings.md` | 可追溯测试证据；绝不自动当作规则注入 |
| 需要解析排版档位时 | `assets/typography-defaults.json` | 仅为指针：含 `default_profile` 与指向 `assets/typography-design-free.json` 和 `assets/typography-small-type.json` 的 `profiles` 映射 |
| 阅读画风参考时 | `assets/style-references/` | 38 个画风文件夹中的参考图，每个画风一张 `previews/<style_id>-contact-sheet.jpg`，以及 `index.md` 与 `index.csv` |
| 阅读构图参考时 | `assets/composition-references/` | 七个原则分组中的构图图，每个版式 ID 恰好一个文件夹 |
| 组装设计简报时 | `templates/prompt-brief-example.json` | `scripts/build_prompt.py` 的输入示例；含 `references` 数组与 `typography_profile` 字段 |
| 任何生成之前 | `scripts/preflight.py` | 材料、画幅与文案完整性校验；由 `build_prompt.py` 与 `human_gate.py` 调用 |
| 方向规划期间 | `scripts/decision_tree.py` | 基于简报的确定性版式候选路由 |
| 步骤 4 和 5 之前 | `scripts/build_prompt.py` | 组装图像提示词；解析 R7 表与 TEMPLATE 标记块 |
| 档位生效时 | `scripts/typography_policy.py` | 读取当前档位数值并输出其提示词约束块 |
| overlay 路径 | `scripts/render_text_layers.py` | 使用用户提供字体的实测 overlay 排版 |
| composite 路径 | `scripts/composite_text_layer.py` | 将模型绘制的文字层混合到底图上 |
| 提供原始素材时 | `scripts/overlay_assets.py` | 将所提供的 logo/二维码 PNG 合成到实际像素上 |
| 步骤 6–7 | `scripts/check_poster.py` | 解码实际像素并计算评分决策 |
| 每个门控步骤 | `scripts/human_gate.py` | 顺序门状态辅助工具 |
| 验证本 skill 时 | `scripts/test_typography.py` | 字号、渲染与质量门槛的回归检查 |
| 验证本 skill 时 | `scripts/test_design_free.py` | 自由设计、精确文案与人工门的回归检查 |

本包包含 38 个画风定义与 17 个版式定义。`neo-brutalist` 和 `full-bleed-image-overlay` 是有效 ID；`neo-brutalism` 和 `full-bleed` 并非真实定义。`cultural.txt` 是扁平的目录索引，不是流程指令。`scripts/test_typography.py` 与 `scripts/test_design_free.py` 仅用于验证，正常运行任务时绝不会被调用。

**参考图库是定义的一部分，而非装饰。** `assets/style-references/` 在 38 个画风文件夹中收录约 220 张参考图，每个画风一张拼版图，位于 `assets/style-references/previews/` 下，并有一个索引（`index.md`、`index.csv`）。`assets/composition-references/` 在七个原则分组（division、imagery、motion、space、structure、subject、typography）中收录约 79 张构图图；每个版式 ID 恰好对应一个文件夹，路径为 `assets/composition-references/<group>/<layout_id>/`。仅凭文字定义是不完整的规范：在提出方向之前，先看其图像；在生成之前，让图像约束配色、材质、质感与构图。它们仅是画风参考——切勿将其作为展品插入，其自身的字体排印也绝不能免除当前档位的约束。

## 排版档位（可插拔）

字体排印由档位驱动，可插拔。共有两个档位：`design-free-v1`（默认），数值在 `assets/typography-design-free.json`；以及 `small-type-refined-v1`，数值在 `assets/typography-small-type.json`。`assets/typography-defaults.json` 仅为指针：它含 `default_profile` 与指向这两个文件的 `profiles` 映射，脚本通过它解析当前档位。设计简报用 `brief.typography_profile` 选择档位；该字段缺失时适用默认的 `design-free-v1`。

切换档位只改变档位文件与配置，绝不改变 `references/style/*.md` 与 `references/layout/*.md` 下的 55 个文件：它们的头部统一引用 `references/typography-constraints.md`，该文件是唯一总入口，并承载下文的切换表。`references/typography-system.md` 仅在 `small-type-refined-v1` 下生效；`references/typography-moves.md` 是可选的字形手法菜单，主要在允许自由字形时使用，其余情形服从该档位的上限。

| 规则 | `design-free-v1` | `small-type-refined-v1` |
|---|---|---|
| 标题字号上限 | 无 | 标题 ≤ 0.055S；标题块目标 15% / 硬上限 20% |
| 文字块面积上限 | 无 | 文字块合计面积 ≤ 画布的 20% |
| 负空间下限 | 无 | ≥ 30% |
| 边缘安全边距 | 0（不要求） | ≥ 8% W/H |
| 避让间距 | 0（不要求） | 文字块间隙 ≥ 2%，核心主体避让 ≥ 短边的 4% |
| 几何校验 | 仅描述，不给判定 | 强制执行（pass/fail） |
| `big-type-only` | 仅经 `user_layout_override`（不属于任何类别池） | 不合格（作为遗留 ID 保留） |
| 最后两条负面提示规则 | 默认条件项 | 生效 |

`design-free-v1` 下只有两条硬性排印底线：每一项必需字符串都逐字正确，并在正常观看尺寸下保持可读；没有伪文字，也不编造事实。字号、字形、变形、叠压、错落、行距、字距与信息区位由 AI 依据主题、媒介、观看尺寸和内容判断；没有默认小字号，也没有默认克制。`small-type-refined-v1` 下，其文件中的每一项数值上限都被强制执行。无论哪个档位生效，都要检查实际像素——仅凭提示词措辞不构成合规。

## 全局构图规则（两档通用）

这些规则两个档位都成立，适用于每个 A/B/C 方向与后续全部细化。只有用户之后明确的指令才能解除其中一条；记录该指令的范围。

- 人物遵循简报解析出的人物策略（`scripts/build_prompt.py::people_policy`）：主题类别含演出（B）、节庆/嘉年华（E）或集市时，或用户参考素材仅含人物（`reference_people: "only-people"`）时，允许人物；参考素材同时含人物与其他内容（`reference_people: "people-plus-content"`）时，尽量不以人物作主体，仅在没有其他内容能承载主题时才使用人物；其余全部情况下不生成真人、插画人物、剪影、手部特写或微型人物场景，优先选用非人物器物、材料、工艺结构、自然形态与抽象关系。当所提供的素材必须展示且本身含人物时，不擅自篡改或删除，先说明冲突并取得明确决定。用户之后明确的指令随时可以解除或收紧本规则；记录其范围。
- 禁止可见分格的多图拼版（九宫格、卡片墙、侧边上下分格细节图、带分隔线的拼贴）。采用一个连续、完整的视觉空间，以大形、尺度、留白与前后关系组织。隐藏的对齐网格仍可使用，但不得画成可见格子。
- 因此 `modular-grid`、`split-horizontal`、`split-vertical` 永远不进候选池，框景（`frame-within-frame`）只允许单一连续窗口。剩余候选不足时，说明并调整类别适配，不暗中恢复禁用布局。
- 候选池在两个档位下都严格按类别映射（`references/selection-guide.md` R7）：每个类别贡献其 primary 与 secondary 版式，相关 specialism 再补充 specialist 版式。任何档位都不再向所有类别追加布局。`big-type-only` 不属于任何类别行，故 `design-free-v1` 下仅可经 `user_layout_override` 使用，`small-type-refined-v1` 下直接拒绝。`modular-grid`、`split-horizontal`、`split-vertical` 仍全局排除。38 个画风在两个档位下均可用。

## 核心要求与记录

字体排印使用 `references/font-pairing-guide.md` 中描述的 8 种视觉配对预设。本包不附带任何字体文件，其运作机制是语言而非文件：选择所描述字形特征与海报画风、配色、材质和文化语域相匹配的配对，再通过该描述——字形形状、笔画对比、字重、比例、字距——来表达它。切勿将字体族名称、文件名或路径写入图像提示词。因此 integrated 生成是默认的文本路径。当文案需要在不重生成底图的前提下修改，或多种语言版本共用同一张已批准底图时，使用经 `scripts/composite_text_layer.py` 的 composite 路径——同样不需要任何字体文件。仅当用户为该任务明确提供字体文件时，overlay 排版才可用；在渲染请求的 `supplied_fonts` 中注册这些文件（没有系统字体回退），并在渲染前核实字形覆盖情况。不要安装、下载或私自打包字体来启用 overlay。

- 保留每一项必需的展示项与事实。不编造活动细节、文化归属、翻译、背书或遗产身份，也不为视觉简洁而删减内容。当任务明确授权压缩母本文案句式时，可以缩短所提供句子——但绝不丢弃必需的名称、头衔、官方定名、日期、场地、开放时间或入场条款；记录每次压缩并确认含义未变。
- 任务提供的官方定名是硬性要求。诸如非物质文化遗产名录条目之类的名称，必须在要求其出现的语言版本中逐字逐字地出现，并附上其在另一版本中提供的对应表述。绝不对定名进行意译、独立翻译或缩短；在质量审查步骤（步骤 6）通过之前，逐字符核实这些字符串。
- 所提供的摄影素材可以作为视觉基底，而不仅是参考。当设计简报提供可用摄影时，优先采用以一到三张所提供照片为输入的图生图生成，或直接合成这些照片，使真实手工艺品以其本来面目呈现。当某张所提供照片经二次裁剪后即能成立构图时，就裁切并直接使用原图，而不是生成一张底图，并记录这次裁剪。
- 诸如标志和标记之类的矢量素材对保真度敏感。将所提供的 SVG 按交付分辨率栅格化，核实结果非空且背景透明，再按计划位置原样合成；绝不让图像模型重绘、改风格或近似标志。所提供的 PNG/JPG 标记已是栅格图：以同样方式合成，绝不重新生成。
- 区分必需的展示素材与仅作画风参考的素材。未经授权，不要把画风参考作为展品插入；在 HG1 澄清含糊的角色。
- 默认在对话上下文中维护设计简报、编号素材清单、版本、核实证据和用户决定。不要为每个任务都要求 analysis.md、material-inventory.md、human-gates.md 或其他流程文件。
- 将参考模块的 schema 用作组织指引；仅在要求时或跨会话恢复需要时保存任务记录，并将其视为记录而非额外的 skill 模块。
- 当前明确的用户指令优先。笼统的"直接做"请求不会取消已约定的人工门；记录任何明确授权或豁免的范围。
- 审查实际完成图像。提示词质量、无文字背景和高模型评分都不能确立终版海报就绪。

## 人工门与任务状态

使用 `scripts/human_gate.py` 作为任务的顺序门状态辅助工具，并在首次使用前阅读 `references/human-gate-usage.md`。其动作集合为 `init`、`status`、`brief`、`directions`、`select`、`poster`、`review`、`confirm_final`（`approve` 是遗留别名）、`feedback`、`check` 与 `exported`。本工作流有三次人工门加一次终版确认：HG1（确认文字）、HG2（文字选风格）、HG3（三选一·构图+低保真）与 `confirm_final`。没有独立的导出审批门——终版确认本身即导出授权，而 `review` 记录的 `pass` 才首次允许它。

将门状态 JSON 保存在任务输出目录（运行期文件 hg-state.json）；它是门恢复所需的唯一流程记录，并非要求创建每一份分析产物。每个语言版本运行一个独立状态文件，使批准绝不跨版本泄漏。在方向登记、海报完成与导出之前，运行相应的 `check` 动作，失败时停止；该辅助工具检查状态与图像版本，不检查对话真实性或视觉质量。

在每个人工门，展示决策所需的信息或实际图像，标明当前版本，用用户的语言提出一个明确问题，然后结束回合以等待。工具返回、沉默、经过的时间、预选选项、模型建议与先前的批准都不构成用户回复。针对当前单个问题解读是/否，针对当前已登记集合解读 A/B/C；清晰的自然语言有效，无需固定口令，而含糊回答会使门保持待决。仅在回复真正到达后才逐字记录，绝不伪造批准证据。三个人工门每次都结束回合等待真实回复，HG1/HG2 不生成图片（0 张），HG3 恰好三张低保真草案。

## 工作流

### 1. 分析材料与人工门 HG1（确认文字，0 张图）

阅读 `references/content-analysis-en.md`。整理主题、标题、完整文案、时间、场地、主办方、参与信息、预期用途、语言、比例、尺寸与素材，并将每一项标记为明确、推断、遗漏或冲突。逐字保留所提供文本与素材；不要猜测无法辨认的附件文本。随后产出单独标注的创意转译简报（分析输出的第 11 节）：九个 Inferred 创意槽位外加构成方法、空间层级、材料质感与点睛色提案，人物槽遵循解析出的人物策略；事实与创意转译保持分离。

记录 `scripts/preflight.py` 校验的字段——`source_audit`（每份文档的 `path`、`pages`、`read_pages`，以及 `unresolved`）、`canvas_spec`、`source_copy` 与 `copy_items`——并在调用 `scripts/build_prompt.py` 或 `brief`/`check`/`directions` 动作之前完成 `preflight.validate`。缺文案、缺页、未知画幅或比例冲突一律阻止生成。

用 `init` 动作初始化任务。分析后向用户展示提取出的完整文案（标题、官方定名、时间、场地、主办方、参与信息等），标明遗漏、冲突与待核实项，请用户确认或更正，然后结束回合等待真实回复；HG1 不生成图片。仅在收到真实回复并按回复更新简报、完成上述 preflight 校验后，运行 `brief`，将 `theme_status` 按回复后的实际状态填写为 `clear`、`missing`、`unclear` 或 `conflict`。标题、时间、场地及其他缺失事实保持缺失，绝不为通过 HG1 而编造。

### 2. 人工门 HG2（文字选风格，0 张图）

仅在 HG1 获得真实确认后，在生成任何图片之前，基于已确认文案，阅读 `references/font-pairing-guide.md` 的 8 组字形配对与 `references/typography-moves.md` 的手法，遵循当前排版档位，给出 2–4 个明确的文字风格方向。每项描述字重、字形、字距、排印手法与适配理由，请用户选定其一或给出偏好，然后结束回合等待真实回复；不生成图片。含糊或无回复保持 HG2 待决，绝不代选。将用户选定的文字风格与逐字回复记入对话上下文中的简报，供步骤 4 和 5 使用；不新增脚本 action。

### 3. 核查文化含义与用途

阅读 `references/quality-rubric-en.md` 的文化章节。核查每个重要元素的含义、归属、地域、年代、宗教或仪式语境与拟用方式，并记录实际来源。检查组合、裁切与变形。将任何无法核实的新装饰元素替换为有依据的主题相关表达，并核实替换项。对用户素材或核心主题的更改需要确认，必要的未解决文化问题会中止受影响的方向。

### 4. 规划三个构图方向并生成三张低保真草案，人工门 HG3（三选一·构图+低保真，恰好 3 张）

仅在 HG2 获得真实选择并完成步骤 3 后，保持已确认文字风格，按以下顺序规划 A/B/C；新增文化元素仍须按步骤 3 核查后使用：

1. 打开 `references/event-layout-map.md` 的 §2，回答它的四个问题以确定视觉关系，再从 §6–§7 取得具有约束力的分类版式池。路由各节只收窄搜索范围；由 §7 与 `references/selection-guide.md` 决定。§7 仅为阅读副本——机器读取源是 `references/selection-guide.md` 中的 R7 表。
2. 完整阅读 `references/selection-guide.md`，并对已分析的简报运行 `scripts/decision_tree.py`；在继续前解决 `needs_analysis`、`conflict` 与 `needs_adjustment`。
3. 列出 `references/style/` 与 `references/layout/` 中的实际文件，从真实文件名词干中为 A/B/C 选择 ID。
4. 完整阅读每个所选画风与版式定义；不要从名称推断内容。
5. 查看每个候选方向的图像：拼版图 `assets/style-references/previews/<style_id>-contact-sheet.jpg` 与版式构图图 `assets/composition-references/<group>/<layout_id>/`。若定义与图像不一致，配色、材质与图形语言以图像为准，字体排印以当前档位为准。
6. 按方向记录 `references` 数组（`path`、`role`、`definition_id`、`inspected`、`borrowed_features`）、`fit_evidence`、`reference_mode`（`direct` 或 `features`）、`typography_profile`，以及标题区、角色字号比例、安全区与图层分离。

A/B/C 必须是三个不同 `style_id` 与三个不同 `layout_id`，取自全局排除之后的候选池。至少在两个视觉维度上区分它们，并将标题与信息放置在由各自所选版式 Text Placement 章节定义的三个空间上不同的区域；仅改变颜色不算一个方向。版式池与比例无关：画幅比例改变版式的实现方式，而非哪些版式合格。当用户固定版式或画风时，仍要通过其他空间与视觉关系独立设计三个方向。

阅读 `references/typography-moves.md`（`design-free-v1` 下可用）、`references/font-pairing-guide.md` 与 `references/base-prompt-EN.md`。用 `scripts/build_prompt.py` 组装每个提示词，它会注入 `scripts/typography_policy.py` 给出的当前档位块，以及 `assets/negative-prompt.txt` 中一种语言的一半禁令。将已确认的画幅原样放入简报的 `canvas` 字段（例如 `landscape 16:9`），绝不依赖内置默认值。只要工具接受参考图像，就让每次生成以所选参考图像为依据；否则在文字提示词中具体命名所借用的元素。

生成恰好三张独立的低保真构图草案 A/B/C，每个方向单独一次生成调用，完整呈现构图、空间层级、色彩与风格基调，关键官方定名、标题等硬性字符串逐字正确；大段次要文案可以占位示意。低保真仅指本阶段的细节与次要文案完成度，不改变生图质量、画质要求、排版档位或提示词组装逻辑。绝不用拼版图、三联画或三分格图替代。

比率硬门——每次生成后，打开实际文件读取其像素宽高；不要相信所请求的尺寸或渲染器标签。实际比例必须严格等于简报的画幅比例：把目标约简为整数 `p:q`，要求 `width * q == height * p`，零容差。若不等，则居中裁剪到最大精确比例矩形 `k = min(width // p, height // q)`，裁剪尺寸 `k*p` × `k*q`，若 `k < 1` 就停止。保存为新版本，重新打开并复核像素比例以及必需文案与主体的覆盖。绝不用加黑边、留白条、纯色条或贴到大画布上来达成比例；裁剪掉必需内容的版本不算通过。检查四条边是否满版——仅比例相符不能豁免空白带或边框。

原始资产保真——当用户提供 logo 或二维码 PNG 时，先生成满版画面，再用 `scripts/overlay_assets.py` 把所提供文件合成到实际像素上，且不改动原图。对于所提供的 SVG，先忠实栅格化为透明 PNG，并核实其非空。把身份资产、位置要求与所有占位措辞——logo、徽章、印章、二维码、占位框、预留位、右上角标记——都排除在图像提示词与负面提示之外。未提供 logo 文件时，整轮都不提及 logo，也绝不编造。裸底图不算候选：先完成本阶段要求的文案与素材合成再登记；次要文案占位的许可不适用于身份资产。

用 `directions` 动作登记这三张实际低保真草案文件。它们等待选择，而非已批准交付物；preview 等历史名称原样沿用。

展示三张实际 A/B/C 低保真草案、显著视觉差异与当前候选 `version`，请用户选择 A/B/C 或带具体反馈请求新集合，然后结束回合等待。仅在真实回复后，以当前候选 `version` 与逐字回复运行 `select`；选择记入简报，进入步骤 5。

- 全部拒绝、回答“否”或请求新方向：使用带 `new_directions` 的 `feedback`，返回本步骤重新规划、生成并登记三张草案，再次经过 HG3。
- 选定方向并附局部反馈：记录选择与反馈，在步骤 5 中沿选定草案完成。
- 仅答“是”、含糊或无回复：保持 HG3 待决；绝不替用户静默选择。

### 5. 高保真终版（1 张）

阅读 `references/design-refinement-en.md`，保持 HG3 已批准方向。在选中的实际低保真草案基础上，以步骤 4 的同一提示词管线（`scripts/build_prompt.py`、当前档位块、负面提示与已确认画幅原样）产出唯一一张高保真终版，补全全部必需的逐字文案、细节与素材合成。保持已批准构图、主体、画风、配色、视角、空间关系、信息位置与 HG2 文字风格方向，应用步骤 4 的比率硬门与原始资产保真规则；生图质量与画质要求保持不变。

在真实所选图像上编辑或合成——包括 composite 路径上的 `scripts/composite_text_layer.py` 与 overlay 路径上的 `scripts/render_text_layers.py`——绝不从文字重新生成相似替代品。局部修正包括错字或缺字、伪文字、偶发缺陷、必需文案补全与必要的可读性修正。

用 `poster` 动作登记完成图像，将其关联到所选预览 `version`，`production_mode` 按实际路径填写为 `edit` 或 `composite`。一次局部修改是所选候选的一个版本，而不是额外方向；重大构图或画风更改返回步骤 4，重新做三张并再次经过 HG3。未提出修改也必须完成高保真制作与步骤 6 质检，才能进入步骤 7。

### 6. 质检（≤2 次修正）

先阅读 `references/quality-script-usage.md` 与 `references/quality-rubric-en.md`，对实际像素运行 `scripts/check_poster.py`。在检查实际像素后，提交当前图像哈希、阶段、H1–H8 证据、按 `references/typography-constraints.md` 当前档位下的当前图像 `typography` 测量值、各维度分数，以及仅限已确认的输出规格。缺少解码能力或证据不算通过。核实报告哈希与已登记海报哈希匹配，然后把报告的 `decision` 与路径交给 `review` 动作。

完整阅读 `references/quality-rubric-en.md`。对第一张完整海报做完整质检并建立基线；对之后每次局部修改只检查实际改动区域及受影响内容。检查逐项覆盖、文化证据、逐字符精确文本（含每一项官方定名）、结构、层级、可读性与实际文件属性，并将任何未核实项标记为未知。只有已记录的通过才继续。

每轮针对对决策影响最大的缺陷修正一次，并重新运行像素质检、提交 `review`。整个质检阶段累计最多两轮修正，不能通过更换版本重置计数；两轮后仍未通过则停下说明并请用户决定，不降标通过。局部缺陷返回步骤 5，文化问题返回步骤 3，不合适的理念返回步骤 4 并再次经过 HG3。绝不降低标准以强求通过，也绝不让内容完整性本身成为高美学评分的理由。

### 7. 终版确认

展示实际的完整版本及其已核实尺寸与格式，并询问它是否为终版。仅在真实确认当前 `version` 后运行 `confirm_final`，提供 `confirm` = true 与逐字回复。终版确认即导出授权；没有独立的导出审批门，方向选择也不等于确认。

- 已确认：继续到步骤 8。
- 局部更改：使用带 `local_revision` 的 `feedback`，返回步骤 5，并在再次询问前重跑分级审查。
- 换方向：使用带 `new_directions` 的 `feedback`，返回步骤 4，并再次经过 HG3。
- 含糊或无回复：保持待决；绝不自动确认。

### 8. 原样交付

交付前立即运行目标为 `export` 的 `check`，随后用 `exported` 登记任何字节相同的副本。交付已确认的原文件，或字节相同的副本：确认之后不再生成、润色、改字、裁剪、调色或转换格式。可见的更改会使确认失效，并返回分级审查与一次新的确认。交付实际链接、已核实规格与质量结论；保留已批准版本，绝不声称未核实的印刷就绪。

## 机器契约

以下接口是最终组装最容易被改坏的地方；只有在同时修改读取它们的代码时才能变更。

- `references/selection-guide.md` 的 R7 —— Category-to-Layout Mapping 表由 `scripts/build_prompt.py::mapping()` 逐行解析：每行按 `|` 切成恰好六段，第 2 段是单个 A–H 字母，每个布局 ID 必须带反引号，且必须恰好八行。不要为对齐本文档其他表格而重排它；增加一列、删除一个类别行或去掉反引号都会使 `mapping()` 失败或静默丢行。
- `references/base-prompt-EN.md` —— 其 `<!-- TEMPLATE:... -->` 标记块由 `scripts/build_prompt.py` 读取。不要重命名标记或删除块，并保留每个块内的 `{{字段}}` 名。
- `assets/negative-prompt.txt` —— 每个非注释行都是 `<中文> \| <英文>`；脚本按第一个 `|` 切分，并依据简报的 `language` 恰好追加其中一种语言的一半。规则内不得出现第二个 `|`，任何一侧都不得为空。
- `scripts/preflight.py` —— 规范字段名 `source_audit`（含 `complete`、`documents`、`unresolved`）、`canvas_spec`（含 `ratio`、`source`、`verbatim`）、`source_copy` 与 `copy_items` 被直接校验。不要重命名它们。
- 遗留兼容 —— `approve` 仅作为 `confirm_final` 的别名被接受，`awaiting_export_approval` / `export_allowed` 是遗留状态名，并非存在额外审批门的证据。

## 语言版本与孪生包约定

多版本交付 —— 一个任务可能要求同一视觉系统以多种语言版本呈现。HG3 所选的方向是共享的视觉资产：主体、构图、配色、材质处理与信息区排布在各版本间保持完全一致。

- 每个语言版本运行一个独立门状态任务（单独的状态文件），各自关联到同一所选方向版本，使批准绝不跨版本泄漏。
- 每个版本根据该语言所提供的母本重建文案清单。绝不要自行翻译文案：逐字使用所提供的措辞；若某版本没有提供的母本，则询问，而非自行生成一份。
- 字体排印在每个版本中遵循相同档位，在该版本自身的画布上测量。必需的定名必须在要求其出现的语言中逐字出现——例如中文版本中的官方遗产名录名称，以及英文版本中所提供的英文对应表述。
- 每个版本独立通过步骤 5–8；批准一个版本绝不批准另一个。

本项目的孪生包约定 —— 英文包与中文孪生包必须保持对齐：

- `scripts/` 与 `assets/` 在两个包中逐字节一致。
- `references/style/*.md` 与 `references/layout/*.md` 是语言中立的 ID 库：两包逐字节一致，且不翻译。
- `SKILL.md` 以及 `references/` 下其余人读文档逐行翻译，两包结构一一对应：英文包为英文，中文包为中文。
- `cultural.txt` 是文件清单而非翻译文本，在两包中逐字节一致。
