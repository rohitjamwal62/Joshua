import os
import time
import asyncio
import configparser
from datetime import datetime
from telethon.sync import TelegramClient, errors
from telethon.events import NewMessage
from match_string import Entry_Purchage, Coin_Name
from Coinspot_API import Sell_Coin, Buy_Coin, Get_Current_Coin_Price
from Telegram_Pull import main_calculation, stop

async def main():
    while True:  # Run indefinitely
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            
            api_id = config.getint('Telegram', 'api_id')
            api_hash = config.get('Telegram', 'api_hash')
            phone_number = config.get('Telegram', 'phone_number')

            NewGroup3_Id = config.getint('Groups', 'NewGroupId3')
            Group3_Name = config.get('GroupName', 'Group3')
            
            async with TelegramClient('session_name', api_id, api_hash) as client:
                await client.start(phone_number)
                @client.on(NewMessage(chats=NewGroup3_Id))
                async def handle_group_message(event):
                    # Re-read config.ini before processing each message
                    config.read('config.ini')
                    profit_percent = config.getint('Percentage', 'Profit_Percentage')
                    loss_percent = config.getint('Percentage', 'Loss_Percentage')
                    await handle_message(client, event, Group3_Name, NewGroup3_Id, profit_percent, loss_percent)
                await client.run_until_disconnected()
        except errors.SessionPasswordNeededError:
            print("The session file is locked with a password. Please unlock it or remove the session file.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await asyncio.sleep(60)  # Wait for a minute before attempting to reconnect

async def handle_message(client, event, groups_names, Group_Id, profit_percent, loss_percent):
    try:
        message = event.message
        string_lower = str(message.text).lower()
        search_string = "long"  # Adjust this based on your signal format
        if search_string in string_lower:
            Purchage_Price = Entry_Purchage(string_lower)
            CoinName = Coin_Name(string_lower)
            Buy_Coin(CoinName.upper(), Purchage_Price)
            print("Bought coin:", CoinName.upper(), "at price:", Purchage_Price)
            while True:
                cal = main_calculation(Purchage_Price, profit_percent, loss_percent)
                Check_Live_Price = Get_Current_Coin_Price(CoinName)
                # print("#############  Check Live Price : ", Check_Live_Price," ###############")
                profit_price = eval(cal.get('profit_price'))
                # print("Profit Price : ", profit_price)
                loss_price = eval(cal.get('loss_price'))
                # print("Loss Price : ", loss_price)
                if Check_Live_Price >= profit_price:
                    Sell_Coin(CoinName.upper(), Purchage_Price)
                    print("Sold coin for profit")
                    break
                elif Check_Live_Price <= loss_price:
                    print("Stop-loss reached and Stopped script")
                    stop()
                else:
                    print("Price not reached. Waiting...")
                    await asyncio.sleep(60)  # Wait for a minute before checking again
        else:
            print("Signal not found in message.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    asyncio.run(main())
