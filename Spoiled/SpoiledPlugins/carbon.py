from pyrogram import Client, filters
from io import BytesIO
from aiohttp import ClientSession
from . import hl, eor, verify, add_command

@Client.on_message(filters.command("carbon", hl))
async def carbon_func(_, message):
    x = await verify(_, message)
    if not x:
        return
    if not message.reply_to_message:
        return await eor(message, "`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await eor(message, "`Reply to a text message to make carbon.`")
    m = await eor(message, "`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await _.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()

aiosession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

command = "Carbon"
help = f"`» {hl}carbon [reply to a text]`"

add_command(command, help)
