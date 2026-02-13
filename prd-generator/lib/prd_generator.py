"""
PRD Generator - PRD文档生成器
"""

import logging
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime
from .utils import get_template_path, read_file, write_file, get_output_dir, sanitize_filename


class PRDGenerator:
    """PRD文档生成器"""

    def __init__(self, prd_type: str = "standard"):
        """
        初始化生成器

        Args:
            prd_type: PRD类型 (standard/lean/onepager/technical/design)
        """
        self.prd_type = prd_type
        self.template_map = {
            "standard": "prd_template.md",
            "lean": "prd_template_lean.md",
            "onepager": "prd_template_onepager.md",
            "technical": "prd_template_technical.md",
            "design": "prd_template_design.md"
        }

    def generate(self, requirements: Dict, output_filename: Optional[str] = None) -> Path:
        """
        生成PRD文档

        Args:
            requirements: 需求信息字典
            output_filename: 输出文件名（可选）

        Returns:
            Path: 生成的PRD文件路径
        """
        logging.info(f"开始生成{self.prd_type} PRD")

        # 加载模板
        template = self._load_template()

        # 填充模板
        content = self._fill_template(template, requirements)

        # 保存文件
        output_path = self._save_prd(content, output_filename or requirements.get("name", "prd"))

        logging.info(f"PRD已生成: {output_path}")
        return output_path

    def _load_template(self) -> str:
        """加载PRD模板"""
        template_name = self.template_map.get(self.prd_type)
        if not template_name:
            raise ValueError(f"不支持的PRD类型: {self.prd_type}")

        template_path = get_template_path(template_name)
        return read_file(template_path)

    def _fill_template(self, template: str, requirements: Dict) -> str:
        """
        填充模板

        Args:
            template: 模板内容
            requirements: 需求信息

        Returns:
            str: 填充后的内容
        """
        content = template

        # 基本信息替换
        content = self._replace_basic_info(content, requirements)

        # 根据PRD类型填充不同内容
        if self.prd_type == "standard":
            content = self._fill_standard_prd(content, requirements)
        elif self.prd_type == "lean":
            content = self._fill_lean_prd(content, requirements)
        elif self.prd_type == "onepager":
            content = self._fill_onepager_prd(content, requirements)
        elif self.prd_type == "technical":
            content = self._fill_technical_prd(content, requirements)
        elif self.prd_type == "design":
            content = self._fill_design_prd(content, requirements)

        return content

    def _replace_basic_info(self, content: str, requirements: Dict) -> str:
        """替换基本信息"""
        # 产品/功能名称
        name = requirements.get("name", "产品名称")
        content = content.replace("[产品/功能名称]", name)

        # 日期
        today = datetime.now().strftime("%Y-%m-%d")
        content = content.replace("[日期]", today)
        content = content.replace("[创建日期]", today)
        content = content.replace("[最后更新]", today)

        # 作者
        author = requirements.get("author", "产品经理")
        content = content.replace("[姓名]", author)
        content = content.replace("[作者]", author)

        # 状态
        content = content.replace("[草稿/审核中/已批准]", "草稿")
        content = content.replace("[状态]", "草稿")

        return content

    def _fill_standard_prd(self, content: str, requirements: Dict) -> str:
        """填充标准PRD"""
        # 问题陈述
        if "problem" in requirements:
            problem = requirements["problem"]
            content = content.replace("[描述现有的情况、痛点或机会]", problem.get("current_state", ""))
            content = content.replace("[清晰阐述需要解决的核心问题]", problem.get("description", ""))
            content = content.replace("[说明问题对用户、业务的影响]", problem.get("impact", ""))

        # 业务目标
        if "goals" in requirements:
            goals = requirements["goals"]
            if isinstance(goals, list):
                goals_text = "\n".join([f"- {goal}" for goal in goals])
                # 简单替换，实际应该更智能
                content = content.replace("- [目标1]\n- [目标2]\n- [目标3]", goals_text)

        # 用户画像
        if "users" in requirements:
            users = requirements["users"]
            # 这里需要更复杂的逻辑来填充用户画像
            # 简化处理

        # 成功指标
        if "metrics" in requirements:
            metrics = requirements["metrics"]
            # 填充指标表格

        # 范围
        if "scope" in requirements:
            scope = requirements["scope"]
            if "in_scope" in scope:
                in_scope_text = "\n".join([f"- {item}" for item in scope["in_scope"]])
                content = content.replace("- [功能1]\n- [功能2]\n- [功能3]", in_scope_text)

            if "out_scope" in scope:
                out_scope_text = "\n".join([f"- {item}" for item in scope["out_scope"]])
                # 替换不包含部分

        return content

    def _fill_lean_prd(self, content: str, requirements: Dict) -> str:
        """填充精益PRD"""
        # 简化的填充逻辑
        if "problem" in requirements:
            content = content.replace("[用1-2段清晰描述问题]", requirements["problem"].get("description", ""))

        if "solution" in requirements:
            content = content.replace("[用1-2段描述解决方案]", requirements["solution"])

        return content

    def _fill_onepager_prd(self, content: str, requirements: Dict) -> str:
        """填充单页PRD"""
        # 单页PRD的填充逻辑
        return content

    def _fill_technical_prd(self, content: str, requirements: Dict) -> str:
        """填充技术PRD"""
        # 技术PRD的填充逻辑
        if "technical" in requirements:
            tech = requirements["technical"]
            # 填充技术相关内容

        return content

    def _fill_design_prd(self, content: str, requirements: Dict) -> str:
        """填充设计PRD"""
        # 设计PRD的填充逻辑
        if "design" in requirements:
            design = requirements["design"]
            # 填充设计相关内容

        return content

    def _save_prd(self, content: str, filename: str) -> Path:
        """
        保存PRD文件

        Args:
            content: PRD内容
            filename: 文件名

        Returns:
            Path: 保存的文件路径
        """
        # 清理文件名
        clean_filename = sanitize_filename(filename)
        if not clean_filename.endswith(".md"):
            clean_filename += "-prd.md"

        # 获取输出目录
        output_dir = get_output_dir()
        output_path = output_dir / clean_filename

        # 写入文件
        write_file(output_path, content)

        return output_path

    def generate_user_story(
        self,
        user_type: str,
        action: str,
        value: str,
        acceptance_criteria: list,
        priority: str = "P0"
    ) -> str:
        """
        生成标准格式的用户故事

        Args:
            user_type: 用户类型
            action: 用户想要执行的操作
            value: 用户获得的价值
            acceptance_criteria: 验收标准列表
            priority: 优先级

        Returns:
            str: 格式化的用户故事
        """
        story = f"""**作为** {user_type}，
**我想要** {action}，
**以便** {value}。

**验收标准**:
"""
        for criterion in acceptance_criteria:
            story += f"- [ ] {criterion}\n"

        story += f"\n**优先级**: {priority}\n"

        return story

    def format_metrics_table(self, metrics: list) -> str:
        """
        格式化成功指标表格

        Args:
            metrics: 指标列表，每个指标是一个字典

        Returns:
            str: 格式化的表格
        """
        table = "| 指标 | 当前值 | 目标值 | 测量方法 |\n"
        table += "|------|--------|--------|----------|\n"

        for metric in metrics:
            name = metric.get("name", "")
            current = metric.get("current", "")
            target = metric.get("target", "")
            method = metric.get("method", "")
            table += f"| {name} | {current} | {target} | {method} |\n"

        return table


def generate_prd(
    prd_type: str,
    requirements: Dict,
    output_filename: Optional[str] = None
) -> Path:
    """
    生成PRD的便捷函数

    Args:
        prd_type: PRD类型
        requirements: 需求信息
        output_filename: 输出文件名

    Returns:
        Path: 生成的PRD文件路径
    """
    generator = PRDGenerator(prd_type)
    return generator.generate(requirements, output_filename)
