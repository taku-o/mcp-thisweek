# mcp-thisweek

今週の月曜日から金曜日の日付と、今日の日付を返すシンプルなMCP(Model Context Protocol)です。

## 機能

- 今週の日付（月曜日から金曜日）の取得 get_this_week_dates
- 今日の日付の取得 get_today_date

## 使い方

```
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

## 開発環境のセットアップ

```
brew install uv
uv venv
uv pip install fastmcp
uv add -r requirements.txt 
```

```
fastmcp dev server.py
fastmcp run server.py
```

## ライセンス

MIT
