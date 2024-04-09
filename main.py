import os,pytz,time,asyncio,re,configparser,requests
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage
from datetime import datetime
from GoogleSheet import get_sheet_row
from UserName_ID import Get_Group_Name_Id
from GoogleSheet import get_sheet_row,Create_Row


api_id = '28110734'
api_hash = '7562e8af60beeb05b10ddac0dd69512e62'
phone_number = '+9182888329988'
Boost_OnlyFans_Group_id = -1001173439993
Group_Name = "Boost OnlyFans"


current_directory = os.path.dirname(os.path.abspath(__file__))
img_directory = os.path.join(current_directory, 'img')


current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

Group_Name1 = "Boost OnlyFans"
Group_Name1_Id = -1001173439993


async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        try:
            await client.start(phone_number)
            @client.on(NewMessage(chats=Group_Name1_Id))
            async def handle_testing_2_message(event):
                await handle_message(client, event, Group_Name1,Group_Name1_Id)  # Pass client to the function
            await client.run_until_disconnected()
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        except Exception as e:
            print(f"An error occurred: {e}")


async def handle_message(client, event, groups_names,Group_Id):  # Add client parameter here
    try:
        if not hasattr(event, 'handled') or not event.handled:
            message = event.message
            # sender_id = message.sender_id  # Get the sender's ID
            # group_name_id = await Get_Group_Name_Id(client,Group_Id, sender_id)
            # UserName = group_name_id.get('UserName')
            # User_Id = group_name_id.get('User_Id')
    except Exception as e:
        pass




if __name__ == '__main__':
    asyncio.run(main())