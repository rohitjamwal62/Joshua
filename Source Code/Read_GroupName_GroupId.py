from telethon.sync import TelegramClient


api_id = '25500977'
api_hash = '7cf41fa26b716a01a46d744758bfbde2'
phone_number = '+61483212824'

# Create a new TelegramClient instance
with TelegramClient('session_name', api_id, api_hash) as client:
    # Start the client
    client.start()

    # Get a list of your chats (dialogs)
    for dialog in client.iter_dialogs():
        print(dialog.name, ":", dialog.id)