from pyrogram import Client, filters
from . import hl, verify, eor, get_id, add_command
from Spoiled.Database.raid import *
from Spoiled.Addons.raid import *
import random 
from .watchers import raid_watcher

@Client.on_message(filters.command(["replyraid", "dreplyraid"], hl))
async def add_or_del_raid(_, m):
    if not await verify(_, m):
        return
    try:
        id = await get_id(_, m)
    except:
        return await eor(m, f"<i>{hl}replyraid or {hl}dreplyraid [Reply | Username | Id]</id>")
    sudo = await is_raid(id)
    if m.text.split()[0][1].lower() == "d":
        if not sudo:
            return await eor(m, f"<i>This user isn't in raid list..!</i>")
        await del_raid(id)
        return await eor(m, f"<i>Raid removed for the user {id} .</i>")
    if sudo:
        return await eor(m, f"<i>{id} is already in raid list..!</i>")
    await add_raid(id)
    return await eor(m, f"<i>{id} is added to raid list...!</i>")

@Client.on_message(filters.command("raid", hl) & filters.group)
async def raider_func(_, m):
    usage = f"{hl}raid [count] [reply or username]"
    if not await verify(_, m):
        return
    try:
        if m.reply_to_message:
            count = int(m.text.split()[1])
            id = m.reply_to_message.from_user.id
        else:
            count = int(m.text.split()[1])
            txt = m.text.split()[2]
            try:
                id = int(txt)
            except:
                id = (await _.get_users(txt)).id
    except:
        return await eor(m, usage)
    men = (await _.get_users(id)).mention
    for i in range(0, count):
        await _.send_message(m.chat.id, random.choice(RAID)+f" {men}")
    

@Client.on_message(group=raid_watcher)
async def cwf(_, m):
    if not m.from_user:
        return
    if not m.from_user.id:
        return
    if not await is_raid(m.from_user.id):
        return 
    x = random.choice(REPLYRAID)
    await m.reply(x)
            
command = "Raid"
help = f"`» {hl}raid [count] - abuse 😙\n\n» {hl}replyraid - adds reply raid for user.\n\n» {hl}dreplyraid - removes reply raid for user.`"

add_command(command, help)
