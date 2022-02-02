import html
import os
import json
import importlib
import time
import re
import sys
import traceback
import MikeyBot.modules.sql.users_sql as sql

from sys import argv
from typing import Optional
from MikeyBot import (
    ALLOW_EXCL,
    CERT_PATH,
    LOGGER,
    OWNER_ID,
    PORT,
    TOKEN,
    URL,
    WEBHOOK,
    SUPPORT_CHAT,
    dispatcher,
    StartTime,
    client as telethn,
    updater,
    pbot)

from telethon import Button, events

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


PM_START_TEXT = """
────「 {} 」────
*Hey! {},*
* I am Mikey! An Anime Themed Super Duper Cool Advance Bot For Managing Your Groups .*
»»»»»—————🎩—————«««««
• *Uptime:* {}
• {} *users, Are My fans ✨----( 👀 )--------✨
»»»»»—————🎩—————«««««
➛ The Help Buttons That Are Below To Know How cool I am [.](pic?????) ××
"""
