from pyrogram import Client, idle
from config import *

SPL = Client(":SPL-USERBOT:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=SECRETS.STRING_SESSION, plugins=dict(root="Spoiled/SpoiledPlugins"))
BOT = Client(":SPL-BOT:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=SECRETS.BOT_TOKEN)

def initiate():
    SPL.start()
    BOT.start()
    x = SPL.get_me()
    y = BOT.get_me()
    try:
        SPL.join_chat("SpLBots")
        SPL.join_chat("Coding_bots")
    except:
        pass
    un = x.username
    bun = y.username
    print(f"@{bun} started successfully !")
    print(f"@{un} started successfully !")
    idle()

initiate()

