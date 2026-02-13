"""
Utility functions for PRD Generator
"""

import os
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


def get_plugin_root() -> Path:
    """
    获取插件根目录

    Returns:
        Path: 插件根目录路径
    """
    # 从当前文件向上查找到插件根目录
    current = Path(__file__).resolve()
    # lib/__init__.py -> lib -> prd-generator
    return current.parent.parent


def load_env(env_file: Optional[str] = None) -> None:
    """
    加载环境变量

    Args:
        env_file: .env文件路径，如果为None则使用默认路径
    """
    if env_file is None:
        plugin_root = get_plugin_root()
        env_file = plugin_root / ".env"

    if os.path.exists(env_file):
        load_dotenv(env_file)
        logging.info(f"已加载环境变量: {env_file}")
    else:
        logging.warning(f"环境变量文件不存在: {env_file}")


def setup_logging(
    level: Optional[str] = None,
    log_file: Optional[str] = None
) -> None:
    """
    配置日志

    Args:
        level: 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: 日志文件路径
    """
    # 从环境变量获取配置
    if level is None:
        level = os.getenv("LOG_LEVEL", "INFO")

    if log_file is None:
        log_file = os.getenv("LOG_FILE")

    # 配置日志格式
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # 配置处理器
    handlers = [logging.StreamHandler()]

    if log_file:
        plugin_root = get_plugin_root()
        log_path = plugin_root / log_file
        handlers.append(logging.FileHandler(log_path, encoding="utf-8"))

    # 配置日志
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=log_format,
        datefmt=date_format,
        handlers=handlers
    )

    logging.info(f"日志系统已初始化，级别: {level}")


def ensure_dir(path: Path) -> None:
    """
    确保目录存在，如果不存在则创建

    Args:
        path: 目录路径
    """
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        logging.debug(f"创建目录: {path}")


def get_output_dir() -> Path:
    """
    获取输出目录

    Returns:
        Path: 输出目录路径
    """
    plugin_root = get_plugin_root()
    output_dir = os.getenv("OUTPUT_DIR", "outputs")
    path = plugin_root / output_dir
    ensure_dir(path)
    return path


def get_version_dir() -> Path:
    """
    获取版本目录

    Returns:
        Path: 版本目录路径
    """
    plugin_root = get_plugin_root()
    version_dir = os.getenv("VERSION_DIR", "outputs/.versions")
    path = plugin_root / version_dir
    ensure_dir(path)
    return path


def sanitize_filename(filename: str) -> str:
    """
    清理文件名，移除不安全的字符

    Args:
        filename: 原始文件名

    Returns:
        str: 清理后的文件名
    """
    # 移除或替换不安全的字符
    unsafe_chars = '<>:"/\\|?*'
    for char in unsafe_chars:
        filename = filename.replace(char, '-')

    # 移除前后空格
    filename = filename.strip()

    # 限制长度
    max_length = 200
    if len(filename) > max_length:
        filename = filename[:max_length]

    return filename


def read_file(file_path: Path, encoding: str = "utf-8") -> str:
    """
    读取文件内容

    Args:
        file_path: 文件路径
        encoding: 文件编码

    Returns:
        str: 文件内容
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return f.read()
    except Exception as e:
        logging.error(f"读取文件失败: {file_path}, 错误: {e}")
        raise


def write_file(
    file_path: Path,
    content: str,
    encoding: str = "utf-8"
) -> None:
    """
    写入文件内容

    Args:
        file_path: 文件路径
        content: 文件内容
        encoding: 文件编码
    """
    try:
        # 确保父目录存在
        ensure_dir(file_path.parent)

        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)

        logging.info(f"文件已保存: {file_path}")
    except Exception as e:
        logging.error(f"写入文件失败: {file_path}, 错误: {e}")
        raise


def get_template_path(template_name: str) -> Path:
    """
    获取模板文件路径

    Args:
        template_name: 模板名称 (如 'prd_template.md')

    Returns:
        Path: 模板文件路径
    """
    plugin_root = get_plugin_root()
    template_path = plugin_root / "references" / template_name

    if not template_path.exists():
        raise FileNotFoundError(f"模板文件不存在: {template_path}")

    return template_path


def format_timestamp(timestamp: Optional[float] = None) -> str:
    """
    格式化时间戳

    Args:
        timestamp: Unix时间戳，如果为None则使用当前时间

    Returns:
        str: 格式化的时间字符串
    """
    from datetime import datetime

    if timestamp is None:
        dt = datetime.now()
    else:
        dt = datetime.fromtimestamp(timestamp)

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_markdown_sections(content: str) -> dict:
    """
    解析Markdown文档的章节结构

    Args:
        content: Markdown内容

    Returns:
        dict: 章节字典 {章节标题: 章节内容}
    """
    sections = {}
    current_section = None
    current_content = []

    for line in content.split('\n'):
        # 检测一级标题
        if line.startswith('# '):
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = line[2:].strip()
            current_content = []
        # 检测二级标题
        elif line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = line[3:].strip()
            current_content = []
        else:
            current_content.append(line)

    # 保存最后一个章节
    if current_section:
        sections[current_section] = '\n'.join(current_content)

    return sections
