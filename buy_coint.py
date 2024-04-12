import requests,hashlib,hmac,time,json

API_KEY = '65ef7ebac655caceefdb71c419a91202'
API_SECRET = 'T1WG4REYWQA0XK8V7QCP2XGF8NK8BJQ1LR7RGVGHMRBLP22AXQ36K3T1LKGCKD3LB9RUUUUQ2KN6VAM9'

def Buy_Coin(CoinName,Price_Purchage):
    SELL_NOW_URL = 'https://www.coinspot.com.au/api/v2/my/buy/now'
    nonce = int(time.time())
    params = {"nonce": nonce, "cointype": CoinName, "amounttype": "coin", "amount" : "0.1"}
    json_params = json.dumps(params, separators=(',' , ':') )
    signature = hmac.new(API_SECRET.encode(), json_params.encode(), hashlib.sha512).hexdigest()
    headers = {
        'Content-Type': 'application/json',
        'key': API_KEY,
        'sign': signature,
    }
    response = requests.post(SELL_NOW_URL, data=json_params, headers=headers).json()
    print(response)