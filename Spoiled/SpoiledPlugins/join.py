from . import hl, eor, verify
from pyrogram import Client, filters

@Client.on_message(filters.command("join", hl))
async def joiner(_, m):
    if not await verify(_, m):
        return
    try:
        await _.join_chat(m.text.split()[1])
        await eor(m, "`Joined !`")
    except Exception as e:
        await eor(m, e)
