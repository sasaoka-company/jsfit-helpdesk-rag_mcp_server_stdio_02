# Sample RAG MCP Server (stdio)

**PDF/DOCX ドキュメントを検索する RAG 機能を提供する MCP サーバー（標準入出力方式）**

このプロジェクトは、PDF/DOCX ドキュメントから関連情報を検索し、RAG（Retrieval-Augmented Generation）機能を提供する MCP サーバーです。
標準入出力を通じて MCP クライアントとの通信を行います。

## 機能

- **search_security**: 情報セキュリティ関連規定.pdf ドキュメントから質問に関連する情報を検索するツール
- **標準入出力方式**: MCP クライアントが直接プロセスを起動してアクセス
- **FAISS 検索**: 高速な類似性検索による関連文書の取得

## MCP クライアントからの接続

### 1. MCP クライアントからの利用

このサーバーは任意の MCP クライアントから利用できます。

**Claude Desktop から利用する場合の設定例：**

`claude_desktop_config.json`に以下のように設定：

```json
{
  "mcpServers": {
    "rag-server-stdio": {
      "command": "D:\\vscode_projects\\sample_rag_mcp_server_stdio\\.venv\\Scripts\\python.exe",
      "args": [
        "D:\\vscode_projects\\sample_rag_mcp_server_stdio\\rag_mcp_server_stdio.py"
      ]
    }
  }
}
```

**その他の MCP クライアントから利用する場合：**

- プロセス起動: 仮想環境の Python インタープリターで `rag_mcp_server_stdio.py` を実行
- コマンド: `D:\vscode_projects\sample_rag_mcp_server_stdio\.venv\Scripts\python.exe`
- 実行スクリプト: `rag_mcp_server_stdio.py`
- トランスポート: `stdio`
- 利用可能ツール: `search_security`

### 2. 利用方法

- **標準入出力方式**: MCP クライアントがサーバープロセスを起動し、stdin/stdout で通信
- **利用可能ツール**: `search_security`（情報セキュリティ関連規定.pdf の検索）
- **注意**: 相対パスは MCP クライアント側からの相対パスとして解決されます

## 開発セットアップ

### 前提条件

- Python 3.11 以上
- [uv](https://docs.astral.sh/uv/) (Python パッケージマネージャー)
- Ollama（`nomic-embed-text:latest`モデル）

### セットアップ手順

**依存関係のインストール**

```powershell
# プロジェクトルートへ移動
cd D:\vscode_projects\sample_rag_mcp_server_stdio

# uvを使用して依存関係をインストール
uv sync
```

## Ollama 設定

使用モデル: `nomic-embed-text:latest`

## テスト実行

```powershell
# uvを使用してテストを実行
uv run pytest tests/ -v
```

## ファイル構成

```
sample_rag_mcp_server_stdio/
├── rag_mcp_server_stdio.py   # メインサーバーファイル
├── rag_core.py               # RAG検索ロジック
├── logger.py                 # ログ設定
├── pyproject.toml            # プロジェクト設定・依存関係
├── uv.lock                   # 依存関係ロックファイル
├── docs/                     # ドキュメント格納
│   └── 情報セキュリティ関連規定.pdf
├── faiss_db/                 # FAISS検索インデックス
└── tests/                    # テストファイル
    └── test_rag_core.py
```
