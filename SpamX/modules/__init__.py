from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/aa4bf1e57d11fb75b602e.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else"𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗦𝗣𝗔𝗠"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[☆𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥☆](https://t.me/mastiwithfriendsx)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ **𝗠คѕƬєя:** ☆𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥☆
➪ **𝗣ƴƬнοи ⩔єяនɨ០ɳ:** `{platform.python_version()}`
➪ **𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 ⩔єяនɨ០ɳ:** `{__version__}`
➪ **𝗣ƴяο ⩔єяនɨ០ɳ:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
