#!/usr/bin/env python3
"""
PRD验证脚本

用法:
    python validate_prd.py <prd_file.md>
    python validate_prd.py <prd_file.md> --verbose
    python validate_prd.py <prd_file.md> --sections user-stories,metrics
"""

import sys
import argparse
from pathlib import Path

# 添加lib目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from prd_validator import PRDValidator
from utils import setup_logging


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="验证PRD文档")
    parser.add_argument("file", help="PRD文件路径")
    parser.add_argument(
        "--type",
        choices=["standard", "lean", "onepager", "technical", "design"],
        default="standard",
        help="PRD类型"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="显示详细信息"
    )
    parser.add_argument(
        "--sections",
        help="只验证特定章节（逗号分隔），如: user-stories,metrics"
    )

    args = parser.parse_args()

    # 设置日志
    log_level = "DEBUG" if args.verbose else "INFO"
    setup_logging(level=log_level)

    # 检查文件是否存在
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ 错误: 文件不存在: {file_path}")
        sys.exit(1)

    # 创建验证器
    validator = PRDValidator(prd_type=args.type)

    # 执行验证
    print(f"\n正在验证PRD: {file_path}\n")
    print("━" * 60)

    result = validator.validate_file(file_path)

    # 显示结果
    print_validation_result(result, verbose=args.verbose)

    # 返回退出码
    if result["issues"]:
        sys.exit(1)
    else:
        sys.exit(0)


def print_validation_result(result: dict, verbose: bool = False):
    """
    打印验证结果

    Args:
        result: 验证结果
        verbose: 是否显示详细信息
    """
    # 文档结构
    print("\n📋 文档结构检查")
    print("━" * 60)
    structure_ok = True
    for issue in result["issues"]:
        if issue["type"] == "structure":
            print(f"❌ {issue['message']}")
            structure_ok = False
    for warning in result["warnings"]:
        if warning["type"] == "structure":
            print(f"⚠️  {warning['message']}")
            structure_ok = False

    if structure_ok:
        print("✅ 文档结构完整")

    # 用户故事
    print("\n👤 用户故事验证")
    print("━" * 60)
    story_issues = [i for i in result["issues"] if i["type"] == "user_story"]
    story_warnings = [w for w in result["warnings"] if w["type"] == "user_story"]

    if not story_issues and not story_warnings:
        print("✅ 用户故事格式正确")
    else:
        for issue in story_issues:
            print(f"❌ {issue['message']}")
        for warning in story_warnings:
            print(f"⚠️  {warning['message']}")

    # 成功指标
    print("\n📊 成功指标检查")
    print("━" * 60)
    metrics_issues = [i for i in result["issues"] if i["type"] == "metrics"]
    metrics_warnings = [w for w in result["warnings"] if w["type"] == "metrics"]
    metrics_suggestions = [s for s in result["suggestions"] if s["type"] == "metrics"]

    if not metrics_issues and not metrics_warnings:
        print("✅ 成功指标已定义")
    else:
        for issue in metrics_issues:
            print(f"❌ {issue['message']}")
        for warning in metrics_warnings:
            print(f"⚠️  {warning['message']}")

    if verbose:
        for suggestion in metrics_suggestions:
            print(f"ℹ️  {suggestion['message']}")

    # 内容完整性
    print("\n🔍 内容完整性")
    print("━" * 60)
    placeholder_warnings = [w for w in result["warnings"] if w["type"] == "placeholder"]

    if not placeholder_warnings:
        print("✅ 无占位符文本")
    else:
        for warning in placeholder_warnings:
            print(f"⚠️  {warning['message']}")

    # 总体评分
    print("\n" + "━" * 60)
    score = result["score"]
    if score >= 90:
        emoji = "🎉"
        level = "优秀"
    elif score >= 75:
        emoji = "👍"
        level = "良好"
    elif score >= 60:
        emoji = "⚠️"
        level = "及格"
    else:
        emoji = "❌"
        level = "需改进"

    print(f"{emoji} 总体评分: {score}/100 ({level})")
    print("━" * 60)

    # 统计
    issue_count = len(result["issues"])
    warning_count = len(result["warnings"])
    suggestion_count = len(result["suggestions"])

    print(f"\n❌ 问题: {issue_count}项")
    print(f"⚠️  警告: {warning_count}项")
    if verbose:
        print(f"ℹ️  建议: {suggestion_count}项")

    # 改进建议
    if result["suggestions"] and (verbose or issue_count > 0 or warning_count > 0):
        print("\n💡 改进建议")
        print("━" * 60)
        for i, suggestion in enumerate(result["suggestions"][:5], 1):
            print(f"{i}. {suggestion['message']}")

    print()


if __name__ == "__main__":
    main()
