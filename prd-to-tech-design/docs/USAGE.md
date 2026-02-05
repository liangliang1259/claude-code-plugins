# PRD转技术方案生成器 - 使用指南

## 快速开始

### 方式一：使用插件目录方式

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design

# 启动Claude Code并指定插件目录
claude --plugin-dir ./prd-to-tech-design
```

启动后，你可以直接使用命令：
```
> /prd-to-tech-design:generate-tech-design
```

### 方式二：安装到Claude Code

```bash
# 将插件安装到Claude Code
claude plugin install ./prd-to-tech-design

# 或者安装到特定范围
claude plugin install ./prd-to-tech-design -s user  # 用户级（所有项目）
claude plugin install ./prd-to-tech-design -s project  # 项目级
```

安装后在任何地方都可以使用：
```
> /prd-to-tech-design:generate-tech-design
```

## 使用流程

### 步骤1：启动插件

```bash
claude --plugin-dir ./prd-to-tech-design
```

### 步骤2：调用生成命令

在Claude Code中输入：

```
> /prd-to-tech-design:generate-tech-design
```

### 步骤3：选择输入方式

系统会询问：**"您想如何提供PRD？"**

选择以下三种方式之一：

#### 选项A：本地文件
```
您想如何提供PRD？ > 本地文件
请提供文件路径： > ./examples/sample-prd.md
```

#### 选项B：飞书导出内容
```
您想如何提供PRD？ > 飞书导出内容
请粘贴markdown内容： >
[这里粘贴从飞书导出的markdown内容]
按 Ctrl+D 结束输入
```

#### 选项C：飞书文档ID
```
您想如何提供PRD？ > 飞书文档ID
请提供文档ID： > docx_xxxxxxxxx
```

### 步骤4：等待生成

插件会自动：
1. 解析PRD内容
2. 分析需求（功能需求、用户故事、约束）
3. 生成技术方案（8个章节）
4. 生成Mermaid图表
5. 保存到文件

### 步骤5：查看输出

文档会保存到：
```
outputs/YYYY/MM-DD/tech-design-{功能名称}-{时间戳}.md
```

例如：
```
outputs/2025/02-February/tech-design-用户认证系统-20250205-153022.md
```

## 配置飞书API（可选）

### 为什么需要配置飞书API？

- **不配置**：只能使用"本地文件"和"飞书导出内容"两种方式
- **配置后**：可以直接使用飞书文档ID，自动从飞书获取文档内容

### 配置步骤

#### 方式1：使用配置命令（推荐）

在Claude Code中运行：
```
> /prd-to-tech-design:config-feishu
```

按提示输入：
- App ID
- App Secret
- Base URL（默认：https://open.feishu.cn）

#### 方式2：使用配置脚本

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design
./scripts/setup_feishu.sh
```

#### 方式3：手动配置

1. 创建配置文件：
```bash
cp config/feishu_config.example.json config/feishu_config.json
```

2. 编辑配置文件：
```json
{
  "app_id": "cli_xxxxxxxxx",
  "app_secret": "your_app_secret_here",
  "base_url": "https://open.feishu.cn"
}
```

### 获取飞书API凭据

1. 访问 https://open.feishu.cn/app
2. 创建"自建应用"
3. 在应用详情页获取：
   - App ID
   - App Secret
4. 在"权限管理"中添加：
   - `docx:document` - 查看、评论、导出和管理文档
   - `docx:document:readonly` - 只读访问文档
5. 发布应用版本

### 测试飞书API配置

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design
python3 lib/feishu_client.py docx_your_document_id
```

## 使用示例

### 示例1：使用示例PRD测试

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design
claude --plugin-dir ./

# 在Claude Code中：
> /prd-to-tech-design:generate-tech-design
选择：本地文件
路径：./examples/sample-prd.md
```

### 示例2：使用自己的PRD

```bash
# 将你的PRD文件放在项目目录
cp /path/to/your-prd.md .

# 然后生成
> /prd-to-tech-design:generate-tech-design
选择：本地文件
路径：./your-prd.md
```

### 示例3：从飞书文档生成

```
> /prd-to-tech-design:generate-tech-design
选择：飞书文档ID
文档ID：docx_cn5xxxxxxxxxxxxx
```

## 输出文档内容

生成的技术设计文档包含：

### 8个主要章节

1. **功能概述**
   - 执行摘要
   - 业务目标
   - 成功指标
   - 范围与边界
   - 用户画像

2. **技术栈选型**
   - 编程语言
   - 框架与库
   - 数据库技术
   - 第三方服务
   - 技术替代方案

