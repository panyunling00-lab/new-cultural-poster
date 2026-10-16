# 文化海报文字系统

## 生效档位

本文件只在 `typography_profile = small-type-refined-v1` 时生效；默认档为 `design-free-v1`，此时排版规则见 `references/typography-constraints.md`，本文件的数值与上限不生效。本文件所有数值的唯一来源是 `assets/typography-small-type.json`；`scripts/typography_policy.py` 从这里读数值，用于提示词、渲染与质检。下述配对、气质簇与字图关系同样只在本档下使用。

在方向规划、提示词组装、细化与质量检查时读取。先读活动分类与构图映射，再用本文件快速选择文字方案；需要细分字形时读取本文件对应配对。路径相对于 skill 根目录。

## 1. 快速选择：活动 → 构图 → 字体

下表是起点，不是固定模板。用户明确选择优先；主题气质、文案长度和选定风格共同决定最终方案。分类复用 `selection-guide.md`，布局 ID 必须对应真实定义。

| 活动／主题 | 首选构图 | 主标题配对 | 信息文字与字图关系 |
|---|---|---|---|
| 科技、设计方法、公共议题讲座 | editorial-column / modular-grid | 中性现代；强调力量时用粗黑冲击 | 中性现代；标题与列线对齐，信息分组 |
| 文学、历史、哲学讲座／读书会 | editorial-column / minimal-white-space | 书卷印刷；轻松读书会可用温暖手写 | 中性现代或书卷印刷；与书页、图像并置 |
| 艺术、设计展（A） | off-center-hero / editorial-column | 对比衬线或中性现代 | 中性现代；位于主体侧面的安静区 |
| 演出、音乐、舞蹈（B） | diagonal-dynamic / radial-composition | 粗黑冲击或华丽衬线 | 中性现代；顺应运动轴线，功能文字保持稳定 |
| 非遗、陶瓷、编织、手作（C） | layered-depth / frame-within-frame | 书卷印刷或温暖手写 | 中性现代；通过边缘、材料和空间建立联系 |
| 综合论坛、研讨与工作坊（D） | modular-grid / split-vertical | 中性现代 | 中性现代；标题、议程和参与信息有共同对齐轴 |
| 节庆、亲子、文化市集（E） | modular-grid / radial-composition | 几何圆润或温暖手写 | 中性现代；分区清楚，避免每个活动各用一套字体 |
| 新媒体、实验艺术（F） | large-geometry / folded-space | 中性现代或对比衬线 | 中性现代；可偏移或嵌入，但保留准确阅读区域 |
| 文物、古籍、博物馆（G） | centered-hero / frame-within-frame | 书卷印刷或优雅衬线 | 书卷印刷或中性现代；标题避开文物识别部位 |
| 建筑、园林、城市文化（H） | axonometric-spatial / layered-depth | 中性现代或对比衬线 | 中性现代；与空间轴线、边界或透视呼应 |

一次只选主标题配对与信息配对，不轮询全部字体。A/B/C 可共用配对，通过构图和字图关系体现差异，不能只换字体充当新方向。不要因主题分类自动增加书法、印章或未经核验的文化符号。

## 2. 字体、字阶与字重预算

- 每张海报最多 3 个实际字体家族，优先 1–2 个。中文与拉丁家族分别计数；同一家族的粗细变化不算新家族。双语时可采用中文标题家族 + 中文信息家族 + 共用拉丁家族。
- 最多 3 个字号层级：标题、次标题、正文／时间地点落款。不是每种语言各有三档；同档的光学匹配不应形成额外视觉层级。
- 最多 3 档字重，优先常规与中等两档；粗字重用于短标题。信息字重应清晰，不能为追求纤细而使笔画消失。
- 无次标题时直接使用两档；不要为凑齐层级添加文案。正文、日期、地点和主办方共享信息体系，以分组、位置和留白区分。

## 3. 尺寸、间距与测量

所有数值和测量定义见本档“执行与测量规范”，配对和局部效果不能覆盖该规范。数值由 `assets/typography-small-type.json` 供程序读取。

## 5. 字图关系与执行方式

每个方向选一个主要关系：并置、顺轴、框定、表面嵌入或局部前后交叠。位置跟随选中布局，不固定为同一个角落。文化事实、原始作品、标志与二维码不得被表现性文字损坏或遮挡。

一体生成：把所选配对转成字形、笔画、字距和字重的视觉描述，不传字体文件名；逐字核对实际结果。无需字体包。

叠加排版：使用用户提供的可用字体，记录实际家族与字形覆盖；缺字体时明确需求，不静默换字体。标题艺术设计与信息准确排版可分别处理，但均遵守本档规范。

## 6. 简短决策记录与编辑检查

每个方向只记录：活动分类 / 布局 ID / 主标题与信息配对 / 实际家族预算 / 2–3 档字阶 / 字重 / 字图关系 / 文字区域。

提示词只传当前方案的具体字形、准确文案、位置与本档数值约束，不粘贴整张映射表。HG2 后保留已选文字体系，每次明确 1–3 项修改的位置、动作和预期可见结果。对照前后图片，标记实现、部分实现或未实现，并检查新增错字、遮挡和方向漂移；无变化不能声称细化完成。

最终检查：准确文案与完整覆盖；≤3 家族／字阶／字重；标题块及字号均合规；行距、边距、主体间隔与留白合规；实际尺寸可读。无法验证的项目记为未知，沿用主流程的质量门槛与人工确认，不新增确认轮次。

## 7. 八种字体配对

中文定气质，拉丁文字跟随；仅使用已有文案语言。最多两组配对，总家族数不超过三种。灵感字体名不传给生图工具。

### 1. 中性现代

- 灵感组合：Satoshi + MiSans。
- 提示词字形描述：中文为几何无衬线字形，比例均匀，笔画偏轻至中等；拉丁文字为几何无衬线，字宽均衡，笔画重量匹配；字距适度舒展、克制。
- 气质：冷静中性。
- 主题：展览、美术馆、科技文化。
- 规则：字重协调、间距平稳；信息文字较小但保持可读。

### 2. 几何圆润

- 灵感组合：ITC Avant Garde Gothic + Alibaba PuHuiTi 2.0。
- 提示词字形描述：中文为友好的几何无衬线，笔画末端柔和，字重适度偏粗；拉丁文字呈圆形几何结构与圆润外观，笔画匹配中等至粗重字重。
- 气质：年轻友好。
- 主题：亲子活动、创意市集。
- 规则：圆润节奏与视觉字重协调；除非主题支持，否则避免幼稚装饰。

### 3. 粗黑冲击

- 灵感组合：Helvetica Neue + Plix。
- 提示词字形描述：中文笔画非常粗重、紧凑，字形比例压缩；拉丁文字为超粗、窄体大写，视觉重量密集并向下沉；标题与信息文字形成明显对比。
- 气质：力量硬朗。
- 主题：音乐节、潮流文化、讲座。
- 规则：标题有冲击力，信息处理更平静；不要缩小功能文字。

### 4. 优雅衬线

- 灵感组合：PingFang + MingLiU。
- 提示词字形描述：中文为纤细宋／明体风格，横画细、竖画较强；拉丁文字为精致衬线字形，比例修长，字距舒展。
- 气质：雅致正式。
- 主题：开幕式、颁奖、高雅艺术。
- 规则：这些家族名称只是灵感标签，PingFang 并不是衬线字体。一体生成遵循上述衬线外观；叠加排版使用用户提供的匹配字体。

### 5. 对比衬线

- 灵感组合：Classy Vogue + Source Han Serif CN。
- 提示词字形描述：中文为笔画对比鲜明、衬线锐利的宋体；拉丁文字为高对比编辑型衬线，细发丝线与强竖画形成对比；间距具有精致杂志感。
- 气质：时尚编辑感。
- 主题：设计展、时尚文化活动。
- 规则：中西文字的笔画对比协调；交付尺寸下细笔画仍须可读。

### 6. 温暖手写

- 灵感组合：FontQu Smile（字制区喜脉喜欢体）。
- 提示词字形描述：中文为温暖的手写笔画，动作圆润连贯，节奏轻微不规则；如提供拉丁文案，则采用同样随性节奏的柔和手写字形。
- 气质：亲切治愈。
- 主题：手作市集、读书会、咖啡文化。
- 规则：手写用于短标题，信息文字中性且可读；不添加未要求的拉丁文案。

