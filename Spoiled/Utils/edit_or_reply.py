async def eor(ok, t):
    try:
        await ok.edit(t)
    except:
        await ok.reply(t)
