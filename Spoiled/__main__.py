from Spoiled import SPL, BOT
from pyrogram import idle
from config import CHATS
from pyrogram.errors import FloodWait
import importlib
from Spoiled.SpoiledPlugins import SPL_MODULES
from Spoiled.BotPlugins import BOT_MODULES

import asyncio

async def initiate():
    try:
        await BOT.start()
        print("Bot started !")
        await BOT.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except FloodWait as e:
        print("Can't start bot, sleeping...")
        await asyncio.sleep(e.value)
    for all_module in SPL_MODULES:
        importlib.import_module("Spoiled.SpoiledPlugins" + all_module)
        print(f"Successfully Imported {all_module} 💭")
    for all_module in BOT_MODULES:
        importlib.import_module("Spoiled.BotPlugins" + all_module)
        print(f"Successfully Imported {all_module} 💭")
    try:
        await SPL.start()
        print("Userbot started !")
        await BOT.send_message(CHATS.LOG_GROUP_ID, "Userbot started !")
    except FloodWait as e:
        print("Can't start userbot, sleeping...")
        await asyncio.sleep(e.value)
    print("Bot started !")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(initiate())
