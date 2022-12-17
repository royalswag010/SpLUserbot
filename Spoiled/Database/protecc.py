from . import db

waifu = db.waifu

husbando = db.husbando

async def add_waifu_chat(chat_id: int):
    x = await waifu.find_one({"chat_id": chat_id})
    if x:
        return
    await waifu.insert_one({"chat_id": chat_id})

async def is_waifu_chat(chat_id: int):
    x = await waifu.find_one({"chat_id": chat_id})
    if x:
        return True
    return False

async def del_waifu_chat(chat_id: int):
    x = await waifu.find_one({"chat_id": chat_id})
    if not x:
        return
    await waifu.delete_one({"chat_id": chat_id})

async def add_husbando_chat(chat_id: int):
    x = await husbando.find_one({"chat_id": chat_id})
    if x:
        return
    await husbando.insert_one({"chat_id": chat_id})

async def is_husbando_chat(chat_id: int):
    x = await husbando.find_one({"chat_id": chat_id})
    if x:
        return True
    return False

async def del_husbando_chat(chat_id: int):
    x = await husbando.find_one({"chat_id": chat_id})
    if not x:
        return
    await husbando.delete_one({"chat_id": chat_id})

