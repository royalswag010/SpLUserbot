from pyrogram.types import InlineQueryResultPhoto as IQRP
from Spoiled.SpoiledPlugins import build_help_markup, COMMANDS_HELP
from pyrogram import Client as BOT
from config import IMAGES

if IMAGES.HELP_IMG:
    URL = IMAGES.HELP_IMG
else:
    URL = "https://telegra.ph/file/9f22901d5894fd97b69dc.jpg"

ma = build_help_markup(COMMANDS_HELP)

ans = [IQRP(photo_url=URL, thumb_url=URL, title="Help", description="Help Module [SPL-UB]", caption="Select from below buttons !", reply_markup=ma)]

@BOT.on_inline_query()
async def inl(_, i):
    text = i.query.lower()
    try:
        if text == "inline_help":
            await _.answer_inline_query(i.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)
