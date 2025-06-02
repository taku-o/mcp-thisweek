#!/usr/bin/env python3
import logging
from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta, MO
from fastmcp import FastMCP
from tzlocal import get_localzone

# ロガーの設定
logging.basicConfig(
    #filename='debug.log',  # Log to a local file, commented out
    #level=logging.DEBUG,
    level=logging.CRITICAL + 1,  # Disable logging by setting level above CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create an MCP server
mcp = FastMCP("mcp-thisweek")

@mcp.tool()
def get_this_week_dates() -> list[str]:
    """今週の月曜日から金曜日までの日付を返す"""
    logging.debug("get_this_week_dates が呼び出されました")
    local_tz = get_localzone()
    today = datetime.now(local_tz)
    
    # 今週の月曜日を取得
    monday = today + relativedelta(weekday=MO(-1))
    
    # 月曜日から金曜日までの日付をリスト化
    dates = []
    for i in range(5):  # 月曜から金曜まで
        current_date = monday + timedelta(days=i)
        dates.append(current_date.strftime("%m/%d"))
    
    logging.debug(f"取得した日付: {dates}")
    return dates

@mcp.tool()
def get_today_date() -> str:
    """今日の日付を返す"""
    logging.debug("get_today_date が呼び出されました")
    local_tz = get_localzone()
    today = datetime.now(local_tz)
    result = today.strftime("%m/%d")
    logging.debug(f"今日の日付: {result}")
    return result

if __name__ == "__main__":
    # Start the server
    # The following line assumes `mcp` is the FastMCP instance.
    # Adjust if your server instance has a different name or needs specific startup arguments.
    mcp.run()
