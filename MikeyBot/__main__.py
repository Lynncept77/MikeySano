import html
import os
import json
import importlib
import time
import re
import sys
import traceback
import MikeyBot.modules.sql.users_sql as sql

from MikeyBot.events import register
from MikeyBot.modules import ALL_MODULES
from MikeyBot.modules.helper_funcs.chat_status import is_user_admin
from MikeyBot.modules.helper_funcs.alternate import typing_action
from MikeyBot.modules.helper_funcs.misc import paginate_modules
from MikeyBot.modules.disable import DisableAbleCommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)

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
* 卐 I am Mikey! An Anime Themed Super Duper Cool Advance Bot For Managing Your Groups 卍.*
»»»»»—————🎩—————«««««
• *Uptime:* {}
• {} *users, Are My fans ✨----( 👀 )--------✨
»»»»»—————🎩—————«««««
➛ 卐  The Help Buttons That Are Below To Know How cool I am [.](pic?????) ×× 卍
"""
