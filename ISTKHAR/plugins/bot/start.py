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
    "╭────── ˹ ɪηғσʀϻᴧᴛɪση ˼ ──── ⚘\n"
    "┆⚘ ʜєʏ, ɪ ᴧϻ : [˹ 🅸sᴛᴋʜᴧʀ 🅤sєʀʙσᴛ ˼](https://t.me/Beta_userbot)\n"
    "┆⚘ ϻσʀє ᴧηɪϻᴧᴛɪση, ғᴜη\n"
    "┊⚘ ᴘσɯєʀғᴜʟ & ᴜsєғᴜʟ ᴜsєʀʙσᴛ\n"
    "╰───────────────────────\n"
    "────────────────────────\n"
    "❍ ʜσɯ ᴛσ ᴜsє ᴛʜɪs ʙσᴛ - [ᴛɪᴘs ʜєʀє](https://t.me/betabot_hub) \n"
    "────────────────────────\n"
    "❍ sєssɪσηs ɢєη ʙσᴛ ⁚ [sєssɪση-ʙσᴛ](https://t.me/SHIV_SESSION_BOT) \n"
    "────────────────────────\n"
    "❍ ᴄʟσηє ʙσᴛ ⁚ /clone [ sᴛʀɪηɢ sєssɪση ]\n"
    "────────────────────────\n"
    "❍ ᴘσɯєʀєᴅ ʙу ⏤‌‌‌‌  [˹ ʙᴇᴛᴀ-ʙᴏᴛs™˼𓅂](https://t.me/betabot_hub) \n"
    "────────────────────────"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
        [
            InlineKeyboardButton("˹ σɯηєʀ ˼", url="https://t.me/ll_alexx_lll"),
            InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛє ˼", url="https://t.me/betabot_hub"),
        ],
        [
            InlineKeyboardButton("˹ sᴜᴘᴘσʀᴛ ˼", url="https://t.me/betabot_support"),
            InlineKeyboardButton("˹ ϻᴜsɪᴄ ˼", url="https://t.me/SizzuMusicBot"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴧɢє:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    
    try:
        await text.edit("ᴛʜᴜηᴅєʀ ᴘʀσᴄєssɪηɢ.....✲")
        # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="ISTKHAR/plugins"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 𝗝𝗔 𝗣𝗘𝗟 𝗗𝗘 𝗦𝗔𝗕𝗞𝗢 𝗔𝗕 𝗜𝗦𝗧𝗞𝗛𝗔𝗥 𝗦𝗛𝗜𝗩 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗞𝗘 𝗝𝗔𝗡𝗔 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**єʀʀσʀ:** `{str(e)}`\nᴘʀєss /start ᴛσ sᴛᴧʀᴛ ᴧɢᴧɪη.")
