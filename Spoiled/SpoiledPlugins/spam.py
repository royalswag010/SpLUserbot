from . import hl, eor, verify, get_reply_and_args
from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("spam", hl))
async def spam_func(_, m):
    x = await verify(_, m)
    if not x:
        return
    a, b = await get_reply_and_args(m)
    if not a and not b:
        return await eor(m, f"{hl}spam [either reply or give some text]")
    if not b:
        return await eor(m, f"{hl}spam [count] [text]")
