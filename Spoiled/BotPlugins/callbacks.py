from pyrogram import filters
from Spoiled.SpoiledPlugins import COMMANDS_HELP
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from Spoiled.SpoiledPlugins import build_help_markup, COMMANDS_HELP
from pyrogram import Client as BOT
from Spoiled.Database.sudo import is_sudo
from Spoiled import SPL

back = IKM([[IKB("Back", callback_data="cmd_back")]])

id = None

CMDS = []
for x in COMMANDS_HELP:
    CMDS.append(x)

@BOT.on_callback_query(~filters.regex("cmd_back"))
async def alpha_cbq(_, q):
    global id
    if not id:
        id = (await SPL.get_me()).id
    qid = q.from_user.id
    if id != qid:
        if not await is_sudo(qid):
            return await q.answer("You can't use these !\n\nCreate your own.", show_alert=True)
    for x in COMMANDS_HELP:
        if q.data == x.lower():
            await q.answer()
            await q.edit_message_text(f"**{x} Help Module\n\n**" + COMMANDS_HELP[x], reply_markup=back)

@BOT.on_callback_query(filters.regex("cmd_back"))
async def cmd_back(_, q):
    global id
    if not id:
        id = (await SPL.get_me()).id
    qid = q.from_user.id
    if id != qid:
        if not await is_sudo(qid):
            return await q.answer("You can't use these !\n\nCreate your own.", show_alert=True)
    ma = build_help_markup(COMMANDS_HELP)
    try:
        await q.answer()
        await q.edit_message_text("Select from below buttons !", reply_markup=ma)
    except Exception as e:
        await q.message.reply(e)
