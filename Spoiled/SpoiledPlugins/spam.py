from . import hl, eor, verify, get_reply_and_args
from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("spam", hl))
async def spam_func(_, m):
    reply = m.reply_to_message
    x = await verify(_, m)
    if not x:
        return
    a, b = await get_reply_and_args(m)
    if not a and not b:
        return await eor(m, f"{hl}spam [either reply or give some text]")
    if not b:
        return await eor(m, f"{hl}spam [count] [text]")
    if not a:
        try:
            count = int(b.split()[0])
        except:
            return await eor(m, f"{hl}spam [count] [text]")
        try:
            txt = b.split(None, 1)[1]
        except:
            return await eor(m, f"{hl}spam [count] [text]")
        for u in range(0, count):
            await _.send_message(m.chat.id, txt)
        return
    if a[-7:] == "caption":
        caption = True
        txt = reply.caption
    else:
        caption = False
    type = a.split("-")[0]
    try:
        count = int(b[0])
    except:
        return await eor(m, f"{hl}spam [count] [text]")
    if not caption:
        try:
            txt = b.split(None, 1)[1]
            caption = True
        except:
            pass
    blank = ""
    if type == "photo":
        id = reply.photo.file_id
        for u in range(0, count):
            await _.send_photo(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "video":
        id = reply.video.file_id
        for u in range(0, count):
            await _.send_video(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "document":
        id = reply.document.file_id
        for u in range(0, count):
            await _.send_document(m.chat.id, id, caption=f"{txt if caption else blank}", force_document=True)
    elif type == "animation":
        id = reply.animation.file_id
        for u in range(0, count):
            await _.send_animation(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "voice":
        id = reply.voice.file_id
        for u in range(0, count):
            await _.send_voice(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "audio":
        id = reply.audio.file_id
        for u in range(0, count):
            await _.send_audio(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "text":
        id = reply.text
        for u in range(0, count):
            await _.send_message(m.chat.id, id)
    elif type == "sticker":
        id = reply.sticker.file_id
        for u in range(0, count):
            await _.send_sticker(m.chat.id, id)

