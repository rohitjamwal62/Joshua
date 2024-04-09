from telethon.sync import TelegramClient

# Get group name and group id
api_id = '22842637'
api_hash = '84efbd849705454b21dd41095bc1ddbb'

# Phone number for your Telegram account
phone_number = '+16312521243'

# Create a new TelegramClient instance
with TelegramClient('session_name', api_id, api_hash) as client:
    # Start the client
    client.start()

    # Get a list of your chats (dialogs)
    for dialog in client.iter_dialogs():
        print(dialog.name, ":", dialog.id)