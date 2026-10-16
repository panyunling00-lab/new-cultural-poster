# 人工门脚本集成

在 Skill 根目录下，使用绝对的任务状态与请求路径运行 `scripts/human_gate.py`：

```text
python scripts/human_gate.py --state <task-output>/hg-state.json --request <task-output>/hg-request.json
```

请求文件为 JSON。使用宿主的常规文件编辑工具写入；不要把用户的原话嵌入 shell 命令。state 属于任务输出目录，而非共享的 Skill 文件夹。每个语言版本使用独立的状态文件，每个任务仅允许一个活跃写入者；该脚本是顺序执行的宿主助手辅助工具，而非并发服务器。

除 `init` 外，每个更改状态的请求都需要 `status` 返回的当前整数 `revision`。版本标识符在预览／海报被登记时返回。请求失败会返回退出码 2，并且不更改已保存的状态。先读取结果；绝不要忽略被阻断的检查。

本工作流采用三次人工门加一次终版确认：HG1（确认文字）、HG2（文字选风格）、HG3（三选一·构图+低保真）以及 `confirm_final`（终版确认）。不再有独立的导出审批门。

## action 一览

脚本实际实现的 action，及其各自必需的字段：

| Skill 步骤 | action | 必需数据 |
|---|---|---|
| 首次使用 | `init` | 不存在已有状态 |
| 任意时刻 | `status` | 无；不需要 `revision` |
| 步骤 1（HG1 确认文字） | `brief` | `brief` 对象；`theme_status` = clear / missing / unclear / conflict |
| 步骤 4 登记之前 | `check` | `target` = directions |
| 步骤 4（HG3 登记三张低保真草案） | `directions` | `directions` 中恰好三个对象，每个含 `id` A/B/C、`path`、`style_id`、`layout_id`、`fit_evidence` |
| 步骤 4 收到真实用户回复后 | `select` | `direction`、当前候选 `version`、`human_message` 原文；可选 `refinement_feedback` |
| 步骤 5 完成之前 | `check` | `target` = complete |
| 步骤 5（高保真终版） | `poster` | `path`、`selected_version`、`production_mode` = edit / composite |
| 步骤 6（质检） | `review` | 当前海报 `version`、`decision`、`review_evidence` |
| 步骤 7（终版确认） | `confirm_final` | `confirm` = true、当前海报 `version`、`human_message` 原文 |
| 步骤 8 之前 | `check` | `target` = export |
| 步骤 8 | `exported` | 当前 `version` 与导出 `path` |
| 用户拒绝或请求修改 | `feedback` | `route` = new_directions / local_revision、`human_message` 原文 |

脚本接受的字段取值：`theme_status` = clear / missing / unclear / conflict；`production_mode` = edit / composite；`decision` = pass / revise / rework direction / needs verification / not assessed；`route` = new_directions / local_revision；`check target` = directions / complete / export。登记的图片必须存在、非空，且扩展名为 `.png`、`.jpg`、`.jpeg` 或 `.webp`。

登记 `directions` 还要求：`references/style/<style_id>.md` 画风定义存在、`layout_id` 落在简报的候选池内、每张图片的实际像素比例等于已确认比例，且三张图片哈希互不相同。

`status` 不需要 `revision`。其余每个更改状态的操作（包括 `check`）都需要当前 `revision`，并拒绝过期值。缺少标题、时间或地点不会阻断 `brief`；保留其缺失状态，绝不臆造。主题清晰度由宿主助手判定；Python 只存储该判定，而不是假装理解语义。`approve` 仅作为 `confirm_final` 的旧别名被接受，`awaiting_export_approval`／`export_allowed` 为遗留状态名，不表示另有审批。

## 请求示例

```json
{"action":"init"}
```

```json
{"action":"brief","revision":0,"theme_status":"clear","brief":{"theme":"苏州非遗文化展"}}
```

```json
{"action":"check","revision":1,"target":"directions"}
```

```json
{"action":"directions","revision":1,"directions":[{"id":"A","path":"C:/task/A.png","style_id":"organic-craft","layout_id":"centered-hero"},{"id":"B","path":"C:/task/B.png","style_id":"swiss-editorial","layout_id":"editorial-column"},{"id":"C","path":"C:/task/C.png","style_id":"screenprint","layout_id":"diagonal-dynamic"}]}
```

## 人工门行为

HG1 展示提取出的完整文案（标题、官方定名、时间、场地、主办方、参与信息等），请用户确认或更正，然后结束回合等待真实回复（0 张图）。仅在真实回复后运行 `brief`，`theme_status` 按回复后状态填写；缺失事实保持缺失。

HG2 基于已确认文案，以 2–4 个文字选项描述字重、字形、字距、排印手法与适配理由，请用户选定文字风格或给出偏好，然后结束回合等待真实回复（0 张图）。选择记入对话上下文简报，不新增 action。

HG3 登记并展示恰好三张实际低保真构图草案，标明当前候选版本，请用户选择 A/B/C 或带反馈请求新集合，然后结束本轮。仅在真实用户回复后运行 `select`，提供返回的候选 `version` 与逐字回复。全部拒绝则使用 `feedback`（`new_directions`）返回步骤 4 重做三张并再次经过 HG3；含糊或无回复保持待决，绝不代选。

三个人工门每次都结束回合等待真实回复。选择后按步骤 5 制作并登记唯一一张高保真终版，按步骤 6 质检，整个质检阶段最多两轮修正；仍未通过则停下说明并请用户决定。质检通过后，按步骤 7 展示实际完整版本与已核实尺寸、格式，询问是否为终版；仅在用户对当前版本给出真实确认后运行 `confirm_final`。局部更改使用 `feedback`（`local_revision`）返回步骤 5 并重跑审查；换方向使用 `feedback`（`new_directions`）返回步骤 4 并再次经过 HG3。用户无需输入 action 名或版本 ID；宿主助手将明确无歧义的回复映射到当前展示版本。沉默、工具返回、经过的时间、预选项、模型建议与先前的批准都不是用户同意；含糊或无回复保持待决。

对于重新生成的替换项，登记一组新的 directions 并重新取得选择。若只有一个候选项变化，保留另外两个图像文件，并将三者全部登记为新的当前集合。局部修改保留所选源图像，并使终版确认失效。新的 directions 会清除选择与确认两者。

## 脚本做什么、不做什么

图像登记会检查文件是否存在、扩展名是否受支持、字节数是否非零以及 SHA-256；它不会解码像素、证明三个候选项存在有意义的视觉差异、验证图像是否已展示，或鉴别用户回复的真实性。实际查看、主题判断、制作方式保真、文化审查与质量评分仍留在主 Skill 中。该脚本绝不调用图像生成、等待 stdin 或创建 UI。

宿主必须调用各项检查；该辅助工具无法阻止宿主助手绕过它。确认文本由宿主提供，必须来自真实的对话证据；在对话或任务记录中保留其出处。图片哈希或版本变化不能沿用旧确认。导出核验仅支持字节完全相同的副本；在本第一版中，保持外观不变的格式转换需要单独的视觉核验路径并重新确认。

返回码：0 表示成功或允许，2 表示被阻止或输入错误。读取结果后再继续；绝不要忽略失败。
