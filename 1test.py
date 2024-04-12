from Coinspot_API import Get_Current_Coin_Price
from Telegram_Pull import main_calculation
data = Get_Current_Coin_Price('KSM')
purchase_price = 59
profit_percent = 20  # Default profit percentage
loss_percent = 10  # Default loss percentage
data = main_calculation(purchase_price,profit_percent,loss_percent)


if entry - stop_loss >= 5 and entry - stop_loss <= 10:
    print("yess")

