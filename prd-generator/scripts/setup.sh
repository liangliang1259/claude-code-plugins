#!/bin/bash
# PRD Generator 初始化脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(dirname "$SCRIPT_DIR")"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 PRD Generator 初始化"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3"
    echo "请先安装Python 3.7或更高版本"
    exit 1
fi

echo "✅ Python版本: $(python3 --version)"
echo ""

# 创建必要的目录
echo "创建目录结构..."
mkdir -p "$PLUGIN_ROOT/outputs"
mkdir -p "$PLUGIN_ROOT/outputs/.versions"
mkdir -p "$PLUGIN_ROOT/config"
echo "✅ 目录创建完成"
echo ""

# 安装Python依赖
echo "安装Python依赖..."
cd "$PLUGIN_ROOT"

if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "✅ 依赖安装完成"
else
    echo "⚠️  未找到requirements.txt"
fi
echo ""

# 创建.env文件
if [ ! -f "$PLUGIN_ROOT/.env" ]; then
    echo "创建环境变量文件..."
    if [ -f "$PLUGIN_ROOT/.env.example" ]; then
        cp "$PLUGIN_ROOT/.env.example" "$PLUGIN_ROOT/.env"
        echo "✅ 已创建.env文件（从.env.example复制）"
        echo "   请根据需要修改配置"
    else
        cat > "$PLUGIN_ROOT/.env" <<EOF
# 飞书配置
FEISHU_APP_ID=
FEISHU_APP_SECRET=

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=prd-generator.log

# 输出配置
OUTPUT_DIR=outputs
VERSION_DIR=outputs/.versions
EOF
        echo "✅ 已创建.env文件"
    fi
else
    echo "ℹ️  .env文件已存在，跳过创建"
fi
echo ""

# 检查飞书配置
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "飞书集成配置（可选）"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "如果需要使用飞书文档集成功能，请运行:"
echo "  bash scripts/setup_feishu.sh"
echo ""
echo "或使用命令:"
echo "  /prd-generator:config-feishu"
echo ""

# 完成
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ PRD Generator 初始化完成！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "快速开始:"
echo "  /prd-generator:generate-prd    # 生成PRD"
echo "  /prd-generator:validate-prd    # 验证PRD"
echo "  /prd-generator:version-prd     # 版本管理"
echo ""
echo "查看文档:"
echo "  cat README.md"
echo "  cat docs/USAGE.md"
echo ""
