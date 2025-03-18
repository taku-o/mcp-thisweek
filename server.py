#!/usr/bin/env python3
import logging
from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta, MO
from fastmcp import FastMCP

# ロガーの設定
logging.basicConfig(
    filename='/Users/taku.omi/Documents/workspaces/mcp-thisweek/debug.log',
    #level=logging.DEBUG,
    level=logging.CRITICAL + 1,  # CRITICALより上のレベルを設定することでログ出力を無効化
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create an MCP server
mcp = FastMCP("mcp-thisweek")

@mcp.tool()
def get_this_week_dates() -> list[str]:
    """今週の月曜日から金曜日までの日付を返す"""
    logging.debug("get_this_week_dates が呼び出されました")
    jst = pytz.timezone('Asia/Tokyo')
    today = datetime.now(jst)
    
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
    jst = pytz.timezone('Asia/Tokyo')
    today = datetime.now(jst)
    result = today.strftime("%m/%d")
    logging.debug(f"今日の日付: {result}")
    return result
