import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20604892")
    API_HASH  = os.environ.get("API_HASH", "a75d4dab1a2483a157d93e3ae9bf7500")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7273299519:AAHxRAL5SBMuOkG0gLDYa8PoovxBNu8C7D0") 

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "MetaRename")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://c4.wallpaperflare.com/wallpaper/626/795/625/fan-art-natsuki-subaru-ram-rezero-anime-wallpaper-preview.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '7086472788').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "GENANIMEOFC") # ⚠️ Required Username without @
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002258136705")  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8800"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hɪ {} 👋,
I ᴀᴍ Sᴀsᴜᴋᴇ Uᴄʜɪʜᴀ, ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.\nI ᴡᴀs ᴄʀᴇᴀᴛᴇᴅ ʙʏ Mᴀsᴛᴇʀ @DARKXSIDE78 ᴛᴏ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇs.\nBʏ ᴜsɪɴɢ ᴍᴇ, ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇs, ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟs, ᴀɴᴅ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏs ᴛᴏ ꜰɪʟᴇs ᴀɴᴅ ꜰɪʟᴇs ᴛᴏ ᴠɪᴅᴇᴏs.\nI ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟs ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴs.</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍʏ ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/DARKXSIDE78>Dᴀʀᴋxsɪᴅᴇ78</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/LordShadowSama>Lᴏʀᴅ Sʜᴀᴅᴏᴡ</a>
├📕 Lɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├✍🏼 Iᴍᴘᴏʀᴛ : <a href=https://github.com/aio-libs/aiohttp>Aɪᴏʜᴛᴛᴘ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 3.12</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://t.me/GENANIMEOFC>Gᴇɴ Rᴇɴᴀᴍᴇʀ V0.1</a></b>     
╰───────────────⍟ """

    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ Tᴏ Dᴇᴠᴇʟᴏᴘᴇʀ ﹠ Sᴜᴘᴘᴏʀᴛᴇʀs</b></u>
• ❣️ <a href=https://t.me/DARKXSIDE78>Dᴀʀᴋxsɪᴅᴇ78</a>
• ❣️ <a href=https://t.me/LMPORTANTPERSON>Lᴏʀᴅ Sʜᴀᴅᴏᴡ</a> """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ: <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:

◦ <code>Encoded By @GenAnimeOfc</code>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣</b>"""

    CREATE_TXT = """
<b>Tʜᴀɴᴋ Yᴏᴜ ꜰᴏʀ ᴜsɪɴɢ ᴍʏ Gᴇɴ Rᴇɴᴀᴍᴇʀ (Rᴇɴᴀᴍᴇ Bᴏᴛ)</b>
<b>Iꜰ ʏᴏᴜ’ʀᴇ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ᴘᴜʀᴄʜᴀsɪɴɢ ᴀɴʏ ᴛʏᴘᴇ ᴏꜰ Tᴇʟᴇɢʀᴀᴍ ʙᴏᴛ, Pʏᴛʜᴏɴ sᴄʀɪᴘᴛ, ᴏʀ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ, ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ.</b>

<b>Usᴇʀɴᴀᴍᴇ</b>﹕ @DARKXSIDE78
<b>Pʀɪᴄᴇ﹕ Nᴇɢᴏᴛɪᴀʙʟᴇ</b>
"""
