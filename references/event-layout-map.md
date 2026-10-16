# 文化活动分类、版式与构图路由图

在步骤 3 开始时阅读。本文件按顺序承担两件事：先把一份凌乱的简报路由到一个视觉关系，再给出该活动分类具有约束力的版式候选池。依据活动的实际目的与内容分类，而非泛泛的文化标签。路径从 Skill 根目录解析。

## 1. 效力边界与阅读顺序

- **§2–§5 做路由。** 它们回答「这张海报该由什么关系来承载？」，并给出一小组候选。它们只做收窄，不做决定。
- **§7 是版式的权威。** 它的分类候选池具有约束力。路由各节给出的每个版式都必须与该候选池、以及 `references/selection-guide.md` 中的全局构图排除项求交集：池里没有的，以池为准，路由给出的值此时只作为**关系**方向的提示。§7 是给读者阅读的人读副本；真正的机器数据源是 `references/selection-guide.md` 的 R7，由 `scripts/build_prompt.py` 解析。
- **`references/selection-guide.md` §3–§4 负责筛选。** 路由各节不替代关系分支、画风定义与对真实参考图的查看。分类 D 的信息重要度仍然不构成放大正文字号的授权。
- 先读 §2。一节一用途；新的实测证据写进 `references/test-learnings.md`，不要堆在这里。

## 2. 四个问题

按此顺序作答。Q1 与 Q4 起决定作用。

| # | 问题 | 分支 |
|---|---|---|
| Q1 | 核心是**一个东西**、**多个并列的东西**，还是**东西之间的关系**？ | 一个 → 第 1、14、10 行 · 多个 → 第 3、12 行 · 关系 → 第 6、7、8、13 行 |
| Q2 | 内容是**静态**还是**在运动中**？ | 静态 → 静穆／结构／档案系各行 · 运动 → 第 4、9、15 行 |
| Q3 | 需要出现的**必需文案**有多少？ | 少 → 以留白为主的行（10、1） · 多 → 栏式与网格行（5、3、12） |
| Q4 | 这是一次**安静的馆藏式阅读**，还是一场**现场性／表达性活动**？ | 安静 → 簇 1–5 · 表达 → 允许簇 6–7 |

Q4 是许可门槛，不是偏好。按 `references/selection-guide.md` §4 的风格光谱，高能与实验簇仅在用户明确要求，或活动确实属于音乐节、潮流文化、实验艺术、现场演出时可用。面向展览、博物馆与非遗类活动，A/B/C 中至少有一个方向仍须以留白与克制的用色为主线。

## 3. 内容处境 → 构图

| 内容处境 | 承载它的视觉关系 | 版式候选 | 起始气质簇 |
|---|---|---|---|
| 一件作品、一件文物或一个物件就是全部重点 | 单一主体，孤立且完整可辨 | `centered-hero`、`off-center-hero` | 1 静穆馆藏、5 影像造物 |
| 手艺人的手、材质与制作过程就是重点 | 材质分层与制作痕迹 | `layered-depth`、`frame-within-frame` | 3 手作材质 |
| 多件并列作品、多场次、多节目 | 众多平等单元，按统一秩序排列 | `modular-grid` | 2 编辑档案 |
| 演出、节奏，或一条时间上的节目线 | 方向、流动、汇聚 | `diagonal-dynamic`、`radial-composition` | 6 高能现场 |
| 连续论述：策展文字、讲座、研究 | 一条连续的阅读栏 | `editorial-column`、`split-vertical` | 2 编辑档案 |
| 两个时代、两种视角，或一个场景加它的细部 | 分割与对照 | `split-horizontal`、`split-vertical` | 2 编辑档案 |
| 一个场所、结构、系统或路线 | 空间关系与投影 | `axonometric-spatial`、`large-geometry` | 4 结构几何 |
| 一种转化：折叠、展开、变成他物 | 改变状态的连续平面 | `folded-space`、`layered-depth` | 3 手作材质、7 概念实验 |
| 观众应走进场景之中，文字覆于其上阅读 | 满幅图像加安静的叠加区 | `full-bleed-image-overlay`（保留符合当前排版档位的安静低细节区） | 5 影像造物 |
| 几乎没给素材，只有一种符号或一个沉默的想法 | 由留白与象征完成表达 | `minimal-white-space`、`large-geometry` | 1 静穆馆藏 |
| 一次刻意的非线性、反秩序宣言 | 有意图的失序 | `disorder-layout` | 7 概念实验 |
| 节庆：多个节目、集体参与 | 多元与聚集 | `modular-grid` 加 `radial-composition` 或 `diagonal-dynamic` | 6 高能现场 |
| 透过窗户、展柜、镜头或边界去看 | 被框住的观看 | `frame-within-frame` | 5 影像造物、1 静穆馆藏 |
| 字形本身就是概念 | 字体作为图像，而非作为标题 | `large-geometry`、`off-center-hero`，配排印型画风 | 4 结构几何、6 高能现场 |

