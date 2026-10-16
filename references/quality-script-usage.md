# 质量脚本集成

在第 8–9 步，使用完整的质量评分标准审查实际海报之后，运行 `scripts/check_poster.py`。首次使用前请阅读本文件。该脚本是 `references/quality-rubric-en.md` 的补充；它不替代文化核验、像素检查、OCR 或人工批准。本文件是唯一记录 request／report 契约的地方；评分标准只保留判定标准与阈值。

```text
python scripts/check_poster.py --request <task>/quality-request.json --out <task>/quality-report.json
```

解码与尺寸检查需要 Pillow。若不可用，H5 保持为 unknown；报告缺失的能力，绝不要声称自动检查已通过。未经适当授权不要安装软件包。不需要其他第三方依赖。

## 请求字段

输入是单个 JSON 对象，包含以下键：

| 字段 | 必需 | 含义 |
|---|---|---|
| `image` | 是 | 当前实际图片的绝对路径。脚本读取该文件以计算其 SHA-256，并在有 Pillow 时解码尺寸与格式。 |
| `stage` | 是 | `key_visual` 或 `final_poster`。其他任何值都是无效请求。 |
| `spec` | 否 | 仅限实际存在／已确认的规格。可识别的键：`width`、`height`（整数）、`format`（如 `PNG`、`JPG`/`JPEG`）、`ratio`（如 `2:3`）。比对失败会强制 H5 为 fail。 |
| `visual_review` | 是 | 评审者针对当前图像记录的证据（见下）。 |

### `visual_review`

在准备看图审查之前，用宿主的文件哈希工具获取当前 SHA-256，并将该审查绑定到该哈希与 stage。审查必须针对这些确切的像素进行，不得继承自先前版本。

| 字段 | 必需 | 含义 |
|---|---|---|
| `image_sha256` | 是 | `image` 所指文件的 SHA-256。必须等于脚本计算出的值；否则该审查未被绑定，所有门槛与维度都按缺失处理。 |
| `stage` | 是 | 必须等于请求的 `stage`；不一致同样使审查未被绑定。 |
| `hard_gates` | 是 | 键为 `H1`–`H8` 的对象（见下）。 |
| `dimensions` | 是 | 键为 `A`–`G` 的对象（见下）。 |
| `typography` | 视情况 | 当前档位的字体排印证据（见下）。 |

## 硬门槛字段：`hard_gates.H1`–`H8`

每个门槛是一个对象 `{"status": ..., "evidence": ...}`。`status` 必须为 `pass`、`fail`、`unknown`、`not_applicable` 之一；其他任何值都是无效请求。`evidence` 必须是非空字符串；为空或缺失会将该门槛强制为 `unknown`。

| 门槛 | 检查项 |
|---|---|
| `H1` | 核心需求与强制字体排印档案（见下方档位规则） |
| `H2` | 文案与事实 |
| `H3` | 文化准确性 |
| `H4` | 主体与结构 |
| `H5` | 使用要求（也会被技术性 `spec` 检查覆盖） |
| `H6` | 指定资产 |
| `H7` | 用户素材的完整呈现 |
| `H8` | 可记忆的视觉核心 |

门槛处理说明：

- 随附的 `scripts/check_poster.py` 在其循环中校验 `H1`–`H7`；`H8` 是评分标准的评审判断项（见 `references/quality-rubric-en.md` 第 5 节），以相同的 `{status, evidence}` 结构记录。八个都要记录，不要省略 `H8`。
- 在 `final_poster` 阶段，`H1`、`H5`、`H7` 不可为 `not_applicable`；脚本会把此类值强制为 `unknown`。
- 在 `key_visual` 阶段，脚本把 `H7` 强制为 `not_applicable` 并注明 `pending final poster verification`。
- 技术性 `spec` 失败会把 `H5` 覆盖为 `fail`；缺少 Pillow 会把 `H5` 强制为 `unknown`，除非它已是 `fail`。

## 维度字段：`dimensions.A`–`G`

每个维度是一个对象 `{"score": ..., "evidence": ...}`。有效分数是 `0`–`5` 的整数，且需要非空的 `evidence`；否则该维度为 `not assessed`。零权重维度（例如 `key_visual` 下的 `G`）可以省略。脚本使用评分标准 1.2 的阶段权重、70/85 阈值、最低分 3 以及硬门槛优先；当评分标准的权重或阈值变化时，重新检查代码。

## 字体排印字段：`visual_review.typography`

当前字体排印档位为 `brief.typography_profile`，默认 `design-free-v1`。`visual_review.typography.profile_id` 必须等于当前档位 id；档案与当前档位不一致的记录视为 `unknown`，不能通过。档位总入口为 `references/typography-constraints.md`；`small-type-refined-v1` 的上限定义在 `references/typography-system.md`；唯一数值来源为 `assets/typography-defaults.json`。字段缺失会强制 `H1` 为 `unknown`；测量到的违规或失败的看图审查标记会强制 `H1` 为 `fail`，无论分数多高。脚本不会根据几何报告推断留白或图形优先级。

