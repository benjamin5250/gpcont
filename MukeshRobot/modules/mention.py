from MukeshRobot import pbot as Client # This is bot's Client
from pyrogram import filters # pyrogram filters
import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from MukeshRobot import telethn as client

#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "MentionAll"
__help__ = "Module help message"

spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("I'm not dead 😎")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪  𝐈 𝐚𝐦 ဂရပ်ထမယ် 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐛𝐨𝐭 𝐭𝐨 𝐦𝐞𝐧𝐭𝐢𝐨𝐧 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐢𝐧 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦\n✪ 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐦𝐞 𝐚𝐧𝐝 𝐭𝐲𝐩𝐞 /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ Owner    : [KAREN](https://t.me/KoShine_Apaing)\n┣★ Group › : [ဂရပ်ထမယ်](https://t.me/EwhWTBjxYuYxYTFl)┓\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ\nᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/KoShine_Apaing) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=(
            [
                Button.url(
                    "☀︎︎️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☀︎︎",
                    "https://t.me/Gayetbot?startgroup=true",
                ),
            ],
            [
                Button.url("☀︎︎ Group ☀︎︎︎", "https://t.me/EwhWTBjxYuYxYTFl"),
                Button.url("☀︎︎ Owner ☀︎︎", "https://t.me/KoShine_Apaing"),
            ],
        ),
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮 𝐎𝐟 ဂရပ်ထမယ် 𝐌𝐞𝐧𝐭𝐢𝐨𝐧\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n✪ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.\n✪ `Example: /mentionall Good Morning!`\n✪ Yᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ. Bᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇsssᴀɢᴇ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ Group", "https://t.me/EwhWTBjxYuYxYTFl"),
                Button.url("Channel ☀︎︎", "https://t.me/KoShine_Apaing"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ 𝐎𝐰𝐧𝐞𝐫 𝐌𝐞𝐧𝐮 𝐎𝐟 ဂရပ်ထမယ် 𝐌𝐞𝐧𝐭𝐢𝐨𝐧\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [KAREN](https://t.me/KoShine_Apaing\n✪ The creator\n✪ Group(ttps://t.me/EwhWTBjxYuYxYTFl\n✪ "
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ Group ☀︎︎︎", "https://t.me/EwhWTBjxYuYxYTFl"),
                Button.url("☀︎︎ Owner ☀︎︎", "https://t.me/KoShine_Apaing"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/mentionall|@mentionall|@all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ ᴍᴇ ᴏɴᴇ ᴀʀɢᴜᴍᴇɴᴛ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)"
            )
    else:
        return await event.respond(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)"
            )
    else:
        return await event.respond(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("sᴛᴏᴘᴘᴇᴅ.")

@client.on(events.NewMessage(pattern="^/fools|ကျပ်မပြည့်တဲ့သုံးကောင်|ကျပ်မပြည့်တဲ့သုံးကောင်|@ကျပ်မပြည့်တဲ့သုံးကောင် ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.reply("@KhoonAtta   @KoShine_Apaing   @XiaoBai_Shiba")
    helptext = "@KhoonAtta   @KoShine_Apaing   @XiaoBai_Shiba"
    await event.reply(
        helptext,
        link_preview=False )

@client.on(events.NewMessage(pattern="^/Mommy|@ယောက္ခမ ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.reply("@KoShine_Apaing သူ့ကိုခေါ်တာလား")
    helptext = "@KoShine_Apaing သူ့ကိုခေါ်တာလား"
    await event.reply(
        helptext,
        link_preview=False )
