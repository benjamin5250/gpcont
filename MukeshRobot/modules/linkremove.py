from MukeshRobot import pbot as app # This is bot's client
from pyrogram import filters # pyrogram filters
from MukeshRobot import DRAGONS


#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "Link Remover"
__help__ = "Module help message"


def check_message(type, message):
    print("\n\n\n\n==============\n\n\n")
    print(type, message)

    if message.from_user.id in DRAGONS:
        return

    # check getChatMember, check is creator or administrator
    chat_member = app.get_chat_member(message.chat.id, message.from_user.id)
    print("==================> User data:", chat_member)
    if chat_member.status == 'creator' or chat_member.status == 'administrator':
        return
    if chat_member.status == 'left' and chat_member.user.username == 'GroupAnonymousBot':
        return

    if message.text.find('@') != -1:
        print("Found username in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('t.me') != -1:
        print("Found link to username in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('http://') != -1 or message.text.find('https://') != -1:
        print("Found link to website in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('.com') != -1 or message.text.find('.ir') != -1:
        print("Found link to website in message text")
        app.delete_message(message.chat.id, message.message_id)

# edit message listener
@app.edited_message_handler(func=lambda message: True)
def edit_message(message):
    check_message("edit", message)

# new message listener
@app.message_handler(func=lambda message: True)
def new_message(message):
    check_message("new", message)
