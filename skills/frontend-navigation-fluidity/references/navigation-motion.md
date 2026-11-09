# 状态保留的导航动效

在匹配参考站切换节奏、滑动选中背景或内容入场时阅读。

## 还原交互而非猜测外观

观察完整切换：点击后选中项何时改变、背景如何移动、内容何时开始出现、加载时是否先展示外壳。记录计算样式中的 transition/animation、时长、缓动和 transform；标注来源是运行时、源码还是推断。

例如一次参考实测采用 420ms、`cubic-bezier(0.16, 1, 0.3, 1)`、内容自下方 10px 淡入。这组值可作为该参考的起点，不要求其他项目照搬；用项目可覆盖的 motion tokens 管理，主题颜色仍来自本项目。

## 一个背景跟随真实目标

- 由导航容器拥有一个装饰 indicator，跨需要连续运动的分组共享。真实链接继续提供 aria-current、focus 和交互；indicator 设置 aria-hidden 和 pointer-events:none。
- 以 active link 的 bounding rect 减容器 rect，加对应滚动偏移得到目标位置；宽高来自目标本身，不用菜单序号乘固定高度。
- 初次挂载就位，不从页面角落飞入；没有有效 active item 时隐藏 indicator。后续位置/尺寸更新使用 CSS transition，使连续点击从当前位置接续到新目标。
- 监听实际影响几何的变化：路由、折叠、尺寸、字体/标签变化；按需要使用 ResizeObserver。区分共同滚动容器与独立滚动区域，后者要处理滚动重新定位。清理 observer 和 rAF。
- 激活共享背景后移除链接自身重复的 active 底色/阴影，但保留文字、图标和键盘 focus。检查 stacking context、圆角和点击区域。

## 内容只入场，业务树保持挂载

- 动画作用于稳定 DOM 节点：opacity 与短距离 transform 通常足够。不要把 route key 加到业务子树上，不使用先退场后挂载导致的额外等待。
- 声明 presentation identity：pathname 加实际改变视图的参数。列表搜索、分页、抽屉或翻译更新不应意外重播整个页面；是否有意重播需按产品语义选择。
- 如果 loading boundary 早于内容提交，优先使用显式内容就绪契约，在首次可读结构出现时播放一次。需要 DOM 观察兜底时，使用该产品稳定的内容标记；不能假定所有页面都有 h1，也不能让 observer 在未就绪时永久保留。
- 新导航取消旧动画与观察，后台 query 更新不再次播放。不要在每次数据到达时设置全页 opacity:0。
- 遵循 prefers-reduced-motion；偏好动态切换为 reduce 时取消当前动画。只覆盖测试 token 不等于验证了真实系统偏好路径。
- transform 会创建 containing/stacking context；检查 fixed/sticky、popover、portal、selection 和滚动行为，避免在整个应用外壳上随意添加 transform。让最终状态回到正常样式，清理 animation 对象。

## 几何与中间帧证据

一次浏览器验收至少包含：

- 切换前 active rect 与 indicator rect；
- 切换中的 indicator 目标 transform 与当前 computed transform，两者不同证明存在真实移动；内容 opacity 及 translateY 证明入场；
- 结束后的两组 rect 对齐，opacity:1 且无残余位移；
- 跨分组、快速连续点击、折叠/展开、不同宽度、后台刷新不重播；
- 未保存草稿和业务组件实例保持，不因动效重新挂载。

截图用来展示最终视觉；不能用一张静态截图宣称帧率、流畅性或输入状态保留。测试夹具应导入生产组件，动效隔离夹具可替换路由，但真实路由契约还需真实框架验收。
