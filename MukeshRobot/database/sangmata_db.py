from MukeshRobot.database import dbname
from typing import Dict, Union, List
from MukeshRobot.database.locale_db import name
from pyrogram.types import Message

matadb = dbname["sangmata"]

async def chat_id(_, ctx: Message):
    return ctx.chat.id

# Get Data User
async def cek_userdata(user_id: int) -> bool:
    group = await matadb.find_one({"chat_id": chat_id})
    return bool(group)


async def get_userdata(user_id: int, chat_id: int) -> bool:
    group = await matadb.find_one({"chat_id": chat_id})
    return group["username"], group["first_name"], group["last_name"], group["user_id"]


async def add_userdata(chat_id: int, user_id: int, username, first_name, last_name):
    await matadb.update_one(
        {"chat_id": chat_id},
        {
            "$set": {
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
            }
        },
        upsert=True,
    )



# Enable Mata MissKaty in Selected Chat
async def is_sangmata_on(chat_id: int) -> bool:
    chat = await matadb.find_one({"chat_id_toggle": chat_id})
    return bool(chat)


async def sangmata_on(chat_id: int) -> bool:
    await matadb.insert_one({"chat_id_toggle": chat_id})


async def sangmata_off(chat_id: int):
    await matadb.delete_one({"chat_id_toggle": chat_id})
