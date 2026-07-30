import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27079591")) #optional
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8941001487").split()))
OWNER_ID = int(getenv("OWNER_ID", "8941001487"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7308974963:AAHaotNlqBa-Y8wNphyo_B53OYLDbBrD_GE")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://h.uguu.se/OyXvkMun.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")

PM_LOGGER = -1002287700696
LOG_GROUP = -1002287700696

GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAM-ISTKHAR/ISTKHAR_USERBOT")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
