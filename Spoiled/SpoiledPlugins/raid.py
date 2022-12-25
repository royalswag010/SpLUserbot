from pyrogram import Client, filters
from . import hl, verify, eor, get_id
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
            
