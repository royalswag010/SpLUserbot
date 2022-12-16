from pyrogram import Client, idle
from config import *
import asyncio

SPL = Client(":SPL-USERBOT:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=SECRETS.STRING_SESSION)

async def initiate():
    await SPL.start()
    x = await SPL.get_me()
    try:
        await SPL.join_chat("Coding_bots")
    except:
        pass
    un = x.username
    print(f"@{un} started successfully !")
    await idle()

asyncio.run(initiate())
