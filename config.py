import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25069425")
API_HASH = os.environ.get("API_HASH", "41034e257e6449615faea5f18bbe1dd7")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6034105097:AAHssjQYwoQ7p6jhonOXJF6xHIVLh-mVJeM")

CHANNEL = os.environ.get("CHANNEL", "Crazybotz") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","crazysupportz") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","Crazybotz") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","heartlesssn")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://Renamerplan:Renamerplan@cluster0.kkezdvj.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/6b003c4f05cb8609627d7.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6249148586').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001706887258"))
