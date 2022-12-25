from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev 
from Spoiled.Addons.emotes import *
from . import hl, eor, verify, add_command

@End.on_message(filters.command("emojify", hl))
async def doli(ailika, jhulika: Dev):
        if not await verify(ailika, jhulika):
            return
        txt = jhulika.text
        m = jhulika
        if len(jhulika.command) != 2:
            return await eor(m, f"Try: < {hl}emojify Crystal >")
        txt = txt.split(None, 1)[1]
        final = ""
        for a in txt:
            a = a.lower()
            a = str(a)
            if a in END_TEXT:
                letter = END_EMOJI[END_TEXT.index(a)]
                final += letter
            else:
                final += a
        await eor(m, final)

@End.on_message(filters.command("crystal", hl))
async def crystal(ailika, jhulika: Dev):
    if not await verify(ailika, jhulika):
        return
    m = jhulika
    txt = jhulika.text
    if len(jhulika.command)!= 3:
        return await eor(m, f"Try: < {hl}crystal ✨ doli >")
    emoji = txt.split(None, 2)[1]
    text = txt.split(None, 2)[2]
    final = ""
    for a in text:
        a = a.lower()
        a = str(a)
        if a in END_TEXT:
            letter = END_CJ[END_TEXT.index(a)].format(cj=emoji)
            final += letter
        else:
            final += a
    await eor(m, final)

command = "Emojify"
help = f"• {hl}crystal - try \n\n• {hl}emojify - try"

add_command(command, help)
