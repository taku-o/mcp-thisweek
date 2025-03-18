
次の仕様で、mcp-thisweekフォルダ以下にプログラムを生成してください。

# 概要
今週の日付と、今日の日付を返すMCP。

# 要件
* 大きな機能は2つ。
    * 今週の月曜日から金曜日までの日付を返す。日付のフォーマットはMM/DD。
    * 今日の日付を返す。
* MCPサーバーとしてcursorから使えるようにする。
* python製。

# インストール
pip install -r requirements.txt

# 動かし方
* cursorにmcpサーバーとして設定する場合、どう書けば良い？これでいい？
{
  "mcpServers": {
    "mcp-thisweek": {
      "command": "/Users/taku.omi/.pyenv/shims/python3",
      "args": [
        "/Users/taku.omi/Documents/workspaces/mcp-thisweek/server.py"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}

# コマンド実行実行例
* https://github.com/jlowin/fastmcp
fastmcp dev /Users/taku.omi/Documents/workspaces/mcp-thisweek/server.py
/Users/taku.omi/.pyenv/shims/python3 /Users/taku.omi/Documents/workspaces/mcp-thisweek/server.py


uv venv
uv pip install fastmcp
uv init
uv add -r requirements.txt 

fastmcp run server.py