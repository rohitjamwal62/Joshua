import configparser,asyncio,time,os
from datetime import datetime
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage
from match_string import Entry_Purchage, Coin_Name,Filtered_records
from Coinspot_API import Sell_Coin, Buy_Coin, Get_Current_Coin_Price
from Telegram_Pull import main_calculation,stop,send_email
from GoogleSheet import get_sheet_row,Create_Row
async def main():
    while True:  # Run indefinitely
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            api_id = config.getint('Telegram', 'api_id')
            api_hash = config.get('Telegram', 'api_hash')
            phone_number = config.get('Telegram', 'phone_number')
            NewGroup3_Id = config.getint('Groups', 'NewGroupId3')
            CorNIx_Group_Id = config.getint('Groups', 'NewGroupId2')
            # Sample Group Id here
            Group_Id4 = config.getint('Groups', 'NewGroupId4')
            # End Here

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
                    await handle_message(client, event, NewGroup3_Id, profit_percent, loss_percent,Purchase_Price)

                # CORNIX GROUP
                @client.on(NewMessage(chats=CorNIx_Group_Id))
                async def handle_group_message(event):
                    config.read('config.ini')
                    profit_percent = config.getint('Percentage', 'Profit_Percentage')
                    loss_percent = config.getint('Percentage', 'Loss_Percentage')
                    Purchase_Price = config.getint('Purchase_Price', 'P_Price')
                    await handle_message(client, event, CorNIx_Group_Id, profit_percent, loss_percent,Purchase_Price)

                await client.run_until_disconnected()
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        except errors.ConnectionError as e:
            print(f"Connection error occurred: {e}")
            await asyncio.sleep(60)  # Wait for a minute before attempting to reconnect
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(60)  # Wait for a minute before attempting to reconnect
            

async def handle_message(client, event, Group_Id, profit_percent, loss_percent,Purchase_Price):
    try:
        message = event.message
        string_lower = str(message.text).lower()
        search_string = "long"  # Adjust this based on your signal format
        if search_string in string_lower:
            Pair_Entry_live = Filtered_records(string_lower)
            pair_live_list = [Pair_Entry_live[0].strip().replace(' ',''),Pair_Entry_live[1].strip().replace(' ','')]
            Match_Gsheet_records = get_sheet_row(pair_live_list)
            if Match_Gsheet_records != True:
                print("Signal Found................")
                Create_Row(string_lower)
                Entry_Price = Entry_Purchage(string_lower)
                CoinName = Coin_Name(string_lower)
                Check_Live_Price = Get_Current_Coin_Price(CoinName)
                Purchase_Price = 0.1
                Buy_Coin(CoinName.upper(), Purchase_Price,Check_Live_Price,profit_percent,loss_percent)
                Message_Sent = f"Bought coin:"+ " " +CoinName.upper()+" "+ "at price: "+ str(Purchase_Price)
                send_email("Buy Coin",Message_Sent)
                while True:
                    cal = main_calculation(Entry_Price,profit_percent,loss_percent,Purchase_Price)
                    Buy_profit_price = eval(cal.get('profit_price'))
                    Buy_loss_price = eval(cal.get('loss_price'))
                    loss_price_entry = eval(cal.get('loss_price_entry'))
                    profit_price_Entry = eval(cal.get('profit_price_Entry'))
                    Check_Live_Price = Get_Current_Coin_Price(CoinName)
                    if Check_Live_Price >= profit_price_Entry:
                        profit_price = 0.1 #Remove
                        Sell_Coin(CoinName.upper(), profit_price)
                        # Sell_Coin(CoinName.upper(), Buy_profit_price)
                        Message_Sent = f"Sold coin:"+ " " +CoinName.upper()+" "+ "at price: "+ str(Buy_profit_price)
                        print(Message_Sent)
                        send_email("Sell Coin",Message_Sent)
                        break
                    elif Check_Live_Price <= loss_price_entry:
                        print(f"Stop-loss reached and Stopped script. Loss Price is : {Buy_loss_price}")
                        stop()
                    else:
                        # print("Price not reached. Waiting......")
                        print()
                        await asyncio.sleep(60)  # Wait for a minute before checking again
            else:
                print("This Signal Already exists")
        else:
            pass

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    asyncio.run(main())
