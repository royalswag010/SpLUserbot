from pyrogram import Client, filters
from . import verify, hl, eor
import time
from Spoiled import BOT

un = None
id = None

@Client.on_message(filters.command("help", hl))
async def helper_func(_, m):
    global un, id
    x = await verify(_, m)
    if not x:
        return
    ok = await eor(m, "💎")
    try:
        if not un:
            un = (await BOT.get_me()).username
        if not id:
            id = (await _.get_me()).id
        nice = await _.get_inline_bot_results(bot=un, query="inline_help")
        try:
            await ok.delete()
            await m.delete()
        except:
            pass
        await _.send_inline_bot_result(m.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await eor(m, e)
    
