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

    `args`の`/path/to/mcp-thisweek/server.py`を`mcp-thisweek`ディレクトリにある`server.py`スクリプトへの実際のパスに置き換えてください。また、`command`の`python`は、Python 3.10+インタプリタがシステムのPATHにない場合、フルパスに置き換える必要があるかもしれません。

    ```json
    {
      "mcpServers": {
        "mcp-thisweek": {
          "command": "python",
          "args": [
            "/path/to/mcp-thisweek/server.py"
          ]
        }
      }
    }
    ```

### Dockerを使用する

プロジェクトのルートディレクトリ（`Dockerfile`と`docker-compose.yml`がある場所）に移動し、以下を実行します:
```bash
docker-compose up -d --build
```
これにより、イメージが存在しない場合はビルドされ、コンテナがデタッチモードで起動します。

コンテナを停止および削除するには、次のコマンドを実行します。
```bash
docker-compose down
```

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
