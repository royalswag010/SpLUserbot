from Spoiled import SPL, BOT
from pyrogram import idle
from config import CHATS
from pyrogram.errors import FloodWait

import asyncio

async def initiate():
    try:
        await BOT.start()
        print("Bot started !")
    except FloodWait as e:
        print("Can't start bot, sleeping...")
        await asyncio.sleep(e.value)
    try:
        await SPL.start()
        print("Userbot started !")
    except FloodWait as e:
        print(Can't start userbot, sleeping...")
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
