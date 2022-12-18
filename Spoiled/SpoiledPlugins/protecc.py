from Spoiled.Database.protecc import *
from pyrogram import Client, filters
from . import hl, eor, verify
from .watchers import protecc_watcher
import requests
from bs4 import BeautifulSoup
import os
import time

husbando_id = 1964681186

waifu_id = 1733263647

@Client.on_message(filters.command(["autowaifu", "aw"], hl) & filters.group)
async def waifer(_, m):
    x = await verify(_, m)
    if not x:
        return
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

@Client.on_message(filters.command(["rmautowaifu", "rmaw"], hl) & filters.group)
async def rmwaifer(_, m):
    x = await verify(_, m)
    if not x:
        return
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

@Client.on_message(filters.command(["autohusbando", "ah"], hl) & filters.group)
async def husbander(_, m):
    x = await verify(_, m)
    if not x:
        return
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

@Client.on_message(filters.command(["rmautohusbando", "rmah"], hl) & filters.group)
async def rmhusbander(_, m):
    x = await verify(_, m)
    if not x:
        return
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

@Client.on_message(filters.group, group=protecc_watcher)
async def cwf(_, m):
    bots = [husbando_id, waifu_id]
    id = m.from_user.id
    if not id in bots:
        return
    x = await is_waifu_chat(m.chat.id)
    y = await is_husbando_chat(m.chat.id)
    if not x and not y:
        return
    if id == husbando_id:
        if not y:
            return
    elif id == waifu_id:
        if not x:
            return
    if m.photo:
        dl = await m.download()
        file = {"encoded_image": (dl, open(dl, "rb"))}
        grs = requests.post(
               "https://www.google.com/searchbyimage/upload",
                files=file,
                allow_redirects=False,
            )
        loc = grs.headers.get("Location")
        response = requests.get(
            loc,
            headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
                    },
                )
        qtt = BeautifulSoup(response.text, "html.parser")
        div = qtt.find_all("div", {"class": "r5a77d"})[0]
        alls = div.find("a")
        text = alls.text
        try:
            if "cg" in text:
                return
            if "fictional character" in text:
                return
        except:
            pass
        ok = await _.send_message(m.chat.id, f"/protecc {text}")
        time.sleep(5)
        await ok.delete()
        os.remove(dl)
    
    
    
