# 变更历史

## [1.0.0] - 2026-02-13

### 新增功能

#### 核心功能
- ✨ 支持5种PRD模板类型（标准、精益、单页、技术、设计）
- ✨ 交互式需求发现工作流
- ✨ 自动生成标准格式的用户故事
- ✨ 支持多种成功指标框架（AARRR、HEART、北极星指标、OKRs）
- ✨ PRD文档验证功能
- ✨ 完整的版本管理系统
- ✨ 飞书文档集成

#### PRD模板
- 📝 标准PRD模板 - 15个完整章节
- 📝 精益PRD模板 - 精简的敏捷版本
- 📝 单页PRD模板 - 执行摘要格式
- 📝 技术PRD模板 - 工程重点
- 📝 设计PRD模板 - UX/UI重点

#### 命令
- 🔧 `/prd-generator:generate-prd` - 生成PRD文档
- 🔧 `/prd-generator:validate-prd` - 验证PRD文档
- 🔧 `/prd-generator:config-feishu` - 配置飞书API
- 🔧 `/prd-generator:version-prd` - 版本管理

#### 代理
- 🤖 prd-discovery - 需求发现代理
- 🤖 prd-builder - PRD构建代理

#### 参考文档
- 📚 用户故事示例与最佳实践
- 📚 成功指标框架指南（AARRR、HEART、OKRs）
- 📚 5个完整的PRD模板

#### Python库
- 🐍 utils.py - 通用工具函数
- 🐍 prd_validator.py - PRD验证逻辑
- 🐍 prd_generator.py - PRD生成工具
- 🐍 feishu_client.py - 飞书API客户端
- 🐍 version_manager.py - 版本管理器

#### 版本管理
- 📦 自动版本创建
- 📦 版本历史查看
- 📦 版本差异比较
- 📦 版本恢复功能
- 📦 版本标签管理

#### 飞书集成
- 🔗 飞书API认证
- 🔗 飞书文档读取
- 🔗 飞书文档解析
- 🔗 配置管理

### 文档
- 📖 完整的README文档
- 📖 详细的使用指南
- 📖 命令参考文档
- 📖 代理说明文档
- 📖 示例PRD文档

### 配置
- ⚙️ 插件清单 (plugin.json)
- ⚙️ 环境变量配置 (.env.example)
- ⚙️ 飞书配置示例 (feishu_config.example.json)
- ⚙️ Python依赖 (requirements.txt)

### 特性
- ✅ 全中文支持
- ✅ 结构化需求收集
- ✅ 自动生成用户故事
- ✅ 多种指标框架支持
- ✅ 文档质量验证
- ✅ 完整版本控制
- ✅ 飞书无缝集成

---

## 版本说明

### 版本号规则

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范：

- **主版本号**：不兼容的API修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 变更类型

- ✨ **新增功能** (Added)
- 🔧 **功能变更** (Changed)
- 🐛 **问题修复** (Fixed)
- ⚠️ **废弃功能** (Deprecated)
- 🗑️ **移除功能** (Removed)
- 🔒 **安全修复** (Security)

---

## 未来计划

### v1.1.0 (计划中)
- [ ] 支持更多文档格式导出（PDF、Word）
- [ ] AI辅助需求分析
- [ ] 团队协作功能
- [ ] PRD模板自定义
- [ ] 更多指标框架支持

### v1.2.0 (计划中)
- [ ] 集成Jira/Confluence
- [ ] 自动生成技术方案
- [ ] PRD质量评分系统
- [ ] 多语言支持（英文）

### v2.0.0 (远期规划)
- [ ] Web界面
- [ ] 实时协作编辑
- [ ] PRD模板市场
- [ ] AI自动生成PRD

---

## 反馈与支持

如有问题或建议，请：

1. 提交 [Issue](https://github.com/liangliang1259/claude-code-plugins/issues)
2. 发起 [Pull Request](https://github.com/liangliang1259/claude-code-plugins/pulls)
3. 查看 [文档](docs/README.md)

---

**注意**：本变更历史记录所有值得注意的项目更改。
