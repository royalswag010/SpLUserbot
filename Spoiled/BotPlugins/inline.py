from pyrogram.types InlineQueryResultPhoto as IQRP
from Spoiled.SpoiledPlugins import build_help_markup, COMMANDS_HELP
from pyrogram import Client

URL = "https://telegra.ph/file/c363fbe2341ae115bd8c1.jpg"

ma = build_help_markup(COMMANDS_HELP)

ans = [IQRP(photo_url=URL, thumb_url=URL, title="Help", description="dhanush op", caption="Ja Na Lawde", reply_markup=ma)]

@Client.on_inline_query()
async def inl(_, i):
    try:
        text = i.query.lower()
        if text == "":
            await _.answer_inline_query(i.id, results=ans, cache_time=0)
    except Exception as e:
        print(e)
