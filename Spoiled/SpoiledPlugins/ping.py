from pyrogram import Client, filters 
from pyrogram.types import Message
from Spoiled.Utils import eor, verify
import time
from config import IMAGES, STUFF
from . import startTime

hl = STUFF.COMMAND_HANDLER

TEXT = """

💞Pong💞

   🔸️ {}
   🔹️ 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛 ~ {}

"""

def grt(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(filters.command("ping", hl))
async def alive_or_ping(_, m):
    x = await verify(_, m)
    if not x:
        return
    l = await _.get_me()
    st = time.time()
    ok = await eor(m, "`Checking...`")
    end = time.time()
    men = l.mention
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [𝚂𝙿𝙻](t.me/SpLBots)\n"
    await ok.delete()
    try:
        return await m.reply_photo(IMAGES.PING_IMG, caption=TEXT.format(pong, men))
    except:
        return await m.reply(TEXT.format(pong, men))
