"""
PRD Validator - PRD文档验证器
"""

import re
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from .utils import read_file, parse_markdown_sections


class PRDValidator:
    """PRD文档验证器"""

    def __init__(self, prd_type: str = "standard"):
        """
        初始化验证器

        Args:
            prd_type: PRD类型 (standard/lean/onepager/technical/design)
        """
        self.prd_type = prd_type
        self.issues = []
        self.warnings = []
        self.suggestions = []
        self.score = 100

    def validate_file(self, file_path: Path) -> Dict:
        """
        验证PRD文件

        Args:
            file_path: PRD文件路径

        Returns:
            Dict: 验证结果
        """
        logging.info(f"开始验证PRD: {file_path}")

        # 读取文件
        content = read_file(file_path)

        # 解析章节
        sections = parse_markdown_sections(content)

        # 执行各项检查
        self._validate_structure(sections)
        self._validate_user_stories(content)
        self._validate_metrics(content)
        self._validate_placeholders(content)
        self._validate_scope(sections)

        # 计算总分
        self._calculate_score()

        # 生成报告
        return self._generate_report()

    def _validate_structure(self, sections: Dict[str, str]) -> None:
        """验证文档结构"""
        required_sections = self._get_required_sections()

        for section in required_sections:
            if section not in sections:
                self.issues.append({
                    "type": "structure",
                    "severity": "error",
                    "message": f"缺少必需章节: {section}"
                })
            elif not sections[section].strip():
                self.warnings.append({
                    "type": "structure",
                    "severity": "warning",
                    "message": f"章节内容为空: {section}"
                })

    def _get_required_sections(self) -> List[str]:
        """获取必需章节列表"""
        if self.prd_type == "standard":
            return [
                "执行摘要",
                "问题陈述",
                "目标与目的",
                "用户画像",
                "用户故事与需求",
                "成功指标",
                "范围",
                "技术考虑"
            ]
        elif self.prd_type == "lean":
            return [
                "问题",
                "解决方案",
                "用户故事",
                "成功指标",
                "范围"
            ]
        elif self.prd_type == "onepager":
            return [
                "概述",
                "核心需求",
                "成功标准",
                "时间线"
            ]
        elif self.prd_type == "technical":
            return [
                "技术背景",
                "架构设计",
                "API规范",
                "数据模型",
                "性能要求"
            ]
        elif self.prd_type == "design":
            return [
                "设计目标",
                "用户研究",
                "用户体验流程",
                "视觉设计要求",
                "交互设计"
            ]
        else:
            return []

    def _validate_user_stories(self, content: str) -> None:
        """验证用户故事格式"""
        # 查找用户故事
        story_pattern = r'(?:####|###)\s*用户故事\s*#?\d+[：:]\s*(.+?)(?=(?:####|###)|$)'
        stories = re.finditer(story_pattern, content, re.DOTALL)

        story_count = 0
        for match in stories:
            story_count += 1
            story_content = match.group(1)

            # 检查格式
            has_as = "作为" in story_content or "**作为**" in story_content
            has_want = "我想要" in story_content or "**我想要**" in story_content
            has_so = "以便" in story_content or "**以便**" in story_content

            if not (has_as and has_want and has_so):
                self.issues.append({
                    "type": "user_story",
                    "severity": "error",
                    "message": f"用户故事 #{story_count} 格式不正确，缺少标准格式（作为...我想要...以便...）"
                })

            # 检查验收标准
            if "验收标准" not in story_content:
                self.warnings.append({
                    "type": "user_story",
                    "severity": "warning",
                    "message": f"用户故事 #{story_count} 缺少验收标准"
                })
            else:
                # 统计验收标准数量
                criteria_count = story_content.count("- [ ]")
                if criteria_count < 3:
                    self.warnings.append({
                        "type": "user_story",
                        "severity": "warning",
                        "message": f"用户故事 #{story_count} 验收标准不足（建议3-5个，当前{criteria_count}个）"
                    })

        if story_count == 0:
            self.warnings.append({
                "type": "user_story",
                "severity": "warning",
                "message": "未找到用户故事"
            })

    def _validate_metrics(self, content: str) -> None:
        """验证成功指标"""
        # 检查是否有指标表格
        has_metrics_table = "|" in content and ("指标" in content or "目标" in content)

        if not has_metrics_table:
            self.warnings.append({
                "type": "metrics",
                "severity": "warning",
                "message": "未找到成功指标表格"
            })
            return

        # 检查指标是否具体
        vague_terms = ["提升", "改善", "优化", "增加", "减少"]
        for term in vague_terms:
            if term in content and "%" not in content:
                self.suggestions.append({
                    "type": "metrics",
                    "severity": "info",
                    "message": f"指标描述可能不够具体，建议使用具体数值（如：提升50%）"
                })
                break

        # 检查是否有指标框架
        frameworks = ["AARRR", "HEART", "北极星", "OKR"]
        has_framework = any(fw in content for fw in frameworks)

        if not has_framework:
            self.suggestions.append({
                "type": "metrics",
                "severity": "info",
                "message": "建议使用成功指标框架（AARRR、HEART、北极星指标或OKRs）"
            })

    def _validate_placeholders(self, content: str) -> None:
        """检查占位符文本"""
        placeholders = [
            r'\[待定\]',
            r'\[TODO\]',
            r'\[TBD\]',
            r'\[待补充\]',
            r'\[待确认\]',
            r'\[日期\]',
            r'\[姓名\]',
            r'\[描述\]',
            r'\[数值\]'
        ]

        for placeholder in placeholders:
            matches = re.finditer(placeholder, content)
            for match in matches:
                # 找到占位符所在行号
                line_num = content[:match.start()].count('\n') + 1
                self.warnings.append({
                    "type": "placeholder",
                    "severity": "warning",
                    "message": f"第{line_num}行发现占位符: {match.group()}",
                    "line": line_num
                })

    def _validate_scope(self, sections: Dict[str, str]) -> None:
        """验证范围定义"""
        scope_keywords = ["范围", "包含", "不包含"]
        has_scope = any(keyword in sections for keyword in scope_keywords)

        if not has_scope:
            self.warnings.append({
                "type": "scope",
                "severity": "warning",
                "message": "未找到范围定义章节"
            })
            return

        # 检查是否明确了不包含的内容
        scope_content = ""
        for key, value in sections.items():
            if "范围" in key:
                scope_content = value
                break

        if "不包含" not in scope_content and "不在范围" not in scope_content:
            self.suggestions.append({
                "type": "scope",
                "severity": "info",
                "message": "建议明确说明不包含在范围内的功能，防止范围蔓延"
            })

    def _calculate_score(self) -> None:
        """计算总分"""
        # 每个错误扣10分
        self.score -= len(self.issues) * 10

        # 每个警告扣5分
        self.score -= len(self.warnings) * 5

        # 确保分数不低于0
        self.score = max(0, self.score)

    def _generate_report(self) -> Dict:
        """生成验证报告"""
        return {
            "score": self.score,
            "issues": self.issues,
            "warnings": self.warnings,
            "suggestions": self.suggestions,
            "summary": {
                "total_issues": len(self.issues),
                "total_warnings": len(self.warnings),
                "total_suggestions": len(self.suggestions)
            }
        }

    def print_report(self, report: Dict) -> None:
        """打印验证报告"""
        print("\n" + "=" * 60)
        print(f"📋 PRD验证报告")
        print("=" * 60)

        # 总分
        score = report["score"]
        if score >= 90:
            score_emoji = "✅"
            score_text = "优秀"
        elif score >= 70:
            score_emoji = "⚠️"
            score_text = "良好"
        else:
            score_emoji = "❌"
            score_text = "需改进"

        print(f"\n{score_emoji} 总体评分: {score}/100 ({score_text})")

        # 统计
        summary = report["summary"]
        print(f"\n📊 问题统计:")
        print(f"  ❌ 错误: {summary['total_issues']}个")
        print(f"  ⚠️  警告: {summary['total_warnings']}个")
        print(f"  ℹ️  建议: {summary['total_suggestions']}个")

        # 详细问题
        if report["issues"]:
            print(f"\n❌ 错误 ({len(report['issues'])}个):")
            for i, issue in enumerate(report["issues"], 1):
                print(f"  {i}. {issue['message']}")

        if report["warnings"]:
            print(f"\n⚠️  警告 ({len(report['warnings'])}个):")
            for i, warning in enumerate(report["warnings"], 1):
                msg = warning['message']
                if 'line' in warning:
                    msg += f" (第{warning['line']}行)"
                print(f"  {i}. {msg}")

        if report["suggestions"]:
            print(f"\nℹ️  改进建议 ({len(report['suggestions'])}个):")
            for i, suggestion in enumerate(report["suggestions"], 1):
                print(f"  {i}. {suggestion['message']}")

        print("\n" + "=" * 60)


def validate_prd(file_path: str, prd_type: str = "standard", verbose: bool = False) -> Dict:
    """
    验证PRD文件的便捷函数

    Args:
        file_path: PRD文件路径
        prd_type: PRD类型
        verbose: 是否打印详细报告

    Returns:
        Dict: 验证结果
    """
    validator = PRDValidator(prd_type)
    report = validator.validate_file(Path(file_path))

    if verbose:
        validator.print_report(report)

    return report
