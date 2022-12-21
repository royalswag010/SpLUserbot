from pyrogram import filters
from Spoiled.SpoiledPlugins import COMMANDS_HELP
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from .inline import ma
from pyrogram import Client as BOT
from Spoiled.Database.sudo import is_sudo
from Spoiled import SPL

back = IKM([[IKB("Back", callback_data="cmd_back")]])

id = None

while True:
    for x in COMMANDS_HELP:
        @BOT.on_callback_query(filters.regex(x.lower()))
        async def cbq_alpha(_, q):
            global id
            if not id:
                id = (await SPL.get_me()).id
            qid = q.from_user.id
            if id != qid:
                if not await is_sudo(qid):
                    return await q.answer("You can't use these !\n\nCreate your own.", show_alert=True)
            await q.answer()
            await q.edit_message_text(COMMANDS_HELP[x], reply_markup=back)

@BOT.on_callback_query(filters.regex("cmd_back"))
async def cmd_back(_, q):
    global id
    if not id:
        id = (await SPL.get_me()).id
    qid = q.from_user.id
    if id != qid:
        if not await is_sudo(qid):
            return await q.answer("You can't use these !\n\nCreate your own.", show_alert=True)
    try:
        await q.answer()
        await q.edit_message_text("Select from below buttons !", reply_markup=ma)
    except Exception as e:
        await q.message.reply(e)
