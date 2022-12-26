from . import db

pmdb = db.pm

async def toggle_pm():
    x = await pmdb.find_one({"pm": 0})
    if x:
        return await pmdb.delete_one({"pm": 0})
    else:
        return await pmdb.insert_one({"pm": 0})

async def is_pm_on():
    x = await pmdb.find_one({"pm": 0})
    if x:
        return True
    return False
