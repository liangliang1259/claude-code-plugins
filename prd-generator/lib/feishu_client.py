"""
Feishu Client - 飞书API客户端
"""

import json
import logging
import requests
from pathlib import Path
from typing import Dict, Optional
from .utils import get_plugin_root


class FeishuClient:
    """飞书API客户端"""

    def __init__(self, app_id: Optional[str] = None, app_secret: Optional[str] = None):
        """
        初始化飞书客户端

        Args:
            app_id: 飞书应用ID
            app_secret: 飞书应用密钥
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.api_base_url = "https://open.feishu.cn/open-apis"
        self.access_token = None

        # 如果没有提供凭据，尝试从配置文件加载
        if not self.app_id or not self.app_secret:
            self._load_config()

    def _load_config(self) -> None:
        """从配置文件加载凭据"""
        try:
            plugin_root = get_plugin_root()
            config_path = plugin_root / "config" / "feishu_config.json"

            if config_path.exists():
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.app_id = config.get("app_id")
                    self.app_secret = config.get("app_secret")
                    self.api_base_url = config.get("api_base_url", self.api_base_url)
                    logging.info("已加载飞书配置")
            else:
                logging.warning("飞书配置文件不存在")
        except Exception as e:
            logging.error(f"加载飞书配置失败: {e}")

    def authenticate(self) -> str:
        """
        获取访问令牌

        Returns:
            str: 访问令牌

        Raises:
            Exception: 认证失败
        """
        if not self.app_id or not self.app_secret:
            raise ValueError("缺少飞书应用凭据")

        url = f"{self.api_base_url}/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()

            data = response.json()
            if data.get("code") != 0:
                raise Exception(f"认证失败: {data.get('msg')}")

            self.access_token = data.get("tenant_access_token")
            logging.info("飞书认证成功")
            return self.access_token

        except requests.exceptions.RequestException as e:
            logging.error(f"飞书认证请求失败: {e}")
            raise Exception(f"飞书认证失败: {e}")

    def get_document(self, document_id: str) -> Dict:
        """
        获取飞书文档内容

        Args:
            document_id: 文档ID

        Returns:
            Dict: 文档内容

        Raises:
            Exception: 获取文档失败
        """
        # 确保已认证
        if not self.access_token:
            self.authenticate()

        url = f"{self.api_base_url}/docx/v1/documents/{document_id}/raw_content"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            data = response.json()
            if data.get("code") != 0:
                raise Exception(f"获取文档失败: {data.get('msg')}")

            logging.info(f"成功获取飞书文档: {document_id}")
            return data.get("data", {})

        except requests.exceptions.RequestException as e:
            logging.error(f"获取飞书文档请求失败: {e}")
            raise Exception(f"获取飞书文档失败: {e}")

    def parse_document(self, document_data: Dict) -> str:
        """
        解析飞书文档为Markdown格式

        Args:
            document_data: 文档数据

        Returns:
            str: Markdown格式的文档内容
        """
        try:
            # 获取文档内容
            content = document_data.get("content", "")

            # 飞书文档通常返回的是富文本格式
            # 这里需要根据实际返回格式进行解析
            # 简化处理：直接返回文本内容

            if isinstance(content, str):
                return content

            # 如果是结构化数据，需要递归解析
            # 这里提供基础实现
            return self._parse_blocks(content)

        except Exception as e:
            logging.error(f"解析飞书文档失败: {e}")
            raise

    def _parse_blocks(self, blocks) -> str:
        """
        解析飞书文档块

        Args:
            blocks: 文档块列表

        Returns:
            str: Markdown文本
        """
        if not blocks:
            return ""

        markdown_lines = []

        for block in blocks:
            block_type = block.get("block_type")

            if block_type == "heading1":
                text = self._extract_text(block)
                markdown_lines.append(f"# {text}\n")
            elif block_type == "heading2":
                text = self._extract_text(block)
                markdown_lines.append(f"## {text}\n")
            elif block_type == "heading3":
                text = self._extract_text(block)
                markdown_lines.append(f"### {text}\n")
            elif block_type == "text":
                text = self._extract_text(block)
                markdown_lines.append(f"{text}\n")
            elif block_type == "bullet":
                text = self._extract_text(block)
                markdown_lines.append(f"- {text}\n")
            elif block_type == "ordered":
                text = self._extract_text(block)
                markdown_lines.append(f"1. {text}\n")
            elif block_type == "code":
                text = self._extract_text(block)
                language = block.get("code", {}).get("language", "")
                markdown_lines.append(f"```{language}\n{text}\n```\n")
            elif block_type == "quote":
                text = self._extract_text(block)
                markdown_lines.append(f"> {text}\n")

        return "\n".join(markdown_lines)

    def _extract_text(self, block: Dict) -> str:
        """
        从块中提取文本

        Args:
            block: 文档块

        Returns:
            str: 文本内容
        """
        # 根据飞书API返回的实际结构提取文本
        # 这里提供基础实现
        text_elements = block.get("text", {}).get("elements", [])

        if not text_elements:
            return ""

        texts = []
        for element in text_elements:
            if "text_run" in element:
                texts.append(element["text_run"].get("content", ""))

        return "".join(texts)

    def extract_document_id(self, url: str) -> str:
        """
        从飞书文档URL提取文档ID

        Args:
            url: 飞书文档URL

        Returns:
            str: 文档ID

        Examples:
            >>> client = FeishuClient()
            >>> client.extract_document_id("https://example.feishu.cn/docx/abc123")
            'abc123'
        """
        import re

        # 匹配飞书文档URL模式
        patterns = [
            r'/docx/([a-zA-Z0-9_-]+)',
            r'/docs/([a-zA-Z0-9_-]+)',
            r'/doc/([a-zA-Z0-9_-]+)',
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        # 如果不是URL，可能直接是文档ID
        if re.match(r'^[a-zA-Z0-9_-]+$', url):
            return url

        raise ValueError(f"无法从URL提取文档ID: {url}")

    def test_connection(self) -> bool:
        """
        测试飞书连接

        Returns:
            bool: 连接是否成功
        """
        try:
            self.authenticate()
            return True
        except Exception as e:
            logging.error(f"飞书连接测试失败: {e}")
            return False

    @staticmethod
    def save_config(app_id: str, app_secret: str, api_base_url: Optional[str] = None) -> None:
        """
        保存飞书配置

        Args:
            app_id: 应用ID
            app_secret: 应用密钥
            api_base_url: API基础URL（可选）
        """
        plugin_root = get_plugin_root()
        config_dir = plugin_root / "config"
        config_dir.mkdir(exist_ok=True)

        config_path = config_dir / "feishu_config.json"

        config = {
            "app_id": app_id,
            "app_secret": app_secret,
            "api_base_url": api_base_url or "https://open.feishu.cn/open-apis"
        }

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        logging.info(f"飞书配置已保存: {config_path}")
