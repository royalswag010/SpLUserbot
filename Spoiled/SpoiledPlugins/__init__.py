import time
from config import STUFF
from Spoiled.Utils import *
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

hl = STUFF.COMMAND_HANDLER

startTime = time.time()

COMMANDS_HELP = {}

def add_command(command, help):
    global COMMANDS_HELP
    COMMANDS_HELP[command] = help

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def build_help_markup(set):
    le = len(set)
    rows = le // 3
    rows += 1
    rem = le % 3
    buttons = []
    y = []
    a = 0
    filled = 0
    for each in set:
        x = IKB(each, callback_data=each.lower())
        y.append(x)
        a += 1
        if a == 3:
            buttons.append(y)
            filled += 1
            a = 0
            y = []
        if filled == (rows - 1):
            if list(set).index(each) == (le - 1):
                buttons.append(y)
                y = []
    final = IKM(buttons)
    return final
                
def get_uptime(x):
    z = get_readable_time(int(x-startTime))
    return z
