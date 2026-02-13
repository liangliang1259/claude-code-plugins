# PRD Generator - 产品需求文档生成器

一个专业的Claude Code插件，帮助产品经理快速生成高质量、结构完整的产品需求文档（PRD）。

## 功能特性

### 🎯 核心功能

- **5种PRD模板**：标准、精益、单页、技术、设计
- **交互式需求收集**：通过专业问题引导收集完整需求
- **自动生成用户故事**：标准格式，包含验收标准
- **成功指标框架**：支持AARRR、HEART、北极星指标、OKRs
- **PRD验证**：自动检查文档完整性和质量
- **版本管理**：完整的版本历史、比较和恢复功能
- **飞书集成**：直接从飞书文档生成PRD

### 📋 PRD模板类型

1. **标准PRD** - 全面的产品需求文档
   - 适用场景：重大项目、新产品、复杂功能
   - 包含15个完整章节
   - 详细的用户故事和技术考虑

2. **精益PRD** - 精简的需求文档
   - 适用场景：敏捷团队、快速迭代、MVP
   - 聚焦核心内容
   - 快速生成和更新

3. **单页PRD** - 执行摘要格式
   - 适用场景：高层汇报、快速决策、概念验证
   - 1-2页概述
   - 核心需求和指标

4. **技术PRD** - 工程重点的需求文档
   - 适用场景：技术项目、系统重构、基础设施
   - 详细的技术架构和API规范
   - 性能和安全要求

5. **设计PRD** - UX/UI重点的需求文档
   - 适用场景：设计密集型功能、UI改版
   - 详细的设计要求和用户体验流程
   - 无障碍和响应式设计

## 安装

### 从Marketplace安装

```bash
claude marketplace add liangliang1259/claude-code-plugins
claude plugin install prd-generator
```

### 本地安装

```bash
cd /path/to/claude-code-plugins
claude --plugin-dir ./prd-generator
```

### 安装依赖

```bash
cd prd-generator
pip install -r requirements.txt
```

## 快速开始

### 1. 生成PRD

```bash
/prd-generator:generate-prd
```

按照提示选择：
1. PRD类型（标准/精益/单页/技术/设计）
2. 输入来源（交互式/本地文件/飞书）
3. 回答需求发现问题
4. 自动生成PRD文档

### 2. 验证PRD

```bash
/prd-generator:validate-prd
```

检查PRD文档的：
- 结构完整性
- 用户故事格式
- 成功指标定义
- 内容质量

### 3. 管理版本

```bash
# 查看版本历史
/prd-generator:version-prd list [PRD名称]

# 比较版本
/prd-generator:version-prd diff [PRD名称] v1 v2

# 恢复版本
/prd-generator:version-prd restore [PRD名称] v3
```

### 4. 配置飞书（可选）

```bash
/prd-generator:config-feishu
```

配置后可以直接从飞书文档生成PRD。

## 使用示例

### 示例1：创建移动端功能PRD

```bash
用户: /prd-generator:generate-prd

助手: 请选择PRD类型：
1. 标准PRD
2. 精益PRD
3. 单页PRD
4. 技术PRD
5. 设计PRD

用户: 1

助手: 请选择输入来源：
1. 交互式输入（推荐）
2. 本地文件
3. 飞书文档导出
4. 飞书API

用户: 1

助手: 让我们开始收集需求信息...

1. 产品/功能名称是什么？

用户: 移动端生物识别认证

[继续对话...]

助手: ✅ PRD已成功生成！

📄 文件位置: outputs/移动端生物识别认证-prd.md
📊 PRD类型: 标准PRD
📅 创建时间: 2026-02-13 14:30:00
```

### 示例2：从飞书文档生成PRD

```bash
用户: /prd-generator:generate-prd

助手: 请选择输入来源：

用户: 4 (飞书API)

助手: 请输入飞书文档URL或文档ID：

用户: https://example.feishu.cn/docx/xxxxxxxxxxxxx

助手: 正在从飞书获取文档...
✅ 文档获取成功！

文档标题: 移动端生物识别认证需求
正在生成PRD...

✅ PRD已成功生成！
```

## 目录结构

