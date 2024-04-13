from email.mime.text import MIMEText
import configparser,requests,time,asyncio,sys,smtplib
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')
# Email Setting
SMTP_SERVER = config.get('Email', 'SMTP_SERVER')
SMTP_PORT = config.getint('Email', 'SMTP_PORT')  # Convert to int
EMAIL_USERNAME = config.get('Email', 'EMAIL_USERNAME')
EMAIL_PASSWORD = config.get('Email', 'EMAIL_PASSWORD')
RECIPIENT_EMAIL = config.get('Email', 'RECIPIENT_EMAIL')

def calculate_sell_off_prices(purchase_price, profit_percent, loss_percent):
    profit_price = purchase_price * (1 + profit_percent / 100)
    loss_price = purchase_price * (1 - loss_percent / 100)
    return profit_price, loss_price

def calculate_profit_and_loss(purchase_price, sell_price):
    profit = sell_price - purchase_price
    loss = purchase_price - sell_price if sell_price < purchase_price else 0
    return profit, loss

def calculate_percentage_change(purchase_price, sell_price):
    change = ((sell_price - purchase_price) / purchase_price) * 100
    return change


def main_calculation(purchase_prices,profit_percent,loss_percent):
    purchase_price = eval(purchase_prices)
    Store_Calculation = dict()
    profit_price, loss_price = calculate_sell_off_prices(purchase_price, profit_percent, loss_percent)
    profit, loss = calculate_profit_and_loss(purchase_price, profit_price)
    profit_percentage = calculate_percentage_change(purchase_price, profit_price)
    loss_percentage = calculate_percentage_change(purchase_price, loss_price)
    Store_Calculation['purchase_price'] = purchase_price
    Store_Calculation['profit_price'] = f'{profit_price:.2f}'
    Store_Calculation['loss_price'] = f'{loss_price:.2f}'
    Store_Calculation['profit'] = f'${profit:.2f}'
    Store_Calculation['profit_percentage'] = f'${profit_percentage:.2f}'
    Store_Calculation['loss_percentage'] = f'${loss_percentage:.2f}'
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