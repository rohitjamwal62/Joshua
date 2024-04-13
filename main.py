import os,time,asyncio,re,configparser,requests
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage
from datetime import datetime
from GoogleSheet import get_sheet_row
from UserName_ID import Get_Group_Name_Id
from GoogleSheet import get_sheet_row,Create_Row
from match_string import StopLoss,Entry_Purchage,Coin_Name
from Coinspot_API import Sell_Coin,Buy_Coin,Get_Current_Coin_Price
from Telegram_Pull import main_calculation,stop

current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

config = configparser.ConfigParser()
config.read('config.ini')
# API KEY_HASH
api_id = config.getint('Telegram', 'api_id')  # Convert to int
api_hash = config.get('Telegram', 'api_hash')
phone_number = config.get('Telegram', 'phone_number')
# Group Id
NewGroup1 = config.getint('Groups', 'NewGroupId1')  # Convert to int
NewGroup2 = config.getint('Groups', 'NewGroupId2')  # Convert to int
# Group Name
Group1 = config.get('GroupName', 'Group1')
Group2 = config.get('GroupName', 'Group2')
# Percentage
profit_percent = config.get('Percentage', 'Profit_Percentage')
loss_percent = config.get('Percentage', 'Loss_Percentage')


GroupName = "Testing Group"
Group_Id = -4173573828

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        try:
            await client.start(phone_number)
            @client.on(NewMessage(chats=Group_Id))
            async def handle_testing_2_message(event):
                await handle_group_message(client, event, GroupName,Group_Id)  # Pass client to the function
            await client.run_until_disconnected()
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
async def handle_group_message(client, event, groups_names,Group_Id):
    try:
        profit_percent = 60
        loss_percent = 10
        message = event.message
        string_lower = str(message.text).lower()
        search_string = "long"  # Adjust this based on your signal format
        if search_string in string_lower:
            Purchage_Price = Entry_Purchage(string_lower)
            CoinName = Coin_Name(string_lower)
            Buy_Coin(CoinName.upper(), Purchage_Price)
            print("Bought coin:", CoinName.upper(), "at price:", Purchage_Price)
            while True:
                cal = main_calculation(Purchage_Price,profit_percent,loss_percent)
                Check_Live_Price = Get_Current_Coin_Price(CoinName)
                print("#############  Check Live Price : ",Check_Live_Price," ###############")
                profit_price = eval(cal.get('profit_price'))
                print("Profit Price : ",profit_price)
                loss_price = eval(cal.get('loss_price'))
                print("Loss Price : ",loss_price)
                if Check_Live_Price >= profit_price:
                    Sell_Coin(CoinName.upper(), Purchage_Price)
                    print("Sold coin for profit")
                    break
                elif Check_Live_Price <= loss_price:
                    print("Stop-loss reached and Stopped script")
                    stop()
                else:
                    print("Price not reached. Waiting...")
                    await asyncio.sleep(60)  # Wait for an hour before checking again
        else:
            print("Signal not found in message.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    asyncio.run(main())
