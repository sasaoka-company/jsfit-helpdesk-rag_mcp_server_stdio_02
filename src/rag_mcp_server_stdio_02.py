import sys
import os

from fastmcp import FastMCP
from src.rag_core import search
from src.config import (
    TOOL_NAME,
    TOOL_DESCRIPTION,
)

from logger import get_logger

# ロガー設定
logger = get_logger(__name__)

logger.info("=== SERVER STARTED ===")
logger.info("sys.executable: %s", sys.executable)
logger.info("sys.prefix: %s", sys.prefix)
logger.info("PATH: %s", os.environ.get("PATH"))

# サーバーをインスタンス化し、名前を付けます
mcp = FastMCP(name="mcp-server-stdio-02")

logger.info("FastMCPサーバーオブジェクト（標準入出力）が作成されました。")


@mcp.tool(
    name=TOOL_NAME,
    description=TOOL_DESCRIPTION,
)
def search_snowfall(prompt: str) -> str:
    logger.info(f"[1] 検索クエリ: {prompt}")

    results: list[str] = search(prompt)

    logger.info(f"[2] 検索結果: {results}")

    return "\n\n".join(results)


if __name__ == "__main__":
    logger.info("--- __main__を介してFastMCPサーバーを開始 ---")
    # サーバーが起動し、デフォルトでstdioトランスポートを使用
    mcp.run()
