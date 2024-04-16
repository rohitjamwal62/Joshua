def calculate_price(original_price, percent_change):
    return original_price * (1 + percent_change / 100)

purchase_price = 10
profit_percent = 20  # 20%
loss_percent = 10    # 10%
entry_price = 3

purchase_price_20_percent = calculate_price(purchase_price, profit_percent)
entry_price_20_percent = calculate_price(entry_price, profit_percent)
purchase_price_20_percent_less = calculate_price(purchase_price, -loss_percent)
entry_price_20_percent_less = calculate_price(entry_price, -loss_percent)

print("Purchase Price with 20% increase:", purchase_price_20_percent)
print("Entry Price with 20% increase:", entry_price_20_percent)
print("Purchase Price with 20% decrease:", purchase_price_20_percent_less)
print("Entry Price with 20% decrease:", entry_price_20_percent_less)
