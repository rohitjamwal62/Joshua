

# api_id = 25500977
# api_hash = 7cf41fa26b716a01a46d744758bfbde2
# phone_number = +61483212824


# Replace these with your actual CoinSpot API keys
API_KEY = '65ef7ebac655caceefdb71c419a91202'
API_SECRET = 'T1WG4REYWQA0XK8V7QCP2XGF8NK8BJQ1LR7RGVGHMRBLP22AXQ36K3T1LKGCKD3LB9RUUUUQ2KN6VAM9'

import requests,hashlib,hmac,time,json


BALANCE_URL = 'https://www.coinspot.com.au/api/my/balances'
# BALANCE_URL = "https://www.coinspot.com.au/api/v2/status"
nonce = int(time.time())
params = {
    'nonce': nonce
}
json_params = json.dumps(params, separators=(',' , ':') )
signature = hmac.new(API_SECRET.encode(), json_params.encode(), hashlib.sha512).hexdigest()
headers = {
    'Content-Type': 'application/json',
    'key': API_KEY,
    'sign': signature,

}

response = requests.post(BALANCE_URL, headers=headers, json=params).json()
print(response,"====")

# # Check if request was successful
# if response.status_code == 200:
#     print(response.text,"===")
#     balances = response.json()['balance']
#     print("Your balances:")
#     for currency, amount in balances.items():
#         print(f"{currency}: {amount}")
# else:
#     print("Failed to retrieve balance:", response.text)
