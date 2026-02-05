#!/bin/bash
# Feishu API Setup Helper Script

set -e

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CONFIG_DIR="$PLUGIN_ROOT/config"
CONFIG_FILE="$CONFIG_DIR/feishu_config.json"

echo "=== Feishu API Configuration Setup ==="
echo ""

# Create config directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Check if config already exists
if [ -f "$CONFIG_FILE" ]; then
    echo "Warning: Configuration file already exists at $CONFIG_FILE"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 0
    fi
fi

# Prompt for credentials
echo "Please provide your Feishu API credentials:"
echo "You can obtain these from https://open.feishu.cn/app"
echo ""

read -p "App ID: " APP_ID
read -sp "App Secret: " APP_SECRET
echo ""
echo ""

# Validate input
if [ -z "$APP_ID" ] || [ -z "$APP_SECRET" ]; then
    echo "Error: App ID and App Secret are required."
    exit 1
fi

# Prompt for custom base URL (optional)
read -p "Base URL (default: https://open.feishu.cn): " BASE_URL
BASE_URL=${BASE_URL:-https://open.feishu.cn}

# Create config file
cat > "$CONFIG_FILE" <<EOF
{
  "app_id": "$APP_ID",
  "app_secret": "$APP_SECRET",
  "base_url": "$BASE_URL",
  "created_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "notes": "Configuration for Feishu API access"
}
EOF

# Set appropriate permissions
chmod 600 "$CONFIG_FILE"

echo "✓ Configuration saved to: $CONFIG_FILE"
echo ""

# Optional: Test the configuration
echo "To test the configuration, run:"
echo "  python3 $PLUGIN_ROOT/lib/feishu_client.py <document_id>"
echo ""
echo "Setup complete! You can now use Feishu document fetching."
