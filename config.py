from os import getenv

class API:
    API_ID = int(getenv("API_ID", "13691707"))
    API_HASH = getenv("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

class SECRETS:
    BOT_TOKEN = getenv("BOT_TOKEN", "5449590587:AAH5QaKM1E_fEftVn-9Mw_krUnKOEcn4qXY")
    STRING_SESSION = getenv("STRING_SESSION", "BQC8boAs7ljdHVEufh2-ta_Nfs_e9eHIeZBoSObzl3RYqRHSMdjpbQDSy1XNk_fD0WkL1RRUt4r7xY9O1dxZquDUD4meghlQUv7GROulP3xXmh7cOh9eB2yjY6hiWWyYsULgAUO6pvVcacaM3jy-g2lajVk8T2bWulNgSuGCvz0_WK-_f6vTTepdWRYtSnQvGFVFub44MM2uvpVhQJjMah_At7-mG8nYQwPZsKBHIUa5Bld9Dj5vRCt4EvLu3pxs0aJ6XEj_b-iqdwcQLhVQiylxM1zRGOBidkSewMaWFzLpkgthMNjGxDrESlGXhy33jTz8SLyA7AUMk0aZnVXQde-IAAAAAVBDAOsA")

class STUFF:
    COMMAND_HANDLER = getenv("COMMAND_HANDLER", ".")
    ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🐥")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "i am alive baka")

class IMAGES:
    ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/752d2760ae412d54137aa.jpg")
    PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/6560d89969995dbe7eab8.jpg")
    HELP_IMG = getenv("HELP_IMG", "https://telegra.ph/file/222eb4f860f2c432ec3cb.jpg")

class DATABASE:
    MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://royalswag010:<password>@cluster0.lsmghyk.mongodb.net/?retryWrites=true&w=majority")

class CHATS:
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001643286042"))
