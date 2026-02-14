---
description: 创建独特、高质量的前端界面设计
---

# 前端设计命令

## 命令说明

本命令帮助你创建独特、生产级别的前端界面，避免通用的"AI生成"美学。实现真正可用的代码，并对美学细节和创意选择给予极大关注。

## 使用方法

```bash
/frontend-design:create
```

## 工作流程

### 第1步：理解需求

用户提供前端需求：组件、页面、应用或界面。可能包括：
- 目的和受众
- 技术约束
- 设计偏好

### 第2步：设计思考

在编码之前，理解上下文并确定**大胆的美学方向**：

#### 1. 目的分析
- 这个界面解决什么问题？
- 谁会使用它？
- 使用场景是什么？

#### 2. 风格定位

选择一个极致的风格方向（不要中庸）：

**极简主义系列**：
- 极简主义（Brutally Minimal）
- 精致优雅（Luxury/Refined）
- 工业实用（Industrial/Utilitarian）

**丰富表现系列**：
- 极繁主义（Maximalist Chaos）
- 复古未来（Retro-Futuristic）
- 玩趣风格（Playful/Toy-like）

**特色风格系列**：
- 有机自然（Organic/Natural）
- 编辑杂志（Editorial/Magazine）
- 粗野主义（Brutalist/Raw）
- 装饰艺术（Art Deco/Geometric）
- 柔和粉彩（Soft/Pastel）

**关键**：选择清晰的概念方向并精确执行。大胆的极繁主义和精致的极简主义都可以成功 - 关键在于**意图性**，而非强度。

#### 3. 技术约束
- 框架要求（React、Vue、原生HTML等）
- 性能要求
- 无障碍要求

#### 4. 差异化
- 什么让这个设计**令人难忘**？
- 用户会记住的一个特点是什么？

### 第3步：实现代码

生成生产级别、功能完整的代码：

#### 支持的技术栈
- HTML/CSS/JavaScript（原生）
- React + Tailwind CSS
- Vue.js
- 其他现代前端框架

#### 代码要求
- ✅ 生产级别且功能完整
- ✅ 视觉震撼且令人难忘
- ✅ 具有清晰美学观点的连贯性
- ✅ 每个细节都经过精心打磨

### 第4步：前端美学指南

#### 1. 字体排版 🔤

**避免**：
- ❌ Arial、Inter、Roboto等通用字体
- ❌ 系统默认字体

**推荐**：
- ✅ 独特、有趣、美观的字体
- ✅ 意想不到的、有个性的字体选择
- ✅ 搭配：独特的展示字体 + 精致的正文字体

**示例组合**：
- 展示字体：Playfair Display, Bebas Neue, Righteous
- 正文字体：Crimson Text, Source Serif Pro, IBM Plex Sans

#### 2. 色彩与主题 🎨

**原则**：
- 承诺一个连贯的美学
- 使用CSS变量保持一致性
- 主导色 + 鲜明强调色 > 平淡均匀的调色板

**避免**：
- ❌ 紫色渐变 + 白色背景（陈词滥调）
- ❌ 可预测的配色方案

**推荐方法**：
```css
:root {
  /* 主色调 */
  --primary: #...;
  --secondary: #...;

  /* 强调色 */
  --accent: #...;

  /* 背景层次 */
  --bg-primary: #...;
  --bg-secondary: #...;
}
```

#### 3. 动效 ✨

**优先级**：
- HTML：优先使用纯CSS解决方案
- React：使用Motion库（Framer Motion）

**关注点**：
- 高影响力时刻：精心编排的页面加载
- 交错显示（animation-delay）
- 滚动触发效果
- 令人惊喜的悬停状态

**示例**：
```css
/* 交错动画 */
.item:nth-child(1) { animation-delay: 0.1s; }
.item:nth-child(2) { animation-delay: 0.2s; }
.item:nth-child(3) { animation-delay: 0.3s; }
```

#### 4. 空间构图 📐

**打破常规**：
- 意想不到的布局
- 非对称设计
- 重叠元素
- 对角线流动
- 打破网格的元素
- 慷慨的负空间 OR 受控的密度

#### 5. 背景与视觉细节 🎭

**创造氛围和深度**，而非默认纯色：

