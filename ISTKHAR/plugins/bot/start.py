from ISTKHAR import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *

PHONE_NUMBER_TEXT = (
"╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ──── ⚘\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : ˹ 🅸sᴛᴋʜᴀʀ 🅤sᴇʀʙᴏᴛ ˼\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰───────────────────────\n────────────────────────\n❍ нσɯ тσ υʂҽ тнιʂ вσᴛ - ᴛɪᴘs ʜᴇʀᴇ \n────────────────────────\n❍ ʂҽʂʂισɳʂ ɠҽɳ вσᴛ ⁚ sᴇssɪᴏɴ-ʙᴏᴛ \n────────────────────────\n❍ ¢ℓσɳҽ вσт ⁚ /clone [ ʂᴛɾιɳg ʂҽʂʂισɳ ]\n────────────────────────\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  ˹ ᴘᴜʀᴠɪ-ᴍᴜsɪᴄ ™˼𓅂 \n────────────────────────"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
buttons = [
[
InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/ll_THUNDER_lll"),
InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/PURVI_SUPPORT"),
],
[
InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/+6sKyj7Lma1k2MDFl"),
InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/purvi_music_bot"),
],
]
reply_markup = InlineKeyboardMarkup(buttons)
await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
chat = msg.chat
text = await msg.reply("ᴜsᴀɢᴇ:\n\n /clone session")
cmd = msg.command
phone = msg.command[1]
try:
await text.edit("ᴛʜᴜɴᴅᴇʀ ᴘʀᴏᴄᴇssɪɴɢ.....✲")
# change this Directry according to ur repo
client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="ISTKHAR/plugins"))
await client.start()
user = await client.get_me()
await msg.reply(f" 𝗝𝗔 𝗣𝗘𝗟 𝗗𝗘 𝗦𝗔𝗕𝗞𝗢 𝗔𝗕 𝗧𝗛𝗨𝗡𝗗𝗘𝗥 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗞𝗘 𝗝𝗔𝗡𝗔 🥵 {user.first_name} 💨.")
except Exception as e:
await msg.reply(f"ERROR: {str(e)}\nPress /start to Start again.")

Isi font me kar do sab code and block quote dal dena har ek camand pe