最后一行注意：字体作品是所提供的或绘制的**主体**，因此活动文案遵循当前排版档位。`big-type-only` 依然不合格。

纵深优先：面向展览、演出与空间类活动，优先采用上表中的 depth 型各行。A/B/C 除信息区位置外，还必须区别前景／中景／背景、遮挡与穿插、光与介质，或材料厚度，并且不能以颜色变化代替纵深差异。

## 4. 气质簇

作为画风命名空间的起点，覆盖全部 38 个定义。最终主画风仍须按 `references/selection-guide.md` §4 的风格光谱，通过阅读定义并查看其参考图来确定。

| # | 气质簇 | 画风 ID |
|---|---|---|
| 1 | 静穆馆藏 | `japanese-ma`、`swiss-editorial`、`luxury-minimal`、`japanese-modernism` |
| 2 | 编辑档案 | `cultural-editorial`、`image-led-editorial`、`editorial-collage`、`data-editorial`、`monochrome-typographic` |
| 3 | 手作材质 | `organic-craft`、`botanical-premium`、`screenprint`、`risograph-zine`、`xerox-punk`、`print-error` |
| 4 | 结构几何 | `bauhaus-modular`、`constructivist-impact`、`minimal-graphic` |
| 5 | 影像造物 | `cinematic-key-art`、`hyperreal-product`、`art-deco-luxe` |
| 6 | 高能现场 | `futurist-gradient`、`pop-commercial`、`glitch-art`、`kinetic-typography`、`liquid-visual`、`distorted-type`、`emo-visual`、`y2k`、`neo-brutalist`、`retro-futurism` |
| 7 | 概念实验 | `surreal-3d-editorial`、`digital-experimental-type`、`glassmorphism-ui`、`webcore`、`pixel-art`、`dreamcore-softcore`、`contemporary-art` |

这些气质簇是灵感导航，不是准入条件；请为 A/B/C 保留克制与冲击两类画风，不要仅因某画风不在起始簇内就将其排除。

## 5. 打破平局

两行都合适时，依次比较：

1. 哪个版式能让必需文案在配置的最低可读字号下放得下，而无需缩小字号。
2. 哪个版式有真实且已查看过的参考图可用——见 `references/selection-guide.md` §5。
3. 哪个能给 A/B/C 三个在空间上不同的标题／信息区。文字区都挤在同一处的版式，做不出三个方向。
4. 哪个对事实、主体或投放渠道的未证实假设更少。

不要：因为主题「看起来很文化」就默认 `centered-hero` 或 `editorial-column`；把路由各节当成逐项打勾的清单；或用它们覆盖用户明确指定的版式。

## 6. 活动分类

| ID | 分类 | 典型活动 | 视觉核心 |
|---|---|---|---|
| A | 静态视觉艺术展览 | 书法、绘画、摄影、雕塑、插画、设计展 | 以原作作为主体；编辑式与策展式呈现 |
| B | 表演与动态艺术 | 音乐会、戏剧、舞蹈、传统戏曲、音乐节、现场演出 | 动势、节奏与舞台张力 |
| C | 遗产与传统工艺 | 剪纸、陶瓷、编织与刺绣、木雕、漆器、手工艺市集 | 材质、手工层次与温度 |
| D | 知识与学术活动 | 讲座、论坛、读书会、研讨会、工作坊、签售 | 信息密度、秩序与文字 |
| E | 节庆与多元文化 | 民俗节、文化节、美食节、电影节、嘉年华 | 多样性、人群与参与感 |
| F | 当代与实验艺术 | 新媒体展、装置、行为艺术、先锋设计、实验数字艺术 | 观念、非常规关系与实验性 |
| G | 博物馆与收藏展 | 历史文物、考古展、善本、馆藏重点、博物馆镇馆之宝展 | 文物主体、权威感与历史纵深 |
| H | 空间与建筑文化 | 建筑展、园林、城市更新、公共艺术、城市遗产漫步 | 空间关系与结构 |

