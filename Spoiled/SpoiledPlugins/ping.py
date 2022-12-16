from pyrogram import Client, filters 
from pyrogram.types import Message
from Spoiled.Utils import eor
import time
from config import IMAGES, STUFF
from .afk import get_readable_time as grt
from . import startTime

hl = STUFF.COMMAND_HANDLER

TEXT = """

🌙.     *       🌏   *   .      
       .     🛰   
    🚀       *       ☄️ 
      . ┏━━━ 💫🦋🦋💫━━━┓
  
┃┃ ㅤ🧑‍💻ㅤㅤㅤρꪮꪀᧁ 
┃┃
┃┃ㅤㅤㅤ𝕊𝔼ℕ𝕊𝔼𝕀 : {}
┃┃
┃┃ㅤ✅ 𝐔𝐏𝐓𝐈𝐌𝐄 : {}
┃┃
┃┃ㅤ🚩{}𝐦𝐬
┃┃
ㅤ   ┗━━━ 💫🦋🦋💫━━━━┛
. *       🌏          *
               *       ☄️      
🌟 .    ☆    🌙

"""

@Client.on_message(filters.command("ping", hl))
async def alive_or_ping(_, m):
    l = await _.get_me()
    st = time.time()
    ok = await eor(m, "`Checking...`")
    end = time.time()
    men = l.mention
    pong = str((end-st)*1000)[0:5]
    grt = grt(int(time.time()-startTime))
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [𝚂𝙿𝙻](t.me/SpLBots)\n"
    await ok.delete()
    try:
        return await m.reply_photo(IMAGES.PING_IMG, caption=TEXT.format(men, grt, pong))
    except:
        return await m.reply(TEXT.format(men, grt, pong))