### 7. 书卷印刷

- 灵感组合：HWMCT（汇文明朝体）。
- 提示词字形描述：中文为印刷明／宋体，笔画对比适中、书卷节奏均衡；如提供拉丁文案，则使用克制的书籍衬线字形，字重与间距相近。
- 气质：古朴书卷。
- 主题：古籍展、书法展、非遗。
- 规则：书卷中文搭配衬线拉丁；不要自动添加旧纸或历史纹样。

### 8. 华丽衬线

- 灵感组合：Kudry + Source Han Serif CN。
- 提示词字形描述：中文为表现性强、笔画对比鲜明的宋体展示字；拉丁文字为装饰性衬线展示字，曲线夸张、间距严密控制，突出戏剧感。
- 气质：华丽戏剧。
- 主题：晚会、周年庆、品牌夜。
- 规则：装饰限于标题，功能信息简单可读。

## 8. 风格与配对协调

| 气质簇 | 风格 ID | 布局 ID | 配对 | 装饰组合（默认克制） |
|---|---|---|---|---|
| 传统书卷 | japanese-ma、cultural-editorial、botanical-premium、art-deco-luxe | editorial-column、frame-within-frame、minimal-white-space | 优雅衬线、书卷印刷、华丽衬线 | 细线框、小印章、竖排日期标签、角标 |
| 现代克制 | swiss-editorial、minimal-graphic、bauhaus-modular、monochrome-typographic | off-center-hero、modular-grid、split-vertical、large-geometry | 中性现代、对比衬线 | 几何线、角标、信息图标、分隔线 |
| 冲击表现 | neo-brutalist、constructivist-impact、pop-commercial、futurist-gradient | diagonal-dynamic、radial-composition、large-geometry | 粗黑冲击、几何圆润 | 斜向切片、用户提供的小数字、小印章式标签 |
| 手作温度 | organic-craft、screenprint、risograph-zine | layered-depth、frame-within-frame、folded-space | 温暖手写、书卷印刷 | 手绘笔画、邮戳、手写备注、纸张纹理 |

装配规则：

1. 选定活动分类 A–H 后，A/B/C 每个方向由同一气质簇内的一个风格、一个布局、一个配对组成。
2. 活动分类映射（`selection-guide.md` 加本文件的配对映射）优先决定气质簇；三个方向尽量覆盖不同首选，禁止同构。
3. 默认禁止跨簇混搭；仅用户明确指定时允许，并在任务记录中注明。
4. 风格与布局冲突仍按 `selection-guide.md` 第 7 节处理。

## 9. 字图关系：压、穿、嵌、隔、退

每个方向选一种主要关系，不叠加全部效果。

| 关系 | 操作 | 边界 |
|---|---|---|
| 压 | 标题叠在安静的非核心图像区 | 不遮挡保护主体或功能文字 |
| 穿 | 装饰线条在标题局部前后穿行 | 字形完整可辨，功能文字不参与 |
| 嵌 | 标题结合纸面、墙面或几何区域 | 不伪造原始作品、铭文或标志 |
| 隔 | 通过留白或分隔线分开字图 | 保持共同阅读轴与分组 |
| 退 | 辅助文字降低视觉权重 | 保持可读，不能无限缩小 |

压、穿、嵌仅用于非核心图像或独立装饰层。受保护主体间隔、标题边界与字号遵守本文执行与测量规范。

## 执行与测量规范

Read before planning, prompt assembly, rendering, and review. This profile's numeric source is `assets/typography-small-type.json`; `scripts/typography_policy.py` loads it for prompts, rendering, and quality checks. This profile applies to every single poster, each A/B/C candidate, selected-direction variant, edit, and derivative. Library references and existing previews never waive it. Preserve all required copy and original assets. Only a later explicit user instruction can change the constraint; the bundled tools deliberately enforce the current profile.

## Measurement and defaults