```
prd-generator/
├── .claude-plugin/
│   └── plugin.json              # 插件清单
├── commands/                     # 命令定义
│   ├── generate-prd.md          # 生成PRD命令
│   ├── validate-prd.md          # 验证PRD命令
│   ├── config-feishu.md         # 飞书配置命令
│   └── version-prd.md           # 版本管理命令
├── agents/                       # 代理定义
│   ├── prd-discovery.md         # 需求发现代理
│   └── prd-builder.md           # PRD构建代理
├── references/                   # 参考文档
│   ├── prd_template.md          # 标准PRD模板
│   ├── prd_template_lean.md     # 精益PRD模板
│   ├── prd_template_onepager.md # 单页PRD模板
│   ├── prd_template_technical.md# 技术PRD模板
│   ├── prd_template_design.md   # 设计PRD模板
│   ├── user_story_examples.md   # 用户故事示例
│   └── metrics_frameworks.md    # 指标框架指南
├── lib/                          # Python库
│   ├── __init__.py
│   ├── utils.py                 # 工具函数
│   ├── prd_validator.py         # PRD验证
│   ├── prd_generator.py         # PRD生成
│   ├── feishu_client.py         # 飞书客户端
│   └── version_manager.py       # 版本管理
├── scripts/                      # 脚本
│   ├── validate_prd.py          # 验证脚本
│   ├── setup_feishu.sh          # 飞书配置脚本
│   └── setup.sh                 # 初始化脚本
├── config/                       # 配置文件
│   └── feishu_config.example.json
├── examples/                     # 示例文件
│   ├── feature-prd-example.md
│   ├── product-prd-example.md
│   └── enhancement-prd-example.md
├── docs/                         # 文档
│   ├── README.md
│   └── USAGE.md
├── outputs/                      # 输出目录
│   └── .versions/               # 版本历史
├── requirements.txt              # Python依赖
├── .env.example                 # 环境变量示例
├── README.md                    # 主文档
└── CHANGELOG.md                 # 变更历史
```

## 配置

### 环境变量

复制 `.env.example` 到 `.env` 并配置：

```bash
# 飞书配置
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=prd-generator.log

# 输出配置
OUTPUT_DIR=outputs
VERSION_DIR=outputs/.versions
```

### 飞书配置

如需使用飞书集成功能：

1. 访问 [飞书开放平台](https://open.feishu.cn/app)
2. 创建企业自建应用
3. 获取 App ID 和 App Secret
4. 开通文档读取权限
5. 运行 `/prd-generator:config-feishu` 配置

详细步骤见 [飞书配置指南](docs/USAGE.md#飞书集成)

## 最佳实践

### PRD编写建议

1. **明确问题**：清晰描述要解决的问题
2. **用户为中心**：从用户角度思考需求
3. **可衡量**：设定具体的成功指标
4. **范围清晰**：明确包含和不包含的内容
5. **可执行**：提供足够的细节供团队执行

### 用户故事编写

- 使用标准格式：作为...我想要...以便...
- 每个故事3-5个验收标准
- 验收标准必须具体、可测试
- 合理设置优先级（P0/P1/P2）

### 成功指标选择

- 选择合适的指标框架
- 包含当前值和目标值
- 确保指标可衡量和可追踪
- 平衡用户指标和业务指标

### 版本管理

- 重要变更创建版本
- 添加清晰的变更说明
- 使用标签标记里程碑
- 定期清理旧版本

## 故障排查

### 常见问题

**Q: 生成的PRD缺少某些章节？**
A: 检查需求信息是否完整，可以手动补充缺失的章节。

**Q: 用户故事格式不正确？**
A: 运行 `/prd-generator:validate-prd` 检查并修复格式问题。

**Q: 飞书集成无法使用？**
A: 检查App ID和Secret是否正确，确保应用已发布并有文档读取权限。

**Q: 版本历史丢失？**
A: 检查 `outputs/.versions/` 目录是否存在，不要删除该目录。

## 贡献

欢迎贡献代码、报告问题或提出建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

liangliang1259

## 致谢

- 感谢 Claude Code 团队提供的插件平台
- 参考了业界最佳的PRD实践
- 灵感来源于 skills.sh 的 PRD Generator skill

## 相关资源

- [Claude Code 文档](https://docs.anthropic.com/claude/docs)
- [产品管理最佳实践](https://www.productplan.com/learn/product-requirements-document/)
- [用户故事编写指南](https://www.atlassian.com/agile/project-management/user-stories)
- [飞书开放平台](https://open.feishu.cn/)

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

---

**提示**：首次使用建议阅读 [使用指南](docs/USAGE.md) 了解详细功能。
