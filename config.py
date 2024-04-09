import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "7988735"))
    API_HASH = os.environ.get("API_HASH" "8339b7684eb7f4653ed032d4828ebf89")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1281854169:AAFZBTE1lhi_woIiwlR3OQWCDa61GGtLf9Y")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6521935712"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://vivekrajroy705:NL3uH0IX2skZqO5R@cluster0.2bscxuc.mongodb.net/?retryWrites=true&w=majority")
