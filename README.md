# Cultural Event Poster Generator · 文化活动海报生成器

An AI assistant skill for cultural exhibitions, performances, heritage crafts, workshops, and festivals, with reference-guided visual directions, human selection, typography controls, and quality review.

用于文化展览、演出、非遗手工艺、工作坊与节庆海报设计的 AI skill，包含参考图库、三个视觉方向、人工选择、排版档位和质量审查。

## Choose a language · 选择语言

| Version · 版本 | Skill entry · 主文件 | Guide · 使用说明 |
|---|---|---|
| 中文版 · Chinese | [new-cultural-zh/SKILL.md](new-cultural-zh/SKILL.md) | [English overview of the Chinese package](new-cultural-zh/README.md) |
| English · 英文版 | [new-cultural-en/SKILL.md](new-cultural-en/SKILL.md) | [English README](new-cultural-en/README.md) · [Introduction](new-cultural-en/INTRODUCTION.md) |

Both language versions are self-contained in separate folders: **`new-cultural-zh/`** for Chinese and **`new-cultural-en/`** for English. Each includes its own scripts, references, templates, and assets. Ordinary product advertising is outside their scope.

**中文版位于 `new-cultural-zh/`，英文版位于 `new-cultural-en/`，两个文件夹在仓库根目录并列。** 两个版本均包含完整的脚本、参考文档、模板和素材。普通商品广告不在适用范围内。

```text
new-cultural-poster/
├── README.md
├── new-cultural-zh/
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   ├── references/
│   ├── templates/
│   └── assets/
└── new-cultural-en/
    ├── SKILL.md
    ├── README.md
    ├── scripts/
    ├── references/
    ├── templates/
    └── assets/
```

## Download and use · 下载与使用

1. [Download the repository ZIP](https://github.com/panyunling00-lab/new-cultural-poster/archive/refs/heads/main.zip), or use **Code → Download ZIP**.
2. Extract it. For Chinese, use the entire `new-cultural-zh/` folder. For English, use the entire `new-cultural-en/` folder. No manual rearrangement is needed.
3. Keep each skill's directory structure intact. Configure skill discovery according to your AI assistant environment. Reading `SKILL.md` alone does not supply the image library or executable helpers.
4. Provide an event brief, exact required copy, confirmed canvas ratio, and source assets. The skill begins with copy confirmation, then typography selection, then three composition drafts.

下载 ZIP 并解压后，直接选择完整的 `new-cultural-zh/` 或 `new-cultural-en/` 文件夹，无需重新整理文件。保留目录结构，并按所用 AI 助手的方式加载 skill。提供活动资料、完整文案、明确画幅比例与原始素材后，按流程确认文案、选择文字风格并比较三张构图草案。

## Included · 内容

- 38 visual style definitions and 17 layout definitions.
- 177 individual style-reference images, 38 style contact sheets and an overview, plus 79 composition-reference images.
- Two typography profiles: `design-free-v1` (default) and `small-type-refined-v1`.
- Integrated text generation, model-rendered text compositing, and optional overlay using fonts explicitly supplied for the task.
- Helpers for brief validation, prompt assembly, original-asset compositing, sequential approval state, and evidence-based quality checks.

包含 38 种画风、17 种版式、完整参考图库、两套排版档位，以及文案校验、提示词组装、素材合成、人工确认状态和质量检查工具。

## Requirements and validation · 环境与验证

The host assistant supplies image inspection/generation/editing and cultural research. Python 3 and Pillow are needed for the image helpers. No fonts or generation model are bundled.

The English edition passed 54 bundled regression tests. Its shared scripts, assets, and 55 style/layout definitions match the Chinese source byte-for-byte. See [translation notes](new-cultural-en/TRANSLATION-NOTES.md) for localization scope, consistency clarifications, and validation limits. Some unchanged script diagnostics and shared asset metadata remain Chinese.

需要宿主 AI 助手提供看图、生图、编辑与文化资料核查能力；图片处理脚本需要 Python 3 和 Pillow。不附带字体或生成模型。英文版通过 54 项回归测试，共用脚本与素材保持原样；转换范围及验证说明见上方文档。

Reference images guide design; their inclusion does not establish redistribution or commercial-use permission. Review asset-specific rights before reuse. No additional license is asserted by this repository introduction.
