from pyrogram.types import InlineQueryResultPhoto as IQRP
from Spoiled.SpoiledPlugins import build_help_markup, COMMANDS_HELP
from Spoiled import BOT

URL = "https://telegra.ph/file/c363fbe2341ae115bd8c1.jpg"

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
