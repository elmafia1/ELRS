# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
START_PIC  =  getenv ( "START_PIC" ، "https://telegra.ph/file/cc9d3ab087176593ec101.jpg" )
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "QABNADLIB")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS  =  قائمة ( خريطة ( int ، getenv ( "SUDO_USERS" ، "2125600195" ). split ()))
SUPPORT_GROUP  =  getenv ( "SUPPORT_GROUP" ، "https://t.me/ELRASRM" )
UPDATES_CHANNEL  =  getenv ( "UPDATES_CHANNEL" ، "https://t.me/E_L_R_A_S_A_M" )

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐙𝐄𝐔𝐒 𝐎𝐏) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL  =  getenv ( "PROFILE_CHANNEL" ، "https://t.me/E_L_R_A_S_A_M" )
