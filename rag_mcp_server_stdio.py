from fastmcp import FastMCP
import rag_core
import asyncio  # 後でクライアント用に必要になります

from logger import get_logger

# ロガー設定
logger = get_logger(__name__)

# サーバーをインスタンス化し、名前を付けます
mcp = FastMCP(name="security-stdio")

logger.info("FastMCPサーバーオブジェクトが作成されました。")


@mcp.tool(
    name="search_security",
    description="情報セキュリティ関連規定.pdfドキュメントから質問に関連する情報を検索します。",
)
def search_security(prompt: str) -> str:
    logger.info(f"[1] 検索クエリ: {prompt}")

    results: list[str] = rag_core.search(prompt)

    logger.info(f"[2] 検索結果: {results}")

    return "\n\n".join(results)


if __name__ == "__main__":
    logger.info("--- __main__を介してFastMCPサーバーを開始 ---")
    # サーバーが起動し、デフォルトでstdioトランスポートを使用
    mcp.run()
