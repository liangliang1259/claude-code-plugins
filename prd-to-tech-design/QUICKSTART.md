# 🚀 快速开始

## 第一次使用？跟着这个做！

### 步骤1️⃣：安装依赖（30秒）

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design
pip install -r requirements.txt
```

### 步骤2️⃣：验证安装（可选，10秒）

```bash
./scripts/test-plugin.sh
```

看到 ✅ 表示一切正常！

### 步骤3️⃣：启动Claude Code（5秒）

```bash
claude --plugin-dir ./
```

### 步骤4️⃣：生成你的第一个技术方案（2分钟）

在Claude Code中输入：

```
> /prd-to-tech-design:generate-tech-design
```

然后：
1. 选择：`本地文件`
2. 输入路径：`./examples/sample-prd.md`
3. 等待生成完成
4. 查看输出：`outputs/2025/02-February/tech-design-用户认证系统-*.md`

### 🎉 完成！

打开生成的文件查看你的第一个技术方案！

```bash
# 查看输出目录
ls -la outputs/

# 用编辑器打开（VS Code）
code outputs/2025/02-February/tech-design-*.md

# 或用默认编辑器打开
open outputs/2025/02-February/
```

---

## 📝 使用你自己的PRD

```bash
# 1. 把你的PRD文件放到项目目录
cp /path/to/your-prd.md .

# 2. 启动Claude Code
claude --plugin-dir ./

# 3. 生成技术方案
> /prd-to-tech-design:generate-tech-design
选择：本地文件
路径：./your-prd.md
```

---

## 🔧 配置飞书API（可选）

如果你想直接从飞书文档生成：

```bash
# 运行配置脚本
./scripts/setup_feishu.sh

# 或在Claude Code中
> /prd-to-tech-design:config-feishu
```

然后就可以使用：
```
> /prd-to-tech-design:generate-tech-design
选择：飞书文档ID
文档ID：docx_xxxxxxxxx
```

---

## ❓ 遇到问题？

1. **依赖安装失败？**
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

2. **命令找不到？**
   - 确保在项目目录下
   - 确保使用了 `--plugin-dir ./` 参数

3. **查看详细使用指南**
   ```bash
   cat docs/USAGE.md
   ```

---

## 📚 更多资源

- 📖 [完整使用指南](docs/USAGE.md)
- 🏗️ [架构图说明](docs/README.md)
- 📄 [示例PRD](examples/sample-prd.md)
- 📋 [技术设计模板](lib/tech_design_template.md)

---

**现在就开始吧！** 🎊

```bash
cd /Users/leon/Documents/code/claude-code-plugins/prd-to-tech-design
claude --plugin-dir ./
```
