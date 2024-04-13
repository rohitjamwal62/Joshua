from Coinspot_API import Get_Current_Coin_Price
from Telegram_Pull import main_calculation


Live_Price = Get_Current_Coin_Price('KSM')
purchase_price = 59
profit_percent = 20  # Default profit percentage
loss_percent = 10  # Default loss percentage
cal = main_calculation(purchase_price,profit_percent,loss_percent)
# print(cal,"==")
Target_price = eval(cal.get('profit_price'))
Loss = eval(cal.get('loss_price'))
Live_Price = 70.8
# print(Live_Price,"====")
if Live_Price >= Target_price:
    print("Profit................................")
if Live_Price <= Loss:
    print("losssssssssssssssssssssssssssssssssssss")
# if purchase_price
# if entry - stop_loss >= 5 and entry - stop_loss <= 10:
#     print("yess")

