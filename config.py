from os import getenv

class API:
    API_ID = int(getenv("API_ID", "13691707"))
    API_HASH = getenv("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

class SECRETS:
    BOT_TOKEN = getenv("BOT_TOKEN", "5449590587:AAH5QaKM1E_fEftVn-9Mw_krUnKOEcn4qXY")
    STRING_SESSION = getenv("STRING_SESSION", "BQA9e22QO_d8WaqjFySbHgdcUq38dZHvRCjuMDMunsUrutg7OYusWeI_NlXgPSOignkR_mSowLeEmcsVby0g3ea2uI8wu92Yy6MkGHo4HDNcczyHqa1urtbTrmkAuaUgv508gl81t1hKDNqUbL6l7wj5EIpU52ZR0RZ0mYV7rH68WNDugZKloeH9iIWIytDHtXYSjtw5-oalj3sfpGUocPPz7Rq9mf5ovuh6QnNXoAOsOZaaXCBD0JdItA9ZvY037h-RoSZcIWce_ps_ZzRWEYQvIzSg1mccM2fIfMad9vkvjAFbHFGHIMUEkU4f2OqAVwLelP0RsDExvKvOa2Dk2bbIAAAAAVBDAOsA")

class STUFF:
    COMMAND_HANDLER = getenv("COMMAND_HANDLER", ".")
    ALIVE_EMOJI = getenv("ALIVE_EMOJI", "😁")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "hehehehe")

class IMAGES:
    ALIVE_IMG = getenv("ALIVE_IMG", "")
    PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c78c8ab32c754a6461ad3.jpg")
    HELP_IMG = getenv("HELP_IMG", "https://telegra.ph/file/c78c8ab32c754a6461ad3.jpg")

class DATABASE:
    MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://royalswag010:Soham@143@cluster0.lsmghyk.mongodb.net/?retryWrites=true&w=majority")

class CHATS:
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001643286042"))
