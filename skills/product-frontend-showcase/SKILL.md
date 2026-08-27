---
name: product-frontend-showcase
description: "Design, implement, audit, or validate product showcase frontends when the page must explain value, demonstrate the product, and communicate evidence and trust clearly."
---

# 产品前端展示 Skill

这个 skill 用于设计、实现、重构、审查和验证产品官网或产品展示型前端。它适合桌面工具、AI、隐私产品、开发者工具以及其他需要通过页面解释工作流、能力边界和信任方式的软件产品。

不要把它强行用于电商目录、后台 Dashboard、纯内容站或与产品展示无关的通用应用开发。

## 目标

交付一个让用户快速理解产品的前端方案或实现：

- 第一屏说清一个主要产品承诺，并设置一个主要 CTA；
- 页面按照“主张 → 证据 → 边界”的顺序组织，而不是堆叠口号；
- 通过产品形态的 Hero 或演示 UI 展示真实工作流；
- 视觉系统使用角色化 token，确保不同章节和状态保持一致；
- 明确数据流、部署方式、能力边界和 shipped/beta/planned/unknown 状态；
- 在桌面、移动端、键盘操作和 reduced motion 下仍然可理解、可操作。

## 工作模式

根据用户请求选择需要的模式；可以组合使用，不必每次都执行全部内容。

### 1. 设计或实现展示页

1. 先建立产品事实表：目标用户、主要任务、已上线能力、限制、数据边界、证据来源和主要 CTA。
2. 把信息架构写成一组连续主张：Hero/演示、核心结果、证据或测量、前后对比、信任与数据流、工作流细节、部署/方案、兼容性、更新记录、最终 CTA。没有证据的章节删掉或标为待验证。
3. 让 Hero 体现产品工作流。优先使用语义 HTML、CSS 和 SVG 构建产品形态的 UI，而不是只放装饰图。多个场景使用显式状态机管理，避免重复 markup 和不可预测的动画。
4. 按角色化 token 组织颜色、表面、文字、边框、间距和排版。需要具体视觉规则时读取 [references/design-system.md](references/design-system.md)。
5. 为动画和声音提供暂停、重播、静态首帧和 reduced-motion 路径；内容不能依赖自动播放才能被理解。
6. 使用一个有意义的 `h1`、有序标题、命名区域、可键盘操作的 tabs/menus/controls、真实链接和可见 focus 状态。

### 2. 审查或逆向分析已有前端

除非用户另外要求修复，否则只输出分析，不直接改实现文件。

记录观察来源（运行时 DOM、源码、截图或推断），然后检查：

- 信息架构、主 CTA、标题层级、导航和交互后才出现的内容；
- 布局宽度、间距、字体、表面、边框、圆角、阴影、图标和响应式变化；
- tabs、菜单、轮播、表单、自动播放、暂停/重播、loading/empty/error 状态；
- heading、region、button/link、label、focus、对比度、alt 和 reduced motion；
- 数字宣传、功能状态、数据流、保留策略和未明确的限制。

需要逐项清单时读取 [references/audit-checklist.md](references/audit-checklist.md)。报告应区分事实与推断，并按 P0/P1/P2 排序，包含证据、影响和建议。

### 3. 响应式与交互 QA

在页面完成或修改后，至少验证：

- 桌面 `1280 × 720`；
- 可能存在中间断点时的 `1024 × 768`；
- 移动端 `390 × 844`；
- 有明确平板行为时再加 `768 × 1024`。

每个尺寸检查首屏、水平溢出、文字裁切、sticky header、锚点、卡片变换、导航、主要交互、键盘 focus 和 reduced motion。每次操作后检查真实可见结果，不把“点击成功”当作“状态正确”。报告问题时使用 P0/P1/P2，并记录 viewport、route、area、expected、actual、evidence 和 recommendation。需要模板时读取 [references/viewport-matrix.md](references/viewport-matrix.md)。

### 4. 产品文案与宣传审查

对每一条外部可见主张建立 claim matrix，记录证据、状态、缺失条件、误解风险和更安全的写法。状态只使用：

- `shipped`：在指定版本或配置中可用；
- `beta`：可用但有明确限制或范围；
- `planned`：计划中，当前不可用；
- `unknown`：现有材料无法验证。

不要捏造价格、日期、性能倍数、客户数量、兼容性、安全认证或 provider 行为。涉及技术或量化宣传时读取 [references/claim-matrix.md](references/claim-matrix.md)。

## 统一约束

- 产品事实优先于营销语气；无法绑定到行为、测试、更新记录或明确来源的主张应重写、删除或标为 unknown。
- “本地”“私密”“安全”“加密”等词必须说明对应的数据、边界、配置或存储行为。
- 不要暗示模型会读屏、知道事实、执行任务或发送消息，除非产品确实这样做并且页面说明了方式。
- 技术 token（URL、路径、命令、版本、provider、模型名和 API 术语）保持准确，不为了文案风格擅自改写。
- 重复卡片、场景、方案和更新记录使用数组或配置驱动，避免复制多份结构。
- 参考其他网站时只提炼结构和方法，不复制品牌、文案、图片、图标或受保护的视觉资产。

## 输出要求

根据模式输出对应成果：

- 设计/实现：产品事实表、页面主张地图、组件/状态说明、视觉 token、响应式与无障碍验收点，以及实现结果；
- 审查：摘要、信息架构图、token/pattern inventory、优先级问题表、响应式/交互清单和前三项改进；
- QA：按 viewport 和 route 列出 expected/actual/evidence/priority/recommendation；
- 文案：claim matrix、推荐文案、未解决问题和主动拒绝的主张。

完成代码修改后运行项目已有的检查命令，并至少运行仓库根目录的 `scripts/validate_all.py` 验证 skill 结构。
