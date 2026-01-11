import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


OWNER_ID = int(os.environ.get("OWNER_ID", "6299192020"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Tecfreaktamil")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "1003300996382"))

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "1002932879950"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/ufzpkn.jpg")
F_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/ufzpkn.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6299192020 ,6016699737, 5000956033]
    for x in (os.environ.get("ADMINS", "6299192020").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = false if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 "

START_MSG = os.environ.get("START_MESSAGE"Hi Guy's </b>")


ADMINS.append(OWNER_ID)
ADMINS.append(5170611470)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
    
<b>😈 Bot Made By :</b> @itachi_editz"""
# Telegram Channel @itachi_editz
# Developer @itachi
