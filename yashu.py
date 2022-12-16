from pyrogram import Client, idle
from config import *

SPL = Client(":SPL-USERBOT:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=SECRETS.STRING_SESSION, plugins=dict(root="Spoiled/SpoiledPlugins"))

def initiate():
    SPL.start()
    x = SPL.get_me()
    try:
        SPL.join_chat("Coding_bots")
    except:
        pass
    un = x.username
    print(f"@{un} started successfully !")
    idle()

initiate()

