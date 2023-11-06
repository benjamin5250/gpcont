from MukeshRobot.database import name
from typing import Dict, Union, List

matadb = name["sangmata"]

#async def _get_authusers(chat_id: int) -> Dict[str, int]:
#    _notes = await authuserdb.find_one({"chat_id": chat_id})
#    if not _notes:
#        return {}
#    return _notes["notes"]
# Get Data User
async def _cek_userdata(chat_id: int) -> Dict[str, int]:
    _notes = await matadb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]

#async def get_authuser_names(chat_id: int) -> List[str]:
#    _notes = []
#    for note in await _get_authusers(chat_id):
#        _notes.append(note)
#    return _notes
async def cek_userdata(chat_id: int) -> List[str]:
    _notes = []
    for note in await _cek_userdata(chat_id):
        _notes.append(note)
    return _notes

#async def get_authuser(chat_id: int, name: str) -> Union[bool, dict]:
#    name = name["sangmata"]
#    _notes = await _get_authusers(chat_id)
#    if name in _notes:
#        return _notes[name]
#    else:
#        return False
async def get_userdata(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()    
    _notes = await _cek_userdata(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False

#async def save_authuser(chat_id: int, name: str, note: dict):
#    name = name["sangmata"]
#    _notes = await _get_authusers(chat_id)
#    _notes[name] = note
#
#    await authuserdb.update_one(
#        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
#    )
async def add_userdata(chat_id: int, user_id: int, username, userfullname, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _cek_userdata(chat_id)
    _notes[name] = note
    await matadb.update_one({"chat_id": chat_id},
        {
            "$set": {
                "notes": _notes
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
