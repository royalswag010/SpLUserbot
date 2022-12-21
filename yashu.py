from pyrogram import Client, idle
from config import *
from Spoiled import BOT, SPL

def initiate():
    SPL.start()
    BOT.start()
    x = SPL.get_me()
    y = BOT.get_me()
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