- Use the entire canvas W × H, including full-bleed backgrounds; S=min(W,H). A title block includes all title lines, bilingual title items, tracking, leading, outlines, and shadows. Measure actual rendered bounds, not only the nominal font size or one glyph.
- Horizontal title: total title-block height / H targets at most 15% and must never exceed 20%. Vertical title: total title-block width / W targets at most 15% and must never exceed 20%. The 15% value is a preferred upper target, never a minimum to fill. The other axis must remain inside the safe zone. Do not test width OR height and choose whichever happens to pass. Mixed writing directions within one title require a separate layout decision.
- Internal Text Scale weight defaults to 0.35; nominal title S_title=0.14 × 0.35 × S=0.049S, with a hard maximum 0.055S. This is this package's local weight, not an undocumented image-generation API parameter. For image models express the same values in natural-language instructions; their pixels still require inspection.
- Subtitle defaults to 0.45 × S_title, maximum 0.50. Body, captions, dates, venue, organizer and other functional copy default to 0.25 × S_title, maximum 0.30. Use light/regular readable strokes and precise alignment; never use large display type for paragraphs. If titles are reduced to fit, recalculate supporting roles from the actual title size. If no title is supplied, use the nominal title size as the reference; do not invent one.
- Default leading: title 1.20, subtitle 1.40, body/functional copy 1.60 times nominal size. Leave at least 0.02S clear space between text blocks, at least 0.04S from protected core-subject bounds, and at least 8% of W/H from the respective canvas edges. Honor larger confirmed safe areas. This is optical text clearance, not printer bleed.
- Reserve at least 30% of the canvas as purposeful low-detail negative space. Empty atmosphere, plain paper and calm full-bleed image regions count; white pixels alone are not the measure. Text-block bounding rectangles together may occupy at most 20% of canvas area. Do not count whitespace inside a large bounding rectangle as permission to enlarge lettering.
- Keep text readable at the intended delivery size. The overlay helper defaults to a 12px nominal floor at native output size; this floor is a starting point, not a print-point or viewing-distance guarantee. Set a higher `min_font_px` when the channel requires it. If complete copy cannot fit above the floor and within caps, revise regions, line breaks, subject placement or canvas; never drop copy, enlarge body type, or silently shrink below the floor.

## Layers and visual priority

Build background and graphic/illustration layers first. The visual subject or thematic graphic carries the composition, may span or support the canvas, and remains the first focus. Text is a separate transparent layer placed according to the selected layout's Text Placement zones (columns, the side opposite an offset subject, footer/corners, or along a diagonal) as a restrained editorial accent. Original calligraphy/artwork may be a subject asset; it is not permission to enlarge event-title copy. Do not add dummy lettering as a graphic workaround.

Use modern minimal, refined, spacious composition across the library. Borrow selected palette, material, form and cultural vocabulary, but suppress conflicting giant-letter, headline-dominant, dense-copy, cropped-title and edge-hugging instructions. The legacy `big-type-only` layout is ineligible under this profile; use a graphic-led eligible layout. Expressive font character can remain at the constrained size.

Overlay: `scripts/render_text_layers.py` measures actual glyph bounds, fits complete copy within supplied regions and the role caps, rejects collisions/unsafe bounds/oversized titles, and saves a transparent text layer plus a versioned composed preview and geometry report. Supply fonts yourself; no automatic system-font fallback. It does not certify aesthetics, contrast or negative-space area. Inspect the completed pixels.

Integrated: append the complete profile to every generation/edit prompt. Measure the completed title block and supporting type; repair failures. Prompt wording alone never proves compliance.

## Review evidence

In `visual_review.typography`, record `profile_id`, `items` (each item's id, role, direction, actual pixel bbox and nominal/equivalent font_size_px), `graphic_primary`, `subject_clearance_verified`, `negative_space_ratio`, `intended_size_readable`, and location-specific `evidence`. Use one of title/subtitle/body for metrics; map every other copy role to body. The renderer supplies geometry but the reviewer must independently inspect graphic priority, negative space, subject clearance, contrast and readability. Integrated approximate size estimates must name their measurement method and uncertainty. Missing evidence is unknown; a breached cap fails H1 and blocks pass. Do not inherit measurements from another version.

Text-free key visuals omit `items` (or use an empty list) and review reserved-area capacity, graphic priority and negative space. Do not demand a nonexistent title. No text is required solely for this profile. Required assets, glyph fidelity and human gates continue to follow the main workflow.
