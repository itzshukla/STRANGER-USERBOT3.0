from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝐎𝐏 ѕραм"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/89f23433043a4bfa255c3.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐎𝐏 ѕραм - by ʂɧı۷ąɱ"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**❖ 𝐎𝐏 𝐒𝐏𝐀𝐌 ❖**
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➠ **𝓜𝓪𝓼𝓽𝓮𝓻:** [☆ʂɧı۷ąɱ☆](https://t.me/itsz_shivam)
➠ **ρутнσи νєяѕισи:** `{platform.python_version()}`
➠ **𝐎𝐏ѕραм νєяѕισи:** `{__version__}`
➠ **ρуяσ νєяѕισи:** `{pyro_vr}`
➠ **му яєρσ:** [•𝔤𝔬 𝔥𝔢𝔯𝔢•](https://te.legra.ph/file/ebc3fc421b8776e29ad98.mp4)
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
