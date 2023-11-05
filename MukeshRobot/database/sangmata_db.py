from MukeshRobot.database import dbname
from typing import Dict, Union

matadb = dbname["sangmata"]

#async def _get_authusers(chat_id: int) -> Dict[str, int]:
#    _notes = await authuserdb.find_one({"chat_id": chat_id})
#    if not _notes:
#        return {}
#    return _notes["notes"]
# Get Data User
async def cek_userdata(chat_id: int) -> Dict[str, int]:
    _history = await matadb.find_one({"chat_id": chat_id})
    if not _history:
        return {}
    return _history["history"]

#async def get_authuser(chat_id: int, name: str) -> Union[bool, dict]:
#    name = name
#    _notes = await _get_authusers(chat_id)
#    if name in _notes:
#        return _notes[name]
#    else:
#        return False
async def get_userdata(chat_id: int,name: str) -> Union[bool, dict]:
    name = name
    _history = await ek_userdata(chat_id)
    return _history[name]


#async def save_authuser(chat_id: int, name: str, note: dict):
#    name = name
#    _notes = await _get_authusers(chat_id)
#    _notes[name] = note
#
#    await authuserdb.update_one(
#        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
#    )
async def add_userdata(chat_id: int, user_id: int, username, first_name, last_name, name: str, history: dict):
    name = name
    _history = await cek_userdata(chat_id)
    _hisrory[name] = history
    await matadb.update_one({"chat_id": chat_id},
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
