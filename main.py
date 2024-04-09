import os,time,asyncio,re,configparser,requests
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage
from datetime import datetime
from GoogleSheet import get_sheet_row
from UserName_ID import Get_Group_Name_Id
from GoogleSheet import get_sheet_row,Create_Row
from match_string import StopLoss
current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

api_id = '25500977'
api_hash = '7cf41fa26b716a01a46d744758bfbde2'
phone_number = '+61483212824'

# Group_Name1 = "Binance Killers® VIP"
Group_Name2 = "Binance Killers® Cornix"
# Group_Name1_Id = -1001178421859
Group_Name2_Id = -1001336862166
GroupName = "Testing Group"
Group_Id = -4173573828


async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        try:
            await client.start(phone_number)
            @client.on(NewMessage(chats=Group_Id))
            async def handle_testing_2_message(event):
                await handle_message(client, event, GroupName,Group_Id)  # Pass client to the function
            await client.run_until_disconnected()
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        except Exception as e:
            print(f"An error occurred: {e}")

async def handle_message(client, event, groups_names,Group_Id):  # Add client parameter here
    try:
        if not hasattr(event, 'handled') or not event.handled:
            message = event.message
            String_Here = message.text
            data = StopLoss(String_Here)
            print(data,"===========")
            # sender_id = message.sender_id  # Get the sender's ID
            # group_name_id = await Get_Group_Name_Id(client,Group_Id, sender_id)
            # UserName = group_name_id.get('UserName')
            # User_Id = group_name_id.get('User_Id')
    except Exception as e:
        pass

if __name__ == '__main__':
    asyncio.run(main())