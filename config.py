# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7988735")

API_HASH = os.environ.get("API_HASH", "8339b7684eb7f4653ed032d4828ebf89")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1281854169:AAFZBTE1lhi_woIiwlR3OQWCDa61GGtLf9Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "botXhub") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebotXhub")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://vivekrajroy705:NL3uH0IX2skZqO5R@cluster0.2bscxuc.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/2179a9464d47f291f62b3.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6521935712 989095888').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
