# Frontend Design - 前端设计插件

一个专业的 Claude Code 插件，帮助创建独特、高质量的前端界面，避免通用的"AI生成"美学。

## 功能特性

### 🎨 核心功能

- **独特设计**：避免通用AI美学，创造真正令人难忘的界面
- **多种风格**：支持极简、极繁、复古、未来等多种美学方向
- **生产级代码**：生成完整、可运行的前端代码
- **细节打磨**：字体、配色、动画、布局的精心设计

### 🚀 设计方向

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

## 安装

### 从Marketplace安装

```bash
claude marketplace add liangliang1259/claude-code-plugins
claude plugin install frontend-design
```

### 本地安装

```bash
cd /path/to/claude-code-plugins
claude --plugin-dir ./frontend-design
```

## 使用方法

### 基本用法

```bash
/frontend-design:create
```

### 使用流程

1. **描述需求**：告诉插件你想创建什么界面
2. **回答问题**：插件会询问目标用户、风格偏好、技术栈等
3. **获取代码**：插件生成完整的、可运行的前端代码
4. **预览调整**：根据需要进行调整和优化

## 示例

### 示例1：音乐播放器

```
用户: /frontend-design:create

助手: 你想创建什么样的前端界面？

用户: 一个音乐播放器，面向年轻用户，希望有未来感

助手: 太好了！我将为你创建一个复古未来主义风格的音乐播放器。

设计方向：
- 风格：80年代赛博朋克 + 霓虹灯效果
- 字体：Orbitron（展示）+ Rajdhani（正文）
- 配色：深色背景 + 霓虹粉/青色强调
- 特色：发光效果、扫描线、故障艺术动画

[生成完整代码...]
```

### 示例2：作品集网站

```
用户: 帮我设计一个摄影师作品集网站

助手: 我将创建一个编辑杂志风格的作品集网站。

设计方向：
- 风格：大胆排版 + 网格布局
- 字体：Bebas Neue（标题）+ Libre Franklin（正文）
- 配色：黑白为主 + 金色强调
- 特色：大图展示、不对称布局、视差滚动

[生成完整代码...]
```

## 设计原则

### ✅ 要做的

1. **大胆选择**：选择极致的风格方向
2. **独特字体**：避免Inter、Roboto等通用字体
3. **创新布局**：打破常规的网格系统
4. **精心动画**：有意义的动效设计
5. **丰富细节**：背景、纹理、视觉效果

### ❌ 避免的

1. **通用美学**：紫色渐变+白底等陈词滥调
2. **系统字体**：Arial、Inter、Roboto
3. **可预测布局**：千篇一律的网格
4. **缺乏个性**：没有上下文特色的设计

## 技术支持

### 支持的技术栈

- HTML/CSS/JavaScript（原生）
- React + Tailwind CSS
- React + CSS Modules
- Vue.js
- 其他现代前端框架

### 代码特性

- ✅ 生产级别代码
- ✅ 响应式设计
- ✅ 无障碍支持
- ✅ 性能优化
- ✅ 完整注释

## 目录结构

```
frontend-design/
├── .claude-plugin/
│   └── plugin.json              # 插件清单
├── commands/
│   └── create.md                # 创建命令
├── agents/
│   └── design-generator.md      # 设计生成代理
├── references/
│   ├── font-combinations.md     # 字体组合参考
│   ├── color-schemes.md         # 配色方案参考
│   └── animation-patterns.md    # 动画模式参考
├── examples/
│   ├── music-player/            # 音乐播放器示例
│   ├── portfolio/               # 作品集示例
│   └── dashboard/               # 仪表板示例
├── docs/
│   ├── README.md                # 详细文档
│   └── USAGE.md                 # 使用指南
└── README.md                    # 主文档
```

## 最佳实践

### 字体选择

**避免**：
- Inter、Roboto、Arial、系统字体

**推荐**：
- 展示字体：Playfair Display, Orbitron, Bebas Neue
- 正文字体：Source Serif Pro, Rajdhani, Libre Franklin

### 配色方案

**原则**：
- 2-3个主色 + 1-2个强调色
- 使用CSS变量保持一致性
- 考虑深色/浅色模式

### 动画设计

**关注点**：
- 页面加载的精心编排
- 交错延迟创造节奏感
- 滚动触发和悬停效果
- 优先使用CSS动画

### 布局创新

**方法**：
- 非对称设计
- 重叠元素
- 对角线流动
- 打破网格
- 慷慨的负空间

## 贡献

欢迎贡献代码、报告问题或提出建议！

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 开启 Pull Request

## 许可证

MIT License

## 作者

liangliang1259

## 致谢

- 基于 Anthropic 的 frontend-design skill
- 感谢 Claude Code 团队提供的插件平台

---

**记住**：Claude 能够创造非凡的创意作品。不要退缩，展示真正的创造力！
