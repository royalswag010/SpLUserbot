from pyrogram import Client, filters
from . import eor, hl, verify, add_command, get_id
from Spoiled.Database.pm import *

@Client.on_message(filters.command("pmprotect", hl) & filters.me)
async def pmpro(_, m):
    x = await is_pm_on()
    try:
        tg = m.text.split()[1].lower()
    except:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if not tg in ["on", "off"]:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if tg == "on":
        if x:
            return await eor(m, "PM PROTECTION ALREADY ENABLED !")
        await toggle_pm()
        return await eor(m, "PM PROTECTION ENABLED !")
    if not x:
        return await eor(m, "PM PROTECTION ISN'T ENABLED !")
    await toggle_pm()
    return await eor(m, "PM PROTECTION DISABLED !")

@Client.on_message(filters.command(["approve", "disapprove"], hl) & filters.me)
async def appro_dis(_, m):
    if str(m.chat.id)[0] == "-":
        try:
            id = await get_id(_, m)
        except:
            return await eor(m, "REPLY OR GIVE ID !")
    else:
        id = m.chat.id
    tg = m.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await eor(m, "USER WASN'T APPROVED !")
        await disapprove(id)
        return await eor(m, "DISAPPROVED USER TO PM !")
    if x:
        return await eor(m, "USER ALREADY APPROVED !")
    await approve(id) 
    return await eor(m, "USER APPROVED TO PM !")


        