通用字段（每个档位）：

| 字段 | 必需 | 含义 |
|---|---|---|
| `profile_id` | 是 | 必须等于当前档位 id。 |
| `evidence` | 是 | 针对本图、指明位置的证据。证据缺失即为 `unknown`。 |
| `intended_size_readable` | 是 | `true` 通过，`false` 失败，缺失为 `unknown`。 |

`design-free-v1`（默认档）额外要求：

| 字段 | 必需 | 含义 |
|---|---|---|
| `exact_copy_verified` | 是 | 全部必需字符串均逐字正确。 |
| `no_pseudo_text` | 是 | 无伪文字或乱码字形。 |
| `facts_preserved` | 是 | 无编造的事实或文化归属。 |

`small-type-refined-v1` 额外要求：

| 字段 | 必需 | 含义 |
|---|---|---|
| `items` | 是 | 已测量文字项的列表；明确无文字的成品 brief 使用空列表并配 `text_free_confirmed=true`。每项包含 `id`、`role`（`title`/`subtitle`/`body`）、`direction`、`bbox`（像素 `[x0,y0,x1,y1]`）与 `font_size_px`。 |
| `graphic_primary` | 是 | 主题图形／插画为第一视觉焦点。 |
| `subject_clearance_verified` | 是 | 已在实际图像上确认核心主体避让。 |
| `negative_space_ratio` | 是 | 有意的低细节负空间占画布面积的比例。 |
| `intended_size_readable` | 是 | 同上。 |

`small-type-refined-v1` 下的主视觉可以省略 `items`；明确无文字的成品 brief 使用空 `items` 并配 `text_free_confirmed=true`。

## 请求示例

该示例刻意不完整，无法通过。用实际观察到的证据与 0–5 的整数分数替换它。`not_applicable` 需要说明。

```json
{
  "image": "C:/task/poster-preview.png",
  "stage": "final_poster",
  "spec": {"ratio": "2:3", "format": "PNG"},
  "visual_review": {
    "image_sha256": "CURRENT_ACTUAL_FILE_HASH",
    "stage": "final_poster",
    "hard_gates": {
      "H1": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H2": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H3": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H4": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H5": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H6": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H7": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H8": {"status": "unknown", "evidence": "Visual core not reviewed yet"}
    },
    "dimensions": {
      "A": {"score": null, "evidence": ""},
      "B": {"score": null, "evidence": ""},
      "C": {"score": null, "evidence": ""},
      "D": {"score": null, "evidence": ""},
      "E": {"score": null, "evidence": ""},
      "F": {"score": null, "evidence": ""},
      "G": {"score": null, "evidence": ""}
    },
    "typography": {
      "profile_id": "design-free-v1",
      "intended_size_readable": null,
      "exact_copy_verified": null,
      "no_pseudo_text": null,
      "facts_preserved": null,
      "evidence": ""
    }
  }
}
```

## 报告字段与退出码

报告中回显 `rubric_version`、`stage`、`image`、`image_sha256`、`inspection`、`technical_checks`、`visual_review_bound_to_image`、`hard_gates`、`typography_checks`、`dimensions`、`total`、`decision`、`known_failures`、`human_approval` 与 `limitations`。退出码 `0` 表示该阶段通过评分标准；退出码 `2` 表示已评估但未通过；退出码 `1` 表示输入无效或执行错误。

## 缺失证据不等于通过

没有证据或未设置 status 的门槛即为 `unknown`；`unknown` 会阻断已确认的交付决定。缺少某个加权分数会产出 `not assessed` 且没有完整总分。`image_sha256` 缺失或不匹配会使审查未被绑定，于是每个门槛与维度都按缺失处理。只要有任何门槛为 `unknown` 或任何加权维度未评分，退出码 `0` 就不可能。即使整体判定为 `not assessed`，也要报告已知的硬门槛失败。`key_visual` 通过不等于最终交付批准。脚本从不执行 OCR、二维码解码或印刷检查，且其分数来自提交的证据——它核验规则，而非证据的真实性。

## 将报告发送至人工门

对于 `final_poster`，将报告中的实际 `decision` 与报告路径传给 `scripts/human_gate.py` 的 `review` action，并使用匹配的已登记海报版本。`review` action 请求要求：

| 字段 | 必需 | 含义 |
|---|---|---|
| `action` | 是 | `"review"`。 |
| `revision` | 是 | 由 `status` 调用返回的当前整数 revision。 |
| `version` | 是 | 正在审查的已登记海报版本；必须与当前海报一致。 |
| `decision` | 是 | `pass`、`revise`、`rework direction`、`needs verification`、`not assessed` 之一。 |
| `review_evidence` | 是 | 非空的质检依据或报告路径。 |

调用 `review` 之前，核验报告的 `image_sha256` 与已登记海报的哈希一致。只有 `pass` 才会把工作流推进到 `awaiting_export_approval`；它绝不提供用户的导出批准。其他结果使海报停留在 `review_poster`，并按评分标准的指引沿用到第 4、7 或 3–6 步。
