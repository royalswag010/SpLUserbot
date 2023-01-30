from pyrogram import Client, filters
from . import hl, eor, verify
import os
import time

@Client.on_message(filters.command("restart"))
async def reboot(_, m):
    if not await verify(_, m):
        return
    ok = await eor(m, "Rebooting, wait for 10sec..")
    time.sleep(3)
    await ok.delete()
    try:
        os.system(f"kill -9 {os.getpid()} && python3 yashu.py")
    except Exception as e:
        await m.reply(e)
