import configparser
import asyncio
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage

async def main():
    while True:  # Run indefinitely
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            api_id = config.getint('Telegram', 'api_id')
            api_hash = config.get('Telegram', 'api_hash')
            phone_number = config.get('Telegram', 'phone_number')
            NewGroup3_Id = config.getint('Groups', 'NewGroupId3')
            
            async with TelegramClient('session_name', api_id, api_hash) as client:
                await client.start(phone_number)
                
                # TESTING GROUP
                @client.on(NewMessage(chats=NewGroup3_Id))
                async def handle_group_message(event):
                    # Re-read config.ini before processing each message
                    config.read('config.ini')
                    profit_percent = config.getint('Percentage', 'Profit_Percentage')
                    loss_percent = config.getint('Percentage', 'Loss_Percentage')
                    Purchase_Price = config.getint('Purchase_Price', 'P_Price')
                    await handle_message(client, event, NewGroup3_Id, profit_percent, loss_percent, Purchase_Price)
                
                await client.run_until_disconnected()
        
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        
        except errors.AuthKeyDuplicatedError:
            print("The authorization key (session file) was used under two different IP addresses simultaneously.")
            print("Generating a new session name...")
            # Generate a new session name or handle session management differently
            
        except errors.ConnectionError as e:
            print(f"Connection error occurred: {e}")
            await asyncio.sleep(60)  # Wait for a minute before attempting to reconnect
        
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(60)  # Wait for a minute before attempting to reconnect

async def handle_message(client, event, Group_Id, profit_percent, loss_percent, Purchase_Price):
    try:
        message = event.message
        string_lower = str(message.text).lower()
        print(string_lower, "####################")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    asyncio.run(main())
