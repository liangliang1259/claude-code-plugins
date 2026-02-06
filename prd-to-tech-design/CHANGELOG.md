# Changelog

All notable changes to the PRD to Tech Design plugin will be documented in this file.

## [1.0.1] - 2026-02-06

### Added
- 完整的 Python 实现模块
  - `lib/utils.py` - 工具函数（文件操作、日志、配置管理）
  - `lib/prd_parser.py` - PRD 解析器（章节、需求、用户故事提取）
  - `lib/feishu_client.py` - 飞书 API 客户端
  - `lib/tech_design_template.md` - 技术设计文档模板
- Hook 脚本实现
  - `scripts/validate_output.sh` - 输出验证脚本
  - `scripts/post_process.sh` - 后处理脚本
- PRD 解析功能
  - 自动提取文档章节结构
  - 识别功能需求和优先级
  - 提取用户故事（As a... I want... so that...）
  - 识别约束条件
  - 提取文档元数据
- 飞书集成
  - 支持飞书 API 认证
  - 文档内容获取
  - Markdown 导出功能
- 文档验证
  - 检查必需章节（8个核心章节）
  - 验证 Mermaid 图表数量（至少3个）
  - 内容长度检查
  - 章节内容完整性验证
- 文档后处理
  - 自动生成目录
  - 添加元数据头
  - 创建备份文件
  - 生成文档统计摘要

### Changed
- 更新插件版本号至 1.0.1
- 完善插件配置文件

### Fixed
- 修复模块导入问题（支持相对导入和绝对导入）
- 优化 Mermaid 语法验证逻辑

## [1.0.0] - 2026-02-05

### Added
- 初始版本发布
- 基础插件结构
- 命令定义（generate-tech-design, config-feishu）
- Agent 定义（prd-analyzer, tech-design-generator）
- 技能定义（prd-analysis）
- 示例 PRD 文档
- 配置模板
