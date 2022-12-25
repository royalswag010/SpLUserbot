from . import db

raid = db.raid

async def add_raid(user_id: int):
    x = await raid.find_one({"user_id": user_id})
    if x:
        return
    return await raid.insert_one({"user_id": user_id})

async def del_raid(user_id: int):
    x = await raid.find_one({"user_id": user_id})
    if not x:
        return
    return await raid.delete_one({"user_id": user_id})

async def is_raid(user_id: int):
    x = await raid.find_one({"user_id": user_id})
    if not x:
        return False
    return True

async def get_raids():
    x = raid.find({"user_id": {"$gt": 0}})
    if not x:
        return []
    h = []
    for y in await x.to_list(length=1000000000):
        h.append(y["user_id"])
    return h

