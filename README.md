# Claude Code 插件集合

> 实用的 Claude Code 插件集合，提升开发效率

[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-blue)](https://code.claude.com/docs/en/plugin-marketplaces)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📦 可用插件

### 🚀 PRD 转技术设计文档 (prd-to-tech-design)

自动将产品需求文档（PRD）转换为完整的技术设计文档。

**功能特性：**
- 支持 Markdown 本地文件
- 支持飞书在线文档
- 智能分析需求并生成技术方案
- 自动生成数据库设计、API 设计等内容

**安装使用：**

```bash
# 1. 安装插件市场
claude marketplace add liangliang1259/claude-code-plugins

# 2. 安装插件
claude plugin install prd-to-tech-design

# 3. 使用插件
/prd-to-tech-design:generate-tech-design
```

**详细文档：** [prd-to-tech-design/README.md](./prd-to-tech-design/README.md)

---

## 🛠️ 快速开始

### 方式一：通过 Claude Code 命令安装（推荐）

```bash
# 添加插件市场
claude marketplace add liangliang1259/claude-code-plugins

# 列出可用插件
claude plugin list

# 安装插件
claude plugin install prd-to-tech-design
```

### 方式二：从 GitHub 克隆

```bash
# 克隆仓库
git clone https://github.com/liangliang1259/claude-code-plugins.git
cd claude-code-plugins/prd-to-tech-design

# 安装依赖
pip install -r requirements.txt

# 启动 Claude Code 并加载插件
claude --plugin-dir ./
```

### 方式三：配置自动加载

在 Claude Code 配置文件中添加：

```json
{
  "pluginDir": "/path/to/claude-code-plugins"
}
```

配置文件位置：
- macOS: `~/.config/claude/settings.json`
- Windows: `%APPDATA%\claude\settings.json`
- Linux: `~/.config/claude/settings.json`

---

## 📚 插件开发

如果你想开发自己的插件：

1. 参考 [prd-to-tech-design](./prd-to-tech-design/) 的结构
2. 创建 `.claude-plugin/plugin.json` 配置文件
3. 实现你的功能

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License

---

## 🔗 相关资源

- [Claude Code 官方文档](https://code.claude.com/docs/en/plugin-marketplaces)
- [Awesome Claude Code Plugins](https://github.com/Chat2AnyLLM/awesome-claude-plugins)

---

## ⭐ 如果这个项目对你有帮助，请给个 Star！

Made with ❤️ by [liangliang1259](https://github.com/liangliang1259)
