#ᴀᴅᴅ ʟɪᴄᴇɴsᴇ ᴛᴇxᴛ ʜᴇʀᴇ ɢᴇᴛ ɪᴛ ғʀᴏᴍ ʙᴇʟᴏᴡ.

from MukeshRobot import pbot as app # This is bot's client
from pyrogram import filters # pyrogram filters
from pyrogram.types import Message
from MukeshRobot.sanghandler import COMMAND_HANDLER
from MukeshRobot.utils.admins import can_change_info
from MukeshRobot.utils.localization import use_chat_lang
from MukeshRobot.database.sangmata_db import (
    add_userdata,
    cek_userdata,
    get_userdata,
    is_sangmata_on,
    sangmata_off,
    sangmata_on,
)

#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "SangMata"
__help__ = "This function is on testing mode and isn't fully developed. \n Use `/sangmata_set on` to enable, \n `/sangmata_set off` to disable."


# Check user that change first_name, last_name and usernaname
@app.on_message(
    filters.group & ~filters.bot & ~filters.via_bot,
    group=5,
)
#   user = await extract_user(message)
#    token = await int_to_alpha(user.id)
#    _check = await get_authuser_names(message.chat.id)
#    count = len(_check)
#    if int(count) == 25:
#        return await message.reply_text(_["auth_1"])
#    if token not in _check:
#        assis = {
#            "auth_user_id": user.id,
#            "auth_name": user.first_name,
#            "admin_id": message.from_user.id,
#            "admin_name": message.from_user.first_name,
#        }
@use_chat_lang()
async def cek_mataa(_, ctx: Message, strings):
    if ctx.sender_chat or not await is_sangmata_on(ctx.chat.id):
        return
    chat_id = ctx.chat.id
    user_id = ctx.from_user.id
    token = await int_to_alpha(user_id)
    _check = await cek_userdata(ctx.chat.id)
    if token not in _check:
        await add_userdata(chat_id, 
            ctx.from_user.id,
            ctx.from_user.username,
            ctx.from_user.first_name,
            ctx.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(ctx.chat.id)
    msg = ""
    if (
        usernamebefore != ctx.from_user.username
        or first_name != ctx.from_user.first_name
        or lastname_before != ctx.from_user.last_name
    ):
        msg += f"💔<b>User History</b>💔\n\n User: {ctx.from_user.mention} \n\n ID: [<code>{ctx.from_user.id}</code>]\n\n"
    if usernamebefore != ctx.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else strings("no_uname")
        usernameafter = (
            f"@{ctx.from_user.username}"
            if ctx.from_user.username
            else strings("no_uname")
        )
        msg += strings("uname_change_msg").format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(chat_id, 
            ctx.from_user.username,
            ctx.from_user.first_name,
            ctx.from_user.last_name,
        )
    if first_name != ctx.from_user.first_name:
        msg += strings("firstname_change_msg").format(
            bef=first_name, aft=ctx.from_user.first_name
        )
        await add_userdata(chat_id,
            ctx.from_user.username,
            ctx.from_user.first_name,
            ctx.from_user.last_name,
        )
    if lastname_before != ctx.from_user.last_name:
        lastname_before = lastname_before or strings("no_last_name")
        lastname_after = ctx.from_user.last_name or strings("no_last_name")
        msg += strings("lastname_change_msg").format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(chat_id,
            ctx.from_user.username,
            ctx.from_user.first_name,
            ctx.from_user.last_name,
        )
    if msg != "":
        await ctx.reply_text(msg, quote=False)


@app.on_message(
    filters.group
    & filters.command("sangmata_set", COMMAND_HANDLER)
    & ~filters.bot
    & ~filters.via_bot
)
@can_change_info
@use_chat_lang()
async def set_mataa(_, ctx: Message, strings):
    if len(ctx.command) == 1:
        return await ctx.reply_text(
            strings("set_sangmata_help").format(cmd=ctx.command[0])
        )
    if ctx.command[1] == "on":
        cekset = await is_sangmata_on(ctx.chat.id)
        if cekset:
            await ctx.reply_text(strings("sangmata_already_on"))
        else:
            await sangmata_on(ctx.chat.id)
            await ctx.reply_text(strings("sangmata_enabled"))
    elif ctx.command[1] == "off":
        cekset = await is_sangmata_on(ctx.chat.id)
        if not cekset:
            await ctx.reply_text(strings("sangmata_already_off"))
        else:
            await sangmata_off(ctx.chat.id)
            await ctx.reply_text(strings("sangmata_disabled"))
    else:
        await ctx.reply_text(strings("wrong_param"))

# int_to_alpha
async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id
