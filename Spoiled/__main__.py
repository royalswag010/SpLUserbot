from Spoiled import SPL, BOT
from pyrogram import idle
from config import CHATS

import asyncio

async def initiate():
    await SPL.start()
    await BOT.start()
    try:
        await SPL.send_message(CHATS.LOG_GROUP_ID, "Ub started !")
        await BOT.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    print("Bot started !")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(initiate())
