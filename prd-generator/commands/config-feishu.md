---
description: 配置飞书API凭据，用于直接从飞书获取文档
---

# 配置飞书命令

## 命令说明

配置飞书API凭据，使插件能够直接从飞书获取文档内容。

## 使用方法

```bash
/prd-generator:config-feishu
```

## 前置条件

需要创建飞书企业自建应用并获取凭据。

## 工作流程

### 第1步：引导创建飞书应用

显示详细的创建步骤：

```
📱 飞书应用创建指南

1. 访问飞书开放平台
   https://open.feishu.cn/app

2. 创建企业自建应用
   - 点击"创建企业自建应用"
   - 填写应用名称：PRD Generator
   - 填写应用描述
   - 上传应用图标（可选）

3. 获取应用凭证
   - 进入应用详情页
   - 找到"凭证与基础信息"
   - 复制 App ID
   - 复制 App Secret

4. 配置应用权限
   需要开通以下权限：
   - 查看、评论、编辑和管理云空间中所有文件 (docx:document)
   - 查看云空间中所有文件 (docx:document:readonly)

5. 发布应用
   - 创建应用版本
   - 提交审核
   - 等待审核通过
   - 在企业内发布

详细文档：https://open.feishu.cn/document/home/introduction-to-custom-app-development
```

### 第2步：收集凭据

询问用户输入：

1. **App ID**
   ```
   请输入飞书应用的 App ID:
   ```

2. **App Secret**
   ```
   请输入飞书应用的 App Secret:
   ```

### 第3步：验证凭据

使用提供的凭据测试连接：

```python
# 测试认证
client = FeishuClient(app_id, app_secret)
try:
    token = client.authenticate()
    print("✅ 认证成功！")
except Exception as e:
    print(f"❌ 认证失败: {e}")
```

### 第4步：保存配置

将凭据保存到配置文件：

**方式1：配置文件**
保存到 `config/feishu_config.json`:
```json
{
  "app_id": "cli_xxxxxxxxxxxxx",
  "app_secret": "xxxxxxxxxxxxxxxxxxxxx",
  "api_base_url": "https://open.feishu.cn/open-apis"
}
```

**方式2：环境变量**
保存到 `.env` 文件:
```
FEISHU_APP_ID=cli_xxxxxxxxxxxxx
FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxxx
```

### 第5步：测试配置

提供测试选项：

```
配置已保存！

是否需要测试飞书文档获取功能？(y/n)
```

如果用户选择测试：
1. 询问测试文档URL或ID
2. 尝试获取文档内容
3. 显示文档标题和内容预览

### 第6步：完成

显示成功消息：

```
✅ 飞书配置完成！

📝 配置文件: config/feishu_config.json
🔐 凭据已加密存储

现在你可以使用飞书集成功能：
- 在生成PRD时选择"飞书API"作为输入来源
- 直接从飞书文档生成PRD

提示：
- 确保应用已在企业内发布
- 确保有文档的访问权限
- 支持飞书文档和多维表格
```

## 配置管理

### 查看当前配置

```bash
/prd-generator:config-feishu --show
```

显示当前配置（隐藏敏感信息）：
```
当前飞书配置:

App ID: cli_a1b2c3****** (已配置)
App Secret: ********** (已配置)
API地址: https://open.feishu.cn/open-apis
状态: ✅ 已配置

上次测试: 2026-02-13 14:30:00
测试结果: ✅ 成功
```

### 更新配置

```bash
/prd-generator:config-feishu --update
```

重新输入凭据并更新配置。

### 删除配置

```bash
/prd-generator:config-feishu --remove
```

删除保存的凭据（需要确认）。

## 飞书文档格式要求

### 支持的文档类型
- ✅ 飞书文档（Docs）
- ✅ 飞书多维表格（Base）
- ✅ Markdown格式

### 文档结构建议

为了更好地解析，建议飞书文档使用以下结构：

```
# 产品需求

## 问题描述
[问题内容]

## 目标用户
[用户描述]

## 功能需求
[需求列表]

## 成功指标
[指标内容]
```

### 获取文档URL

1. 打开飞书文档
2. 点击右上角"分享"
3. 复制文档链接

URL格式：
```
https://example.feishu.cn/docx/xxxxxxxxxxxxx
```

## 权限说明

### 必需权限

应用需要以下权限才能正常工作：

1. **文档读取权限**
   - `docx:document:readonly` - 查看文档
   - `docx:document` - 读取文档内容

2. **用户信息权限**（可选）
   - `contact:user.base:readonly` - 获取用户基本信息

### 权限配置步骤

1. 进入飞书开放平台
2. 选择应用
3. 点击"权限管理"
4. 搜索并开通所需权限
5. 重新发布应用版本

## 故障排查

### 常见问题

#### 1. 认证失败
```
❌ 认证失败: invalid app_id or app_secret
```

**解决方案**：
- 检查App ID和App Secret是否正确
- 确保应用已发布
- 检查应用是否被禁用

#### 2. 权限不足
```
❌ 权限不足: 无法访问文档
```

**解决方案**：
- 检查应用权限配置
- 确保开通了文档读取权限
- 重新发布应用

#### 3. 文档不存在
```
❌ 文档不存在或无权访问
```

**解决方案**：
- 检查文档URL是否正确
- 确保文档未被删除
- 检查应用是否有文档访问权限

#### 4. 网络错误
```
❌ 网络错误: 连接超时
```

**解决方案**：
- 检查网络连接
- 检查防火墙设置
- 尝试使用代理

## 安全建议

1. **不要提交凭据到版本控制**
   - 将 `config/feishu_config.json` 添加到 `.gitignore`
   - 使用环境变量存储敏感信息

2. **定期更新App Secret**
   - 建议每3-6个月更新一次
   - 更新后重新配置插件

3. **最小权限原则**
   - 只开通必需的权限
   - 定期审查权限使用情况

4. **监控API使用**
   - 关注API调用量
   - 设置异常告警

## 相关命令

- `/prd-generator:generate-prd` - 生成PRD（可使用飞书输入）

## 参考资料

- [飞书开放平台文档](https://open.feishu.cn/document/)
- [飞书API认证指南](https://open.feishu.cn/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
- [飞书文档API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN)
