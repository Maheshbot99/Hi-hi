import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22525529")
API_HASH = os.environ.get("API_HASH", "840111f82bbd1d2d3de5055afccf6a92")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "5355979778:AAE7y04umUaDNfyUls8Ejf_5h6vGYtJERvQ")

CHANNEL = os.environ.get("CHANNEL", "CrazyXBoTs") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","@ReName_MsBot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","KicchaFanMaHi") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","CrazyXBoTs") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","KicchaFanMaHi")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Name")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://Name:Name@cluster0.m12ofgg.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/d132594c0967e45270962.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5450011131').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001808372200"))
