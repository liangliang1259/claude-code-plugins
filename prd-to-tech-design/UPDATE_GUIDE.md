# 插件更新指南

## 📦 版本 1.0.1 更新内容

本次更新添加了完整的 Python 实现，使插件功能完全可用。

### 🎉 新增功能

1. **完整的 Python 模块实现**
   - PRD 解析器：自动提取需求、用户故事、约束条件
   - 飞书客户端：支持从飞书文档获取 PRD
   - 工具函数库：文件操作、日志、配置管理

2. **智能文档验证**
   - 自动检查技术设计文档的完整性
   - 验证必需章节和 Mermaid 图表
   - 确保文档质量

3. **自动后处理**
   - 生成文档目录
   - 添加元数据和统计信息
   - 创建备份和摘要文件

## 🔄 如何更新插件

### 方式 1：本地开发模式（推荐）

如果你正在本地使用此插件：

```bash
# 1. 拉取最新代码（如果从 git 仓库）
cd /Users/a58/Documents/personal/code/claude-code-plugins/prd-to-tech-design
git pull

# 2. 验证插件
./scripts/test-plugin.sh

# 3. 重启 Claude Code 或重新加载插件
# 在 Claude Code 中执行：
# /reload-plugins
```

### 方式 2：从头安装

```bash
# 1. 克隆仓库
git clone <your-repo-url> prd-to-tech-design
cd prd-to-tech-design

# 2. 安装依赖
pip install -r requirements.txt

# 3. 测试插件
./scripts/test-plugin.sh

# 4. 在 Claude Code 中加载
# 启动 Claude Code 并指定插件目录：
# claude --plugin-dir /path/to/prd-to-tech-design
```

### 方式 3：插件市场安装（未来支持）

```bash
# 在 Claude Code 中执行：
/install prd-to-tech-design
```

## ✅ 验证更新

运行测试脚本确认更新成功：

```bash
./scripts/test-plugin.sh
```

应该看到所有检查项都显示 ✅。

## 🚀 使用更新后的插件

```bash
# 1. 启动 Claude Code
cd /Users/a58/Documents/personal/code/claude-code-plugins/prd-to-tech-design
claude --plugin-dir ./

# 2. 在 Claude Code 中运行
/prd-to-tech-design:generate-tech-design

# 3. 选择 PRD 来源
# - 本地文件：./examples/sample-prd.md
# - 飞书文档：需要先配置飞书 API
```

## 📝 配置飞书（可选）

如果需要从飞书获取 PRD：

```bash
# 1. 运行配置命令
/prd-to-tech-design:config-feishu

# 2. 或手动编辑配置
cp config/feishu_config.example.json config/feishu_config.json
# 编辑 config/feishu_config.json，填入你的 app_id 和 app_secret
```

## 🐛 问题排查

### 插件未加载

```bash
# 检查插件配置
cat .claude-plugin/plugin.json

# 验证文件完整性
./scripts/test-plugin.sh
```

### Python 依赖问题

```bash
# 重新安装依赖
pip install -r requirements.txt

# 检查依赖
python3 -c "import requests, dotenv; print('Dependencies OK')"
```

### 模块导入错误

```bash
# 测试模块导入
python3 -c "
import sys
sys.path.insert(0, 'lib')
from utils import load_env_config
from prd_parser import parse_prd_from_file
from feishu_client import FeishuClient
print('All modules imported successfully')
"
```

## 📚 更多信息

- 详细使用指南：[docs/USAGE.md](docs/USAGE.md)
- 快速开始：[QUICKSTART.md](QUICKSTART.md)
- 变更日志：[CHANGELOG.md](CHANGELOG.md)
- 问题反馈：[GitHub Issues](https://github.com/yourusername/prd-to-tech-design/issues)

## 🎯 下一步

1. ✅ 更新完成
2. 📖 阅读使用文档
3. 🧪 测试插件功能
4. 💡 提供反馈和建议
