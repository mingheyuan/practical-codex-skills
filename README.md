# 个人自用 Codex Skills

这个仓库用于存取、备份和持续整理我个人在 Codex 中使用的 skills。它不是某个产品的源代码，也不追求覆盖所有场景；每个 skill 都应该是一套可以反复复用的工作方法。

## 当前内容

目前仓库包含一个统一的产品前端展示 skill：

| Skill | 用途 |
| --- | --- |
| `$product-frontend-showcase` | 设计、实现、审查和验证有清晰产品叙事的官网或产品展示型前端 |

刚刚从 Saymore 页面提炼出的内容已经融合到这个 skill 中，包含：

- 产品官网的信息架构、页面节奏和产品形态 Hero；
- 视觉 token、网格、章节、对比和信任/数据流表达；
- 前端审查、交互状态、无障碍和响应式 QA；
- 基于证据的产品文案、数据边界和功能生命周期标记。

它借鉴的是可复用的方法，不复制 Saymore 的品牌、文案、资源或具体页面。

## 安装

在仓库根目录执行：

```bash
cp -R skills/product-frontend-showcase ~/.codex/skills/
```

安装后可以在任务中使用：

```text
$product-frontend-showcase 帮我把这个产品官网整理成清晰的产品展示页
```

也可以用于审查已有页面或做多尺寸验证：

```text
$product-frontend-showcase 审查这个前端的叙事、交互、响应式和文案风险
```

## 目录结构

```text
skills/
└── product-frontend-showcase/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── design-system.md
        ├── audit-checklist.md
        ├── viewport-matrix.md
        └── claim-matrix.md
scripts/
└── validate_all.py
```

references 按任务需要加载：视觉实现看 `design-system.md`，前端审查看 `audit-checklist.md`，响应式验证看 `viewport-matrix.md`，产品文案或技术宣传看 `claim-matrix.md`。

## 维护原则

- 先确认产品事实，再写营销表达。
- 一个章节只承载一个清晰主张，并给出相应证据。
- 让产品演示帮助理解，不让动画遮蔽内容。
- 把数据流、限制和未完成状态讲清楚。
- 区分观察到的事实、推断和待验证信息。
- 新增 skill 时保持目录独立、触发边界清晰，并在提交前运行校验脚本。

## 校验

```bash
python3 scripts/validate_all.py
```
