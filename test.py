# entry_min = 40
# entry_max = 42.85
# stop_loss = 38.73

# # Define the profit and loss percentages
# profit_percentage = 0.1  # 10% profit
# loss_percentage = 0.03  # 3% loss

# # Calculate the profit and loss prices
# profit_price = entry_min * (1 + profit_percentage)
# loss_price = entry_min * (1 - loss_percentage)

# # Print the results
# print(f"Entry Price Range: ${entry_min} - ${entry_max}")
# print(f"Stop Loss: ${stop_loss}")
# print(f"Profit Target: ${profit_price:.2f} ({profit_percentage*100}% profit)")
# print(f"Loss Limit: ${loss_price:.2f} ({loss_percentage*100}% loss)")

# def calculate_sell_off_prices(purchase_price, profit_percent, loss_percent):
#     profit_price = purchase_price * (1 + profit_percent / 100)
#     loss_price = purchase_price * (1 - loss_percent / 100)
#     return profit_price, loss_price

# # Example usage
# purchase_price = 42.85  # Example purchase price
# profit_percent = 10  # Example profit percentage
# loss_percent = 3  # Example loss percentage

# profit_price, loss_price = calculate_sell_off_prices(purchase_price, profit_percent, loss_percent)
# print(f"Sell-off price for profit: {profit_price}")
# print(f"Sell-off price for loss: {loss_price}")
purchase_price_range = [40, 41.5, 42.85]
target_prices = [43.5, 44, 45, 46, 48, 50, 52, 55, 58, 61]
stop_loss_price = 38.73
profit_threshold = 0.10  # 10%
loss_threshold = 0.03  # 3%
for purchase_price in purchase_price_range:
    print(f"Purchase Price: ${purchase_price:.2f}")
    print("Target Prices:")
    for target_price in target_prices:
        profit_percentage = ((target_price / purchase_price) - 1) * 100
        print(f"  Target Price: ${target_price:.2f} -> Profit: {profit_percentage:.2f}%")

    # print("Stop Loss Price:")
    # loss_percentage = ((stop_loss_price / purchase_price) - 1) * 100
    # print(f"  Stop Loss Price: ${stop_loss_price:.2f} -> Loss: {loss_percentage:.2f}%")
    # print()


# def calculate_percentages(entry_price, profit_pct, loss_pct):
#   """
#   Calculates sell-off prices for profit and stop-loss based on entry price and percentages.

#   Args:
#       entry_price (float): The price at which the coin was purchased.
#       profit_pct (float): The percentage profit to target for sell-off (e.g., 0.1 for 10%).
#       loss_pct (float): The percentage loss to tolerate before selling at a loss (e.g., 0.03 for 3%).

#   Returns:
#       tuple: A tuple containing the sell-off price for profit, stop-loss price, and a dictionary with entry and target prices.
#   """

#   # Calculate sell price for profit
#   profit_price = entry_price * (1 + profit_pct)

#   # Calculate stop-loss price
#   stop_loss_price = entry_price * (1 - loss_pct)

#   # Prepare target prices dictionary
#   target_prices = {
#       "Entry": entry_price
#   }

#   return profit_price, stop_loss_price, target_prices

# # Example usage with adjustable percentages
# entry_price = 41.5
# profit_pct = 0.1  # Adjust for desired profit percentage (e.g., 0.1 for 10%)
# loss_pct = 0.03   # Adjust for desired loss tolerance (e.g., 0.03 for 3%)

# sell_profit, stop_loss, target_prices = calculate_percentages(entry_price, profit_pct, loss_pct)

# print(f"Sell for profit at: ${sell_profit:.2f}")
# print(f"Stop-loss at: ${stop_loss:.2f}")
# print(target_prices)

