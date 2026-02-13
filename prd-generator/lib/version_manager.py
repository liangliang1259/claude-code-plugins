"""
Version Manager - PRD版本管理器
"""

import json
import logging
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
from difflib import unified_diff
from .utils import get_version_dir, read_file, write_file, ensure_dir, format_timestamp


class VersionManager:
    """PRD版本管理器"""

    def __init__(self, prd_name: str):
        """
        初始化版本管理器

        Args:
            prd_name: PRD名称
        """
        self.prd_name = prd_name
        self.version_dir = get_version_dir() / prd_name
        self.metadata_file = self.version_dir / "metadata.json"
        ensure_dir(self.version_dir)

    def create_version(
        self,
        content: str,
        message: str,
        author: Optional[str] = None,
        email: Optional[str] = None
    ) -> str:
        """
        创建新版本

        Args:
            content: PRD内容
            message: 变更说明
            author: 作者姓名
            email: 作者邮箱

        Returns:
            str: 版本号
        """
        # 加载元数据
        metadata = self._load_metadata()

        # 生成版本号
        version = self._generate_version_number(metadata)

        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{version}_{timestamp}.md"
        file_path = self.version_dir / filename

        # 保存版本文件
        write_file(file_path, content)

        # 计算变更统计
        changes = self._calculate_changes(metadata, content)

        # 更新元数据
        version_info = {
            "version": version,
            "timestamp": datetime.now().isoformat(),
            "author": author or "Unknown",
            "email": email or "",
            "message": message,
            "tags": [],
            "file_path": filename,
            "file_size": len(content.encode("utf-8")),
            "line_count": content.count("\n") + 1,
            "changes": changes
        }

        metadata["versions"].append(version_info)
        metadata["current_version"] = version
        self._save_metadata(metadata)

        logging.info(f"已创建版本: {version}")
        return version

    def list_versions(self) -> List[Dict]:
        """
        列出所有版本

        Returns:
            List[Dict]: 版本列表
        """
        metadata = self._load_metadata()
        return metadata.get("versions", [])

    def get_version(self, version: str) -> Optional[Dict]:
        """
        获取版本信息

        Args:
            version: 版本号

        Returns:
            Optional[Dict]: 版本信息
        """
        versions = self.list_versions()
        for v in versions:
            if v["version"] == version:
                return v
        return None

    def get_version_content(self, version: str) -> str:
        """
        获取版本内容

        Args:
            version: 版本号

        Returns:
            str: 版本内容

        Raises:
            FileNotFoundError: 版本不存在
        """
        version_info = self.get_version(version)
        if not version_info:
            raise FileNotFoundError(f"版本不存在: {version}")

        file_path = self.version_dir / version_info["file_path"]
        return read_file(file_path)

    def diff_versions(self, version1: str, version2: str) -> Dict:
        """
        比较两个版本的差异

        Args:
            version1: 版本1
            version2: 版本2

        Returns:
            Dict: 差异信息
        """
        content1 = self.get_version_content(version1)
        content2 = self.get_version_content(version2)

        # 计算差异
        lines1 = content1.splitlines(keepends=True)
        lines2 = content2.splitlines(keepends=True)

        diff = list(unified_diff(
            lines1,
            lines2,
            fromfile=f"版本 {version1}",
            tofile=f"版本 {version2}",
            lineterm=""
        ))

        # 统计变更
        added = sum(1 for line in diff if line.startswith('+') and not line.startswith('+++'))
        deleted = sum(1 for line in diff if line.startswith('-') and not line.startswith('---'))
        modified = min(added, deleted)

        return {
            "version1": version1,
            "version2": version2,
            "diff": "".join(diff),
            "stats": {
                "added": added,
                "deleted": deleted,
                "modified": modified
            }
        }

    def restore_version(self, version: str, message: Optional[str] = None) -> str:
        """
        恢复到指定版本

        Args:
            version: 要恢复的版本号
            message: 恢复说明

        Returns:
            str: 新版本号
        """
        # 获取要恢复的版本内容
        content = self.get_version_content(version)

        # 创建新版本
        restore_message = message or f"恢复到版本 {version}"
        new_version = self.create_version(content, restore_message)

        logging.info(f"已恢复到版本 {version}，新版本: {new_version}")
        return new_version

    def tag_version(self, version: str, tag: str) -> None:
        """
        为版本添加标签

        Args:
            version: 版本号
            tag: 标签名称
        """
        metadata = self._load_metadata()

        for v in metadata["versions"]:
            if v["version"] == version:
                if "tags" not in v:
                    v["tags"] = []
                if tag not in v["tags"]:
                    v["tags"].append(tag)
                    self._save_metadata(metadata)
                    logging.info(f"已为版本 {version} 添加标签: {tag}")
                    return

        raise ValueError(f"版本不存在: {version}")

    def remove_tag(self, version: str, tag: str) -> None:
        """
        移除版本标签

        Args:
            version: 版本号
            tag: 标签名称
        """
        metadata = self._load_metadata()

        for v in metadata["versions"]:
            if v["version"] == version:
                if "tags" in v and tag in v["tags"]:
                    v["tags"].remove(tag)
                    self._save_metadata(metadata)
                    logging.info(f"已移除版本 {version} 的标签: {tag}")
                    return

        raise ValueError(f"版本或标签不存在")

    def delete_version(self, version: str) -> None:
        """
        删除版本

        Args:
            version: 版本号
        """
        metadata = self._load_metadata()

        for i, v in enumerate(metadata["versions"]):
            if v["version"] == version:
                # 删除文件
                file_path = self.version_dir / v["file_path"]
                if file_path.exists():
                    file_path.unlink()

                # 从元数据中移除
                metadata["versions"].pop(i)
                self._save_metadata(metadata)

                logging.info(f"已删除版本: {version}")
                return

        raise ValueError(f"版本不存在: {version}")

    def _load_metadata(self) -> Dict:
        """加载元数据"""
        if self.metadata_file.exists():
            with open(self.metadata_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {
                "prd_name": self.prd_name,
                "current_version": None,
                "versions": []
            }

    def _save_metadata(self, metadata: Dict) -> None:
        """保存元数据"""
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

    def _generate_version_number(self, metadata: Dict) -> str:
        """生成版本号"""
        versions = metadata.get("versions", [])
        if not versions:
            return "v1"

        # 获取最后一个版本号
        last_version = versions[-1]["version"]
        # 提取数字
        import re
        match = re.search(r'v(\d+)', last_version)
        if match:
            number = int(match.group(1)) + 1
            return f"v{number}"
        else:
            return f"v{len(versions) + 1}"

    def _calculate_changes(self, metadata: Dict, new_content: str) -> Dict:
        """计算变更统计"""
        versions = metadata.get("versions", [])
        if not versions:
            return {
                "added": new_content.count("\n") + 1,
                "deleted": 0,
                "modified": 0
            }

        # 获取上一个版本的内容
        last_version = versions[-1]
        try:
            old_content = self.get_version_content(last_version["version"])

            old_lines = old_content.splitlines()
            new_lines = new_content.splitlines()

            # 简单的行级差异统计
            added = len(new_lines) - len(old_lines)
            if added < 0:
                deleted = -added
                added = 0
            else:
                deleted = 0

            # 估算修改的行数
            modified = min(len(old_lines), len(new_lines)) // 10  # 简化估算

            return {
                "added": added,
                "deleted": deleted,
                "modified": modified
            }
        except Exception as e:
            logging.warning(f"计算变更统计失败: {e}")
            return {"added": 0, "deleted": 0, "modified": 0}
