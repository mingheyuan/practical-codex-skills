# 个人自用 Codex Skills

这个仓库用于存取、备份和持续整理我个人在 Codex 中使用的 skills。它不是某个产品的源代码，也不追求覆盖所有场景；每个 skill 都应该是一套可以反复复用的工作方法。

## 当前内容

目前仓库包含以下 skills：

| Skill | 用途 |
| --- | --- |
| `$product-frontend-showcase` | 设计、实现、审查和验证有清晰产品叙事的官网或产品展示型前端 |
| `$frontend-navigation-fluidity` | 优化已有应用的导航切换、预取与缓存复用、侧栏滑动和内容入场，并用真实浏览器验收 |

刚刚从 Saymore 页面提炼出的内容已经融合到这个 skill 中，包含：

- 产品官网的信息架构、页面节奏和产品形态 Hero；
- 视觉 token、网格、章节、对比和信任/数据流表达；
- 前端审查、交互状态、无障碍和响应式 QA；
- 基于证据的产品文案、数据边界和功能生命周期标记。

它借鉴的是可复用的方法，不复制 Saymore 的品牌、文案、资源或具体页面。

`frontend-navigation-fluidity` 面向后台和工作台等已有应用，提炼了多次前端优化中的方法：明确客户端/服务端导航所有权、按意图预取、版本化缓存、保持组件状态的动效，以及区分真实页面计时与自动化开销的验收。它与产品展示页 skill 独立，不复制具体项目的业务数据、内网配置或源代码。

## 安装

在仓库根目录执行：

```bash
cp -R skills/product-frontend-showcase ~/.codex/skills/
cp -R skills/frontend-navigation-fluidity ~/.codex/skills/
```

安装后可以在任务中使用：

```text
$product-frontend-showcase 帮我把这个产品官网整理成清晰的产品展示页
```

也可以用于审查已有页面或做多尺寸验证：

```text
$product-frontend-showcase 审查这个前端的叙事、交互、响应式和文案风险
```

应用内切换迟缓、闪白或需要借鉴参考站动效时：

```text
$frontend-navigation-fluidity 排查这个工作台切换时的等待和闪白，优化侧栏选中背景与内容入场，并验证历史记录和未保存状态
```

## 目录结构

```text
skills/
├── frontend-navigation-fluidity/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── navigation-and-cache.md
│       ├── navigation-motion.md
│       └── acceptance.md
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

导航优化 skill 的 references 同样按需加载：路由与缓存看 `navigation-and-cache.md`，滑动和入场看 `navigation-motion.md`，测量、回归与发布验收看 `acceptance.md`。

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
