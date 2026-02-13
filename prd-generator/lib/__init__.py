"""
PRD Generator Plugin - Python Library
"""

__version__ = "1.0.0"
__author__ = "liangliang1259"

from .utils import load_env, setup_logging, get_plugin_root, ensure_dir
from .prd_validator import PRDValidator
from .prd_generator import PRDGenerator
from .version_manager import VersionManager

try:
    from .feishu_client import FeishuClient
except ImportError:
    # Feishu client is optional
    FeishuClient = None

__all__ = [
    "load_env",
    "setup_logging",
    "get_plugin_root",
    "ensure_dir",
    "PRDValidator",
    "PRDGenerator",
    "VersionManager",
    "FeishuClient",
]
