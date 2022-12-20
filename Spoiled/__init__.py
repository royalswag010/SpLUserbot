from pyrogram import Client
from config import API, SECRETS

SPL = Client(":SPL-USERBOT:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=SECRETS.STRING_SESSION)

BOT = Client(":SPL-BOT:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=SECRETS.BOT_TOKEN, plugins=dict(root="Spoiled/BotPlugins"))
