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


def main_calculation(purchase_price,profit_percent,loss_percent):
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

# profit_percent = 20  # Default profit percentage
# loss_percent = 10  # Default loss percentage
# # data = main(purchase_prices,profit_percent,loss_percent)
# # print(data,"====")

# String = """
# Pair: $KSM/USDT
# Direction: LonG
# Exchanges: ByBit USDTLeverage: 3x
# entry: 40.7 -41.5 -  42.85
# TARGETS: 43.5 - 44 - 45 - 46 - 48 - 50 - 52 - 55 - 58 - 61
# STOP LOSS: 6
# """

# purchase_price = eval(Entry_Purchage(String))

# data = main(64.27,profit_percent,loss_percent)
# print(data)