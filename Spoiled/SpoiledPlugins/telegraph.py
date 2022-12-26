from pyrogram import Client, filters
from telegraph import upload_file
import os
from config import STUFF
from Spoiled.Utils import verify, eor
from . import add_command

hl = STUFF.COMMAND_HANDLER

@Client.on_message(filters.command(["telegraph"], hl))
async def get_link_private(client, message):
    x = await verify(client, message)
    if not x:
        return
    try:
        text = await eor(message, "Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 Downloading media... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

command = "Telegraph"
help = f"`» {hl}telegraph - gives telegraph link of replied media.`"

add_command(command, help)
