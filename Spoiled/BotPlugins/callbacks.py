from pyrogram import Client, filters
from Spoiled.SpoiledPlugins import COMMANDS_HELP
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from .inline import ma

back = IKM([[IKB("Back", callback_data="cmd_back")]])

for x in COMMANDS_HELP:
    @Client.on_callback_query(filters.regex(x.lower()))
    async def cbq_alpha(_, q):
        await q.answer()
        await q.edit_message_text(COMMANDS_HELP[x], reply_markup=back)

@Client.on_callback_query(filters.regex("cmd_back"))
async cmd_back(_, q):
    await q.answer()
    await q.edit_message_text("Select from below buttons !", reply_markup=ma)
