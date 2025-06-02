# mcp-thisweek

今週の月曜日から金曜日までの日付と今日の日付を提供するシンプルなMCP（Model Context Protocol）サーバーです。

## 機能

-   `get_this_week_dates`: 今週の月曜日から金曜日までの日付のリストを返します。
-   `get_today_date`: 今日の日付を返します。

### 例

-   "今週の月曜日から金曜日までの日付を教えてください"
-   "今日は何日ですか"

## セットアップ

pipとPythonを使用するか、Dockerを使用して`mcp-thisweek`をセットアップして実行できます。

### pipとPythonを使用する

1.  **リポジトリをクローンします:**
    ```bash
    git clone https://github.com/taku-o/mcp-thisweek.git
    cd mcp-thisweek
    ```

2.  **依存関係をインストールします:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **MCPクライアントを設定します:**
    `mcp-thisweek`をMCPクライアントの設定ファイル（例:`mcp.json`または`claude_desktop_config.json`）に追加します。

    `command`の`/path/to/fastmcp`を使用する`fastmcp`のパスに、`args`の`/path/to/mcp-thisweek/server.py`を`mcp-thisweek`ディレクトリにある`server.py`スクリプトへの実際のパスに置き換えてください。

    ```json
    {
      "mcpServers": {
        "mcp-thisweek": {
          "command": "/path/to/fastmcp",
          "args": [
            "run",
            "/path/to/mcp-thisweek/server.py"
          ]
        }
      }
    }
    ```

### Dockerを使用する

1.  **Dockerイメージをビルドします:**
    プロジェクトのルートディレクトリ（`Dockerfile`がある場所）に移動し、以下を実行します:
    ```bash
    docker build -t mcp-thisweek .
    ```

2.  **Dockerコンテナを実行します:**
    ```bash
    docker run -d --name mcp-thisweek-container mcp-thisweek
    ```
    これにより、コンテナがデタッチモードで実行されます。

3.  **MCPクライアントを設定します（Docker用）:**
    Dockerを使用する場合、`fastmcp`はコンテナ内で実行されているサーバーと通信する必要があります。`fastmcp`は通常、ローカルコマンド実行を使用します。これをDockerで機能させるには、ラッパースクリプトが必要になるか、`fastmcp`がコンテナに`docker exec`する必要がある場合や、`fastmcp`自体がDockerネットワーク内で実行される場合に、`fastmcp`がサーバーを呼び出す方法を調整する必要がある場合があります。

    `fastmcp`が使用される一般的な方法は、`fastmcp`が実行できるコマンドを指定することです。`fastmcp`がホスト上で実行されている場合、`docker exec`なしではDockerコンテナ内のPythonスクリプトを直接実行できません。

    Docker化された`mcp-server`の場合、`mcp.json`の`command`は通常`docker exec -i mcp-thisweek-container python /app/server.py`のようになります。これは、`fastmcp`がホスト上で実行されており、コンテナ名が`mcp-thisweek-container`であることを前提としています。

    Docker用のJSON設定は次のようになります:
    ```json
    {
      "mcpServers": {
        "mcp-thisweek": {
          "command": "docker",
          "args": [
            "exec",
            "-i",
            "mcp-thisweek-container",
            "python",
            "/app/server.py"
          ]
        }
      }
    }
    ```
    コンテナ`mcp-thisweek-container`が実行されていることを確認してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
