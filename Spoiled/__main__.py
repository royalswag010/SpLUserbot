from Spoiled import SPL, BOT
from pyrogram import idle
from config import CHATS
from pyrogram.errors import FloodWait

import asyncio

async def initiate():
    try:
        SPL.start()
        BOT.start()
        x = SPL.get_me()
        y = BOT.get_me()
    except FloodWait as e:
        await asyncio.sleep(e.value)
    try:
        await SPL.send_message(CHATS.LOG_GROUP_ID, "Ub started !")
        await BOT.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    print("Bot started !")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(initiate())
