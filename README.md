**RAG 機能を提供する MCP サーバー（標準入出力方式）その２**

このプロジェクトは、PDF/DOCX ドキュメントから関連情報を検索し、RAG（Retrieval-Augmented Generation）機能を提供する MCP サーバーです。
標準入出力を通じて MCP クライアントとの通信を行います。

# 1. 機能

- **標準入出力方式**: MCP クライアントが直接プロセスを起動してアクセス
- **ベクトル DB 検索**: 高速な類似性検索による関連文書の取得

# 2. 前提条件

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/) (Python パッケージマネージャー)
- モデル実行環境：Ollama
- Embedding モデル：`nomic-embed-text:latest`
- 仮想環境（`.venv`）が作成されていること

# 3. MCP クライアントからの接続

- コマンド: `（プロジェクトルート）\.venv\Scripts\python.exe`
- 実行スクリプト: `rag_mcp_server_stdio_02.py`
- トランスポート: `stdio`

## （参考）Claude Desktop から利用する場合の設定例：

`claude_desktop_config.json`に以下のように設定：

```json
{
  "mcpServers": {
    "mcp-server-stdio-02": {
      "command": "D:\\github_projects\\jsfit-helpdesk-rag_mcp_server_stdio_02\\.venv\\Scripts\\python.exe",
      "args": [
        "D:\\github_projects\\jsfit-helpdesk-rag_mcp_server_stdio_02\\rag_mcp_server_stdio_02.py"
      ]
    }
  }
}
```

# 4. 開発環境セットアップ

## 4-1. Git 設定

以下コマンドにより、チェックアウト時、コミット時に改行コードを変更しないようにします。（`.gitattributes` のままになります）

```powershell
git config --global core.autocrlf false
```

## 4-2. 依存関係のインストール

以下コマンドにより、`pyproject.toml`で定義されているライブラリをインストールします。

```powershell
uv sync
```

# 5. MCP サーバ起動

明示的な起動は不要です。MCP クライアントから接続されることで起動します。

# 6. テスト実行

```powershell
uv run pytest tests/ -v
```
