# Practical Codex Skills

一组面向产品官网与前端工作的实用 Codex skills。它们从 Saymore 官网的页面叙事、产品模拟器、信任表达和响应式表现中提炼，但不绑定 Saymore 的品牌、文案或资源。

## Included skills

| Skill | Use it for |
| --- | --- |
| `$product-narrative-landing` | 构建有产品演示、证据和信任层的桌面工具 / AI / 隐私产品官网 |
| `$frontend-audit` | 审查现有网站的架构、视觉系统、交互、无障碍和响应式风险 |
| `$responsive-ui-qa` | 在桌面与移动尺寸验证布局、交互和可访问性回归 |
| `$product-copy-guardrails` | 审核软件产品文案、量化宣传、数据边界和生命周期状态 |

## Install

把 `skills/` 下需要的 skill 文件夹复制到 Codex 的 skills 目录，例如：

```bash
cp -R skills/product-narrative-landing ~/.codex/skills/
```

也可以只在任务中显式引用 `$skill-name`。每个 skill 都有独立的 `SKILL.md`，并按需加载自己的 references。

## Design principles

- 先确认产品事实，再写营销表达。
- 一个章节只承载一个清晰主张。
- 让产品演示帮助理解，不让动画遮蔽内容。
- 把数据流、限制和未完成状态讲清楚。
- 用证据区分“观察到的事实”和“推断”。

## Repository structure

```text
skills/
├── product-narrative-landing/
├── frontend-audit/
├── responsive-ui-qa/
└── product-copy-guardrails/
```

## Contributing

新增 skill 前，确保它有清晰的触发边界、一个短而具体的 `SKILL.md`，以及确实能改变执行质量的 references 或 scripts。运行仓库根目录的校验脚本后再提交。
