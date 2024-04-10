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

# Example usage
def main():
    purchase_prices = [40, 41.5, 42.85]
    profit_percent = 20  # Default profit percentage
    loss_percent = 10  # Default loss percentage

    for purchase_price in purchase_prices:
        profit_price, loss_price = calculate_sell_off_prices(purchase_price, profit_percent, loss_percent)
        profit, loss = calculate_profit_and_loss(purchase_price, profit_price)
        profit_percentage = calculate_percentage_change(purchase_price, profit_price)
        loss_percentage = calculate_percentage_change(purchase_price, loss_price)

        print(f"Purchase Price: {purchase_price}")
        print(f"Sell-off price for profit: {profit_price:.2f}")
        print(f"Sell-off price for loss: {loss_price:.2f}")
        print(f"Profit: ${profit:.2f}")
        print(f"Loss: ${loss:.2f}")
        print(f"Profit Percentage: {profit_percentage:.2f}%")
        print(f"Loss Percentage: {loss_percentage:.2f}%")
        print()

if __name__ == "__main__":
    main()