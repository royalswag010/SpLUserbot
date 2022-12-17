from Spoiled.Database.protecc import *
from pyrogram import Client, filters
from . import hl

@Client.on_message(filters.command(["autowaifu", "aw"], hl) & filters.group & filters.me)
async def waifer(_, m):
    
