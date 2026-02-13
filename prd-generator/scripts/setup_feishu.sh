#!/bin/bash
# 飞书配置脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(dirname "$SCRIPT_DIR")"
CONFIG_DIR="$PLUGIN_ROOT/config"
CONFIG_FILE="$CONFIG_DIR/feishu_config.json"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📱 飞书API配置向导"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查配置目录
if [ ! -d "$CONFIG_DIR" ]; then
    mkdir -p "$CONFIG_DIR"
fi

# 显示帮助信息
echo "在开始之前，请确保你已经："
echo "1. 在飞书开放平台创建了企业自建应用"
echo "2. 获取了 App ID 和 App Secret"
echo "3. 开通了文档读取权限"
echo ""
echo "详细步骤: https://open.feishu.cn/document/home/introduction-to-custom-app-development"
echo ""

# 询问是否继续
read -p "是否继续配置？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "已取消配置"
    exit 0
fi

# 输入App ID
echo ""
echo "请输入飞书应用的 App ID:"
read -r APP_ID

if [ -z "$APP_ID" ]; then
    echo "❌ App ID 不能为空"
    exit 1
fi

# 输入App Secret
echo ""
echo "请输入飞书应用的 App Secret:"
read -rs APP_SECRET
echo

if [ -z "$APP_SECRET" ]; then
    echo "❌ App Secret 不能为空"
    exit 1
fi

# 生成配置文件
echo ""
echo "正在保存配置..."

cat > "$CONFIG_FILE" <<EOF
{
  "app_id": "$APP_ID",
  "app_secret": "$APP_SECRET",
  "api_base_url": "https://open.feishu.cn/open-apis"
}
EOF

chmod 600 "$CONFIG_FILE"

echo "✅ 配置已保存到: $CONFIG_FILE"
echo ""

# 测试连接
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 测试飞书API连接"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 使用Python测试
if command -v python3 &> /dev/null; then
    python3 -c "
import sys
sys.path.insert(0, '$PLUGIN_ROOT/lib')
from feishu_client import FeishuClient

try:
    client = FeishuClient()
    token = client.authenticate()
    print('✅ 认证成功！')
    print(f'Access Token: {token[:20]}...')
except Exception as e:
    print(f'❌ 认证失败: {e}')
    sys.exit(1)
"
    TEST_RESULT=$?
else
    echo "⚠️  未找到Python3，跳过连接测试"
    TEST_RESULT=0
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ 飞书配置完成！"
    echo ""
    echo "现在你可以："
    echo "- 在生成PRD时选择'飞书API'作为输入来源"
    echo "- 直接从飞书文档生成PRD"
    echo ""
    echo "提示："
    echo "- 确保应用已在企业内发布"
    echo "- 确保有文档的访问权限"
else
    echo "⚠️  配置已保存，但连接测试失败"
    echo "请检查："
    echo "- App ID 和 App Secret 是否正确"
    echo "- 应用是否已发布"
    echo "- 网络连接是否正常"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