**技术手段**：
- 渐变网格（Gradient Meshes）
- 噪点纹理（Noise Textures）
- 几何图案（Geometric Patterns）
- 分层透明度（Layered Transparencies）
- 戏剧性阴影（Dramatic Shadows）
- 装饰边框（Decorative Borders）
- 自定义光标（Custom Cursors）
- 颗粒叠加（Grain Overlays）

### 第5步：输出代码

生成完整的、可运行的代码文件：

#### 文件结构
```
component-name/
├── index.html          # HTML结构
├── styles.css          # 样式文件
├── script.js           # 交互逻辑
└── README.md           # 使用说明
```

或React项目：
```
ComponentName/
├── ComponentName.jsx   # 组件代码
├── ComponentName.css   # 样式
└── README.md           # 使用说明
```

## 重要原则

### ✅ 要做的

1. **创意解读**：做出意想不到的选择，真正为上下文设计
2. **风格多样**：在浅色和深色主题、不同字体、不同美学之间变化
3. **匹配复杂度**：
   - 极繁设计 → 精心制作的代码 + 大量动画和效果
   - 极简设计 → 克制、精确、细致的间距和排版
4. **大胆创新**：展示真正的创造力，跳出框架思考

### ❌ 避免的

1. **通用AI美学**：
   - ❌ 过度使用的字体（Inter、Roboto、Arial、系统字体）
   - ❌ 陈词滥调的配色（特别是白底紫色渐变）
   - ❌ 可预测的布局和组件模式
   - ❌ 缺乏上下文特色的千篇一律设计

2. **趋同选择**：
   - ❌ 不要在不同生成中收敛到常见选择（如Space Grotesk）
   - ❌ 每个设计都应该是独特的

## 示例对话流程

```
用户: 帮我设计一个音乐播放器界面

助手: 我将为你创建一个独特的音乐播放器界面。

让我先了解一些信息：

1. 目标用户是谁？（如：年轻人、专业音乐人、古典音乐爱好者）
2. 你希望的风格倾向？（如：复古、未来感、极简、丰富）
3. 技术栈偏好？（React、Vue、原生HTML）
4. 有什么特殊要求吗？

[用户回答后]

太好了！基于你的需求，我将创建一个**复古未来主义**风格的音乐播放器：

设计方向：
- 风格：80年代赛博朋克 + 霓虹灯效果
- 字体：Orbitron（展示）+ Rajdhani（正文）
- 配色：深色背景 + 霓虹粉/青色强调
- 特色：发光效果、扫描线、故障艺术动画

[生成完整代码]
```

## 质量检查清单

生成代码前，确保：

- [ ] 选择了明确的美学方向
- [ ] 字体选择独特且合适
- [ ] 配色方案大胆且连贯
- [ ] 包含有意义的动画效果
- [ ] 布局打破常规
- [ ] 背景和细节丰富
- [ ] 代码完整可运行
- [ ] 响应式设计
- [ ] 无障碍考虑

## 相关资源

- 字体资源：Google Fonts, Adobe Fonts
- 配色工具：Coolors, Adobe Color
- 动画库：Framer Motion, GSAP, Anime.js
- 图案生成：Hero Patterns, CSS Pattern

## 技术提示

### CSS变量最佳实践
```css
:root {
  /* 颜色系统 */
  --color-primary: hsl(280, 100%, 70%);
  --color-accent: hsl(180, 100%, 50%);

  /* 间距系统 */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --space-xl: 4rem;

  /* 字体系统 */
  --font-display: 'Playfair Display', serif;
  --font-body: 'Inter', sans-serif;
}
```

### 动画性能优化
```css
/* 使用transform和opacity以获得最佳性能 */
.animated {
  will-change: transform, opacity;
  transform: translateZ(0); /* 硬件加速 */
}
```

### 响应式设计
```css
/* 移动优先 */
.container {
  padding: var(--space-md);
}

@media (min-width: 768px) {
  .container {
    padding: var(--space-lg);
  }
}

@media (min-width: 1024px) {
  .container {
    padding: var(--space-xl);
  }
}
```

---

**记住**：Claude 能够创造非凡的创意作品。不要退缩，展示当跳出框架思考并完全致力于独特愿景时真正能创造什么。