3. **核心模块设计**
   - 系统架构图（Mermaid）
   - 核心业务流程图（Mermaid）
   - 模块划分
   - 数据流时序图（Mermaid）
   - 核心算法

4. **数据库设计**
   - 实体关系图（Mermaid ER图）
   - 表结构
   - 索引策略
   - 数据迁移计划

5. **API设计**
   - API端点
   - 认证与授权
   - 速率限制
   - 错误处理

6. **部署架构**
   - 基础设施架构图（Mermaid）
   - CI/CD流程图（Mermaid）
   - 环境配置
   - 监控与日志
   - 灾难恢复流程图（Mermaid）

7. **风险评估**
   - 技术风险
   - 安全考虑
   - 性能风险
   - 运营风险

8. **开发计划**
   - 实施阶段
   - 项目甘特图（Mermaid）
   - 团队结构
   - 测试策略
   - 上线检查清单

## 常见问题

### Q1: 如何查看生成的Mermaid图表？

生成的Markdown文件中的Mermaid代码可以在以下平台渲染：
- **GitHub/GitLab**：直接在仓库中查看
- **Typora**：支持Mermaid渲染
- **Obsidian**：支持Mermaid
- **VS Code**：安装 "Markdown Preview Mermaid Support" 插件
- **在线工具**：https://mermaid.live/

### Q2: 插件命令找不到？

确保：
1. 已启动Claude Code：`claude --plugin-dir ./prd-to-tech-design`
2. 命令格式正确：`/prd-to-tech-design:generate-tech-design`
3. 如果已安装插件，使用：`/generate-tech-design`（不带前缀）

### Q3: 飞书API调用失败？

检查：
1. 配置文件是否存在：`config/feishu_config.json`
2. App ID和App Secret是否正确
3. 应用权限是否已添加
4. 网络连接是否正常
5. 文档ID格式是否正确（应该以 `docx_` 开头）

### Q4: Python依赖安装失败？

```bash
# 使用国内镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或者升级pip后重试
pip install --upgrade pip
pip install -r requirements.txt
```

### Q5: 生成的文档在哪里？

默认保存在：
```
outputs/YYYY/MM-DD/tech-design-{功能名称}-{时间戳}.md
```

可以通过环境变量自定义：
```bash
export TECH_DESIGN_OUTPUT_DIR=/path/to/outputs
```

### Q6: 如何自定义技术设计模板？

编辑 `lib/tech_design_template.md` 文件，修改：
- 章节结构
- 默认内容
- 示例文本
- 图表样式

## 高级用法

### 批量生成

```bash
# 为多个PRD生成技术方案
for prd in prds/*.md; do
  echo "Processing $prd"
  claude --plugin-dir . --prompt "/prd-to-tech-design:generate-tech-design 本地文件 $prd"
done
```

### 集成到CI/CD

```yaml
# .github/workflows/generate-tech-design.yml
name: Generate Technical Design

on:
  push:
    paths:
      - 'docs/prd/*.md'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          cd prd-to-tech-design
          pip install -r requirements.txt
      - name: Generate tech design
        run: |
          claude --plugin-dir . --prompt "/prd-to-tech-design:generate-tech-design 本地文件 docs/prd/feature.md"
```

### 自定义输出格式

修改 `lib/utils.py` 中的 `get_output_path` 函数：

```python
def get_output_path(self, feature_name: str) -> Path:
    # 自定义文件名格式
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"{feature_name}-技术方案-{timestamp}.md"
    return self.output_dir / filename
```

## 技巧和建议

### 1. PRD编写建议

为了生成更好的技术方案，PRD应该包含：
- ✅ 清晰的功能描述
- ✅ 明确的用户故事
- ✅ 具体的验收标准
- ✅ 性能和安全要求
- ✅ 技术约束条件
- ✅ 业务目标和指标

### 2. 迭代优化

生成技术方案后：
1. 审查生成的每个章节
2. 根据实际情况调整内容
3. 补充缺失的技术细节
4. 更新架构图和流程图
5. 与团队讨论和评审

### 3. 版本管理

```bash
# 将生成的技术方案纳入版本控制
git add outputs/*/tech-design-*.md
git commit -m "docs: 添加用户认证系统技术方案"
```

## 获取帮助

- 查看插件文档：`README.md`
- 查看架构图：`docs/README.md`
- 查看示例PRD：`examples/sample-prd.md`
- 查看模板：`lib/tech_design_template.md`

## 反馈和贡献

如果遇到问题或有改进建议：
1. 检查日志：`logs/prd_to_tech_design.log`
2. 查看错误信息
3. 参考示例PRD测试
4. 提交Issue或PR

---

祝你使用愉快！🎉
