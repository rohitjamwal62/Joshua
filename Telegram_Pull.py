from email.mime.text import MIMEText
import configparser,requests,time,asyncio,sys,smtplib
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')
SMTP_SERVER = config.get('Email', 'SMTP_SERVER')
SMTP_PORT = config.getint('Email', 'SMTP_PORT')  # Convert to int
EMAIL_USERNAME = config.get('Email', 'EMAIL_USERNAME')
EMAIL_PASSWORD = config.get('Email', 'EMAIL_PASSWORD')
RECIPIENT_EMAIL = config.get('Email', 'RECIPIENT_EMAIL')

def calculate_price(original_price, percent_change):
    return original_price * (1 + percent_change / 100)

def main_calculation(entry_prices,profit_percent,loss_percent,purchase_price):
    entry_price = eval(entry_prices)
    
    # print(type(entry_price),"==========entry_price ")
    # print(type(profit_percent),"==========profit_percent ")
    # print(type(loss_percent),"==========loss_percent ")
    # print(type(purchase_price),"==========purchase_price ")
    Store_Calculation = dict()
    profit_price = calculate_price(purchase_price, profit_percent)
    profit_price_Entry = calculate_price(entry_price, profit_percent)
    loss_price = calculate_price(purchase_price, -loss_percent)
    loss_price_entry = calculate_price(entry_price, -loss_percent)
    Store_Calculation['purchase_price'] = purchase_price
    Store_Calculation['profit_price'] = f'{profit_price:.2f}'
    Store_Calculation['loss_price'] = f'{loss_price:.2f}'
    Store_Calculation['profit_price_Entry'] = f'{profit_price_Entry:.2f}'
    Store_Calculation['loss_price_entry'] = f'{loss_price_entry:.2f}'
    return Store_Calculation

def Coin_Name(String):
    Coin = str(String).split('$')[1].split('/')[0].strip()
    return Coin

def stop():
    print("Stopping the script...")
    sys.exit()

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USERNAME
    msg['To'] = RECIPIENT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, RECIPIENT_EMAIL, msg.as_string())
        
