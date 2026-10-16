# 实测文字图层渲染（overlay / 字体排版路径）

用于第 7 步中的 overlay 完成。先阅读 `references/typography-constraints.md`：它是档位总入口，本路径的字号、边距、留白与上限均来自当前档位的配置文件——`assets/typography-design-free.json` 或 `assets/typography-small-type.json`——而非本文件。在 design-free-v1 档下没有数值上限。该辅助脚本使用 Pillow 及内置的 TrueType/OpenType Unicode cmap 检查；如果不可用，请使用具备实际字形测量的等效渲染器，或 integrated 生成加像素审查。不要声称执行了未实际运行的渲染。

```text
python scripts/render_text_layers.py --request <task>/render-request.json --out-dir <task>/version-02
```

提供一张无文字的背景/图形图像与确切文案。overlay 需要明确提供的字体文件；脚本绝不搜索系统字体或猜测缺失的字体。它使用 cmap 格式 4/12（TTF/OTF 或第一个 TTC face）对照所提供字体校验每一个非空白码位。不支持的字体映射格式需要等效且经验证的渲染器，而非假定通过。为缺失字形选择另一个提供的字体；报告未解决的字符。该简易辅助脚本支持每项一个字体、横向软换行与纵向分栏；复杂的文字整形、多字体运行、曲线排字或变形文字可以使用等效渲染器，同时保留相同的边界与上限。

## 输入契约

- `background`：包含图形/插画的现有图像绝对路径，且带有安静的文字区域。
- `supplied_fonts`：实际由用户提供的文件的绝对路径，并为本任务明确注册。每项的 `font` 必须解析为这些文件之一。
- `subject_boxes`：一个或多个实际受保护的核心主体矩形，单位为像素 `[left, top, right, bottom]`。使用紧凑的矩形，或对不规则主体使用若干个更小的矩形。主图形可以延伸出这些框之外；这些框保护视觉上至关重要的主体细节。在 design-free-v1 档下它们是测量值而非禁区，允许重叠。
- `min_font_px`：可选整数下限，默认 12；针对实际渠道使用更高的下限。低于 12 会被辅助脚本拒绝。它不认证物理观看距离下的可读性。
- `items`：完整的文案清单；每项具有唯一的 `id`、确切的 `text`、`role`、`font` 以及像素 `region` 矩形。直接映射 title/subtitle；日期、正文、地点、主办方、图注、CTA 及所有其他角色均使用正文字号层级。
- 可选的项字段：`direction`（默认横向，或纵向）、`align`（默认 left，或 center、right）、`color`（默认 #202020）、处于当前档位角色上限内的整数 `font_size_px`（design-free-v1 档下不设上限），以及至少为该角色默认值的 `leading`。纵向换行会开启另一个从右到左的分栏。所提供文字的词与标点均不会被移除；软换行只改变视觉上的行位置。

当前档位从短边计算自动字号。在 small-type-refined-v1 档下它使用 Text Scale=0.35，把每个区域向内缩进短边的 2%，裁剪到 8% 的画布安全区，随后测量完整的标题边界、角色字号、文字块间距与 4% 的核心主体净空。在 design-free-v1 档下它只使用渲染器起始值（边距与间距为 0，无上限），记录几何数据而不据此判否。文字不能悄悄溢出区域之外。如果内容无法在可读性下限之上容纳，或当前档位的组合检查失败，辅助脚本会返回错误且不产出预览；请修改版式/画布。

示例 schema（将每个路径与项替换为实际设计简报；这不是可运行的字体素材）：

```json
{
  "background": "C:/task/selected-background.png",
  "supplied_fonts": ["C:/task/user-supplied-font.ttf"],
  "subject_boxes": [[250, 450, 750, 1100]],
  "min_font_px": 12,
  "items": [
    {
      "id": "title", "role": "title", "text": "所提供的确切标题",
      "font": "C:/task/user-supplied-font.ttf",
      "region": [80, 120, 920, 380], "direction": "horizontal"
    },
    {
      "id": "venue", "role": "venue", "text": "所提供的确切地点",
      "font": "C:/task/user-supplied-font.ttf",
      "region": [80, 1200, 920, 1380]
    }
  ]
}
```

## 输出与评审

使用新的版本目录。现有的输出、源背景与先前的预览绝不被覆盖。输出：

- `text-layer.png`：透明的满画布文字图层；图形保持分离。
- `composed-preview.png`：图形背景加文字图层，等待评审与 HG3。
- `typography-geometry.json`：实际渲染的 bbox、名义字号、文案、字体文件、几何检查结果与合成预览哈希。

## 合成原始必需素材

用 `scripts/overlay_assets.py` 把必需的原始 logo/二维码 PNG 合成到画布；绝不用生成的图形替代，也不要求图像模型画一个空白占位。该辅助脚本读取海报的实际像素尺寸，直接合成到现有画布上，不做内边距或放大。保真是重点：模型绝不重绘 logo；提供的 SVG 必须先被忠实地栅格化为透明 PNG（保留原始几何与颜色），再进行合成。其他对保真敏感的素材同样要求忠实合成原件。该辅助脚本只接受 PNG 输入，其他格式一律拒绝。

```text
python scripts/overlay_assets.py --request <task>/assets-request.json --out-dir <task>/assets-version-02
```

请求 JSON 示例（使用实际的用户提供 PNG 文件）：

```json
{
  "background": "C:/task/composed-preview.png",
  "assets": [
    {
      "id": "institution-logo",
      "path": "C:/task/user-supplied-logo.png",
      "position": "top-right",
      "scale": 0.08,
      "margin": 0.03,
      "opacity": 1.0
    },
    {
      "id": "reservation-qr",
      "path": "C:/task/user-supplied-qr.png",
      "position": "bottom-left",
      "scale": 0.12,
      "margin": 0.03,
      "opacity": 1.0
    }
  ]
}
```

`position` 支持 `top-right`、`top-left`、`bottom-left`、`bottom-right` 与 `center`。`scale` 是素材最长边占海报短边的比例（默认 `0.08`），保持宽高比。`margin` 是同一短边的比例（默认 `0.03`），`opacity` 取值在 `[0, 1]`（默认 `1`）。素材按列表顺序用 `alpha_composite` 合成。输出是指定 out-dir 内新的 `assets-overlay.png`；现有文件与原始文件绝不被覆盖。脚本打印一份 JSON 报告，含实际画布尺寸、每个素材的像素 bbox（`[left, top, right, bottom]`，right/bottom 为开区间）与 SHA-256 哈希。检查结果并确认二维码仍可解码；合成成功不认证可读性或批准。

只将测量得到的 `items` 复制到 `visual_review.typography`，且仅针对匹配的当前像素。独立检查并添加当前档位的评审标志——small-type-refined-v1 档下为 `graphic_primary`、`subject_clearance_verified`、`negative_space_ratio`、`intended_size_readable`；design-free-v1 档下为 `intended_size_readable`、`exact_copy_verified`、`no_pseudo_text`、`facts_preserved`——外加具体的 `evidence`；不要从一次成功的几何渲染中自动填充这些标志。然后运行 `check_poster.py`。可读性、对比度、美学质量与实际负空间面积需要像素检查；仅凭几何不认证对比度、文案或可读性，且在 design-free-v1 档下大字号与叠压不是失败。
