from MukeshRobot import pbot as app # This is bot's client
from pyrogram import filters # pyrogram filters
from MukeshRobot import DRAGONS
from telebot import TeleBot

#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "Link Remover"
__help__ = "Module help message"

def check_message(type, message):
    print("\n\n\n\n==============\n\n\n")
    print(type, message)

    if message.from_user.id in DRAGONS:
        return

@app.on_message(filters.forward & filters.document)
async def fwdmsg(bot, message):
    await message.delete
    
@app.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.service)
async def delete(bot,message):
 await message.delete()

