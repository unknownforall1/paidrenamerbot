# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7988735")

API_HASH = os.environ.get("API_HASH", "8339b7684eb7f4653ed032d4828ebf89")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "BOT TOKEN ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "botXhub")

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebotXhub")     


LOGCHANNEL= os.environ.get("LOGCHANNEL", "-1002087175886")
DBCHANNEL = os.environ.get("DBCHANNEL", "-1002087175886")
DB_URL = os.environ.get("DB_URL", "#DATABASE URL")
 
FLOOD = int(os.environ.get("FLOOD", "10"))
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/2179a9464d47f291f62b3.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6521935712 989095888').split()]

PORT = os.environ.get("PORT", "8080")

OWNER_ID = int(os.environ.get("OWNER_ID", 6521935712))

BANNED_USERS = []

DOWNLOAD_LOCATION = "./DOWNLOADS" 

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
