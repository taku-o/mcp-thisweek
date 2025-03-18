# mcp-thisweek

今週の月曜日から金曜日の日付と、今日の日付を返すシンプルなMCP(Model Context Protocol)です。

## 機能

- 今週の日付（月曜日から金曜日）の取得 get_this_week_dates
- 今日の日付の取得 get_today_date

### 例

- 今週の月曜日から金曜日までの日付を教えてください。
- 今日の日付を教えてください。

## セットアップ

### download and setup mcp-thisweek
```
# download mcp-thisweek
git clone git@github.com:taku-o/mcp-thisweek.git

cd mcp-thisweek
pip install -r requirements.txt

# get fastmcp path
which fastmcp
```

### add mcp-thisweek MCP server to mcp.json, or claude_desktop_config.json

- replace "/path/to" with your path on example.

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

## ライセンス

MIT
