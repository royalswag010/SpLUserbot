from pyrogram import Client, idle
from config import *
import time 
from Spoiled import BOT, SPL
from pyrogram.errors import FloodWait

def initiate():
    try:
        SPL.start()
        BOT.start()
        x = SPL.get_me()
        y = BOT.get_me()
    except FloodWait as e:
        time.sleep(e.value)
    try:
        SPL.join_chat("SpLBots")
        SPL.join_chat("Coding_bots")
        SPL.send_message(CHATS.LOG_GROUP_ID, "Ub started !")
        BOT.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    un = x.username
    bun = y.username
    print(f"@{bun} started successfully !")
    print(f"@{un} started successfully !")
    idle()

initiate()

