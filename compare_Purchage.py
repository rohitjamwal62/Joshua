import requests,json,time
API_KEY = '65ef7ebac655caceefdb71c419a91202'
API_SECRET = 'T1WG4REYWQA0XK8V7QCP2XGF8NK8BJQ1LR7RGVGHMRBLP22AXQ36K3T1LKGCKD3LB9RUUUUQ2KN6VAM9'

def get_coin_price():
    url = "https://www.coinspot.com.au/pubapi/latest"
    response = requests.get(url)
    data = response.json()
    
#     print(data,"====")
# data = get_coin_price( )
# # Function to sell coin
# def sell_coin():
#     url = "https://www.coinspot.com.au/api/ro/my/balance"
#     payload = {
#         "cointype": "BTC",  # Replace 'BTC' with your coin symbol
#         "amount": "all",
#         "rate": 70,  # Sell at $70
#         "withdraw": "false"
#     }
#     headers = {
#         "Content-Type": "application/json",
#         "key": API_KEY,
#         "sign": API_SECRET
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     return response.json()

# # Main loop
# while True:
#     current_price = get_coin_price()
#     print("Current price:", current_price)
    
#     if current_price >= 70:
#         print("Selling coin...")
#         sell_response = sell_coin()
#         print("Sell response:", sell_response)
#         break  # Exit the loop after selling
    
#     time.sleep(60)  # Check price every minute