## 7. 分类到版式的映射

> **人读副本，不是数据源。** 下表是给读者阅读的人读镜像。它**不是**脚本数据源：具有权威性的机器读取表是 `references/selection-guide.md` 的 R7，由 `scripts/build_prompt.py` 解析。请保持本副本与 R7 逐字符一致；两者一旦不同，以 R7 为准，并须修正本副本。

| 分类 | 主要版式 | 次要版式 | 理由与专项补充 |
|---|---|---|---|
| A | `editorial-column`, `off-center-hero` | `minimal-white-space`, `frame-within-frame` | 将原作与策展文案并置呈现。对于书法或篆刻，另可纳入 `diagonal-dynamic` 以表现笔画动势，同时原作字迹仍作为已提供图像的主体，活动文案遵循当前排版档位。 |
| B | `diagonal-dynamic`, `radial-composition` | `layered-depth`, `full-bleed-image-overlay` | 以舞台式聚焦表达动势与节奏。 |
| C | `layered-depth`, `frame-within-frame` | `editorial-column`, `minimal-white-space` | 将分层材质与物件呈现相结合。对于市集，另可纳入 `modular-grid`。 |
| D | `editorial-column`, `modular-grid` | `minimal-white-space`, `split-vertical` | 建立阅读路径与醒目的讲座主题。 |
| E | `modular-grid`, `radial-composition` | `diagonal-dynamic`, `full-bleed-image-overlay` | 组织多项活动与集体庆祝氛围。 |
| F | `disorder-layout`, `large-geometry` | `off-center-hero`, `folded-space` | 支撑实验性解构与几何观念。 |
| G | `centered-hero`, `frame-within-frame` | `axonometric-spatial`, `editorial-column` | 以居中方式或通过展柜式画框呈现馆藏重点。 |
| H | `axonometric-spatial`, `layered-depth` | `large-geometry`, `folded-space` | 表达轴测结构与空间层次。 |

## 8. 使用规则

所有分类路线均继承 `references/typography-constraints.md` 中的当前排版档位，其数值来源为 `assets/typography-defaults.json`。分类路线是候选起点，不是画风或字号限制；全局构图排除项与当前排版档位仍然适用。分类 D 的信息重要性本身并不构成突破当前档位字号规则的授权。旧版 `big-type-only` 版式不适用。

1. 选择优先级：用户明确指令 > 分类映射 > 内容关系精修。先考虑主分类的主要版式，再考虑专项补充与次要版式。即使某项通用质量偏好通常不支持某个已映射的主要版式，该版式仍然可用；例如，分类 G 允许居中呈现文物。在适用处继续应用主题主导的色彩与可读的信息。
2. A/B/C 必须覆盖该分类的不同主要版式，且不得共享相同的构图或文字区。所选版式必须产生空间上不同的标题/信息区，因此三者在文字放置上也各不相同。若只有两个主要版式，通常前两个方向各用一个，第三个方向选择一个不同的专项或次要版式。用户明确固定的版式优先；此时通过其他空间与视觉关系区分三个方向。
3. 对于混合型活动，取相关候选池的并集，并记录主分类与辅分类。主分类决定主要优先级。例如，传统工艺市集为 C 主 + E 辅。不要用固定的通用三件套替代该候选池。

## 9. 需求路由自查

| 主题 | 分类 | 候选自查 |
|---|---|---|
| 书法展 | A | 主要：editorial-column、off-center-hero；专项：diagonal-dynamic；原书法为图像，活动文案为小字。斜向选项已包含。 |
| 社区戏剧节 | B 主；提供多项活动时为 E 辅 | B 主：diagonal-dynamic、radial-composition；节庆类辅候选可扩展候选池。 |
| 传统剪纸市集 | C 主 + E 辅 | C 主：layered-depth、frame-within-frame；市集补充：modular-grid；E 增加 radial-composition、diagonal-dynamic 与 full-bleed-image-overlay。 |
