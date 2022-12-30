from pyrogram import Client, filters
from . import eor, verify, hl, get_uptime
from config import STUFF, IMAGES
import time

if not STUFF.ALIVE_EMOJI:
    EMOTES = "🍁"
else:
    EMOTES = STUFF.ALIVE_EMOJI

if not STUFF.ALIVE_TEXT:
    text = "I'm Alive !"
else:
    text = STUFF.ALIVE_TEXT

if IMAGES.ALIVE_IMG:
    IMG = IMAGES.ALIVE_IMG
else:
    IMG = "https://telegra.ph/file/7c71bb8e52ea14794561e.jpg"


form = """

{}

┏━━━━━━✦❘༻༺❘✦━━━━━━┓
┃{} 𝐀𝐋𝐏𝐇𝐀 𝐁𝐎𝐓 : V1
┃{} 𝐔𝐏𝐓𝐈𝐌𝐄 : {}
┃{} 𝐎𝐖𝐍𝐄𝐑 : {}
┗━━━━━━✦❘༻༺❘✦━━━━━━┛
┏━━━━━━✦❘༻༺❘✦━━━━━━┓
┃ ⁭⁫     {}📡 𝐏𝐈𝐍𝐆 : {} ms
┗━━━━━━✦❘༻༺❘✦━━━━━━┛
        ↠━━━━━☬◆☬━━━━━↞

"""

@Client.on_message(filters.command("alive", hl))
async def aliver(_, m):
    x = await verify(_, m)
    if not x:
        return
    x = time.time()
    ok = await eor(m, "`checking...`")
    x = str((time.time()-x)*1000)
    y = x.index(".")
    x = f"`{x[0:y+2]}`"
    upt = get_uptime(time.time())
    men = (await _.get_me()).mention
    await ok.delete()
    await m.reply_photo(IMG, caption=form.format(text, upt, men, x))
