from Spoiled.Database.protecc import *
from pyrogram import Client, filters
from . import hl, eor

@Client.on_message(filters.command(["autowaifu", "aw"], hl) & filters.group & filters.me)
async def waifer(_, m):
    if len(m.command) > 1:
        try:
            id = (m.text.split()[1])
        except:
            await eor(m, f"{hl}aw [chat_id]")
        if str(id)[0] != "-":
            return
    else:
        id = m.chat.id
    
    x = await is_waifu_chat(id)
    if x:
        return await eor(m, "Auto waifu already enabled in this chat !")
    await add_waifu_chat(id) 
    x = (await _.get_chat(id)).title
    await eor(m, f"{x} is added to waifu chats !")

@Client.on_message(filters.command(["rmautowaifu", "rmaw"], hl) & filters.group & filters.me)
async def rmwaifer(_, m):
    if len(m.command) > 1:
        try:
            id = (m.text.split()[1])
        except:
            await eor(m, f"{hl}rmaw [chat_id]")
        if str(id)[0] != "-":
            return
    else:
        id = m.chat.id
    
    x = await is_waifu_chat(id)
    if not x:
        return await eor(m, "Auto waifu isn't enabled in this chat !")
    await del_waifu_chat(id) 
    x = (await _.get_chat(id)).title
    await eor(m, f"{x} is removed from waifu chats !")

@Client.on_message(filters.command(["autohusbando", "ah"], hl) & filters.group & filters.me)
async def husbander(_, m):
    if len(m.command) > 1:
        try:
            id = (m.text.split()[1])
        except:
            await eor(m, f"{hl}ah [chat_id]")
        if str(id)[0] != "-":
            return
    else:
        id = m.chat.id
    
    x = await is_husbando_chat(id)
    if x:
        return await eor(m, "Auto husbando already enabled in this chat !")
    await add_husbando_chat(id) 
    x = (await _.get_chat(id)).title
    await eor(m, f"{x} is added to husbando chats !")

@Client.on_message(filters.command(["rmautohusbando", "rmah"], hl) & filters.group & filters.me)
async def rmhusbander(_, m):
    if len(m.command) > 1:
        try:
            id = (m.text.split()[1])
        except:
            await eor(m, f"{hl}rmah [chat_id]")
        if str(id)[0] != "-":
            return
    else:
        id = m.chat.id
    
    x = await is_husbando_chat(id)
    if not x:
        return await eor(m, "Auto husbando isn't enabled in this chat !")
    await del_husbando_chat(id) 
    x = (await _.get_chat(id)).title
    await eor(m, f"{x} is removed from husbando chats !")

        
