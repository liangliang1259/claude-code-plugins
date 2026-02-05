#!/bin/bash
# 插件快速测试脚本

set -e

PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PLUGIN_ROOT"

echo "======================================"
echo "PRD转技术方案生成器 - 插件测试"
echo "======================================"
echo ""

# 检查Python
echo "1. 检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo "✅ Python版本: $PYTHON_VERSION"
echo ""

# 检查依赖
echo "2. 检查Python依赖..."
MISSING_DEPS=0

check_module() {
    if python3 -c "import $1" 2>/dev/null; then
        echo "✅ $1 已安装"
    else
        echo "❌ $1 未安装"
        MISSING_DEPS=1
    fi
}

check_module "requests"
check_module "dotenv"

if [ $MISSING_DEPS -eq 1 ]; then
    echo ""
    echo "请运行: pip install -r requirements.txt"
    exit 1
fi
echo ""

# 检查关键文件
echo "3. 检查插件文件..."
FILES_OK=true

check_file() {
    if [ -f "$1" ]; then
        echo "✅ $1"
    else
        echo "❌ $1 缺失"
        FILES_OK=false
    fi
}

check_file ".claude-plugin/plugin.json"
check_file "commands/generate-tech-design.md"
check_file "commands/config-feishu.md"
check_file "agents/prd-analyzer.md"
check_file "agents/tech-design-generator.md"
check_file "lib/utils.py"
check_file "lib/prd_parser.py"
check_file "lib/tech_design_template.md"

if [ "$FILES_OK" = false ]; then
    echo ""
    echo "❌ 插件文件不完整"
    exit 1
fi
echo ""

# 检查示例PRD
echo "4. 检查示例PRD..."
if [ -f "examples/sample-prd.md" ]; then
    echo "✅ 示例PRD存在"
    echo ""
    echo "5. 测试PRD解析器..."
    python3 -c "
import sys
sys.path.insert(0, 'lib')
from prd_parser import parse_prd_from_file
parser = parse_prd_from_file('examples/sample-prd.md')
print(f'✅ PRD解析成功')
print(f'   - 识别章节: {len(parser.sections)} 个')
print(f'   - 字数: {parser.content.split().__len__()} 个')
"
else
    echo "⚠️  示例PRD不存在"
fi
echo ""

# 检查飞书配置
echo "6. 检查飞书配置..."
if [ -f "config/feishu_config.json" ]; then
    echo "✅ 飞书配置已配置"
    # 验证配置格式
    if python3 -c "import json; json.load(open('config/feishu_config.json'))" 2>/dev/null; then
        echo "✅ 飞书配置格式正确"
    else
        echo "❌ 飞书配置格式错误"
    fi
else
    echo "⚠️  飞书未配置（仅影响飞书API功能）"
fi
echo ""

# 创建输出目录
echo "7. 准备输出目录..."
mkdir -p outputs
echo "✅ 输出目录已创建: outputs/"
echo ""

echo "======================================"
echo "✅ 插件测试通过！"
echo "======================================"
echo ""
echo "下一步："
echo ""
echo "1. 启动Claude Code并加载插件："
echo "   cd $PLUGIN_ROOT"
echo "   claude --plugin-dir ./"
echo ""
echo "2. 在Claude Code中运行："
echo "   > /prd-to-tech-design:generate-tech-design"
echo ""
echo "3. 选择测试PRD："
echo "   输入方式: 本地文件"
echo "   文件路径: ./examples/sample-prd.md"
echo ""
echo "📖 详细使用指南: docs/USAGE.md"
echo ""
