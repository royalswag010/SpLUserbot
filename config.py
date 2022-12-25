from os import getenv

class API:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")

class SECRETS:
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    STRING_SESSION = getenv("STRING_SESSION", "")

class STUFF:
    COMMAND_HANDLER = getenv("COMMAND_HANDLER", ".")
    ALIVE_EMOJI = getenv("ALIVE_EMOJI", "")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "")

class IMAGES:
    ALIVE_IMG = getenv("ALIVE_IMG", "")
    PING_IMG = getenv("PING_IMG", "")
    HELP_IMG = getenv("HELP_IMG", "")

class DATABASE:
    MONGO_DB_URL = getenv("MONGO_DB_URL", "")

class CHATS:
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
