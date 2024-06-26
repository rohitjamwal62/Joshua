import requests,hashlib,hmac,time,json

API_KEY = '65ef7ebac655caceefdb71c419a91202'
API_SECRET = 'T1WG4REYWQA0XK8V7QCP2XGF8NK8BJQ1LR7RGVGHMRBLP22AXQ36K3T1LKGCKD3LB9RUUUUQ2KN6VAM9'

def Buy_Coin(CoinName,Price_Purchage,Check_Live_Price,profit_percent,loss_percent):
    SELL_NOW_URL = 'https://www.coinspot.com.au/api/v2/my/buy/now'
    nonce = int(time.time())
    params = {"nonce": nonce, "cointype": CoinName, "amounttype": "coin", "amount" : Price_Purchage}
    json_params = json.dumps(params, separators=(',' , ':') )
    signature = hmac.new(API_SECRET.encode(), json_params.encode(), hashlib.sha512).hexdigest()
    headers = {
        'Content-Type': 'application/json',
        'key': API_KEY,
        'sign': signature,
    }
    response = requests.post(SELL_NOW_URL, data=json_params, headers=headers).json()
    print("\n")
    print(f"Buy Amount at price : ${Price_Purchage}")
    print(f"Coin Price (At time of purchage): {CoinName.upper()} ${Check_Live_Price}")
    print(f"Profit : {profit_percent}") 
    print(f"Stop loss : {loss_percent}")
    print("\n")
    
def Sell_Coin(CoinName,Price_Purchage):
    SELL_NOW_URL = 'https://www.coinspot.com.au/api/v2/my/sell/now'
    nonce = int(time.time())
    params = {"nonce": nonce, "cointype": CoinName, "amounttype": "coin", "amount" : Price_Purchage}
    json_params = json.dumps(params, separators=(',' , ':') )
    signature = hmac.new(API_SECRET.encode(), json_params.encode(), hashlib.sha512).hexdigest()
    headers = {
    'Content-Type': 'application/json',
    'key': API_KEY,
    'sign': signature,
    }
    response = requests.post(SELL_NOW_URL, data=json_params, headers=headers).json()
    print("Successfully Sell the Coin")

def Get_Current_Coin_Price(CoinName):
    SELL_NOW_URL = 'https://www.coinspot.com.au/api/v2/quote/buy/now'
    nonce = int(time.time())
    params = {"nonce": nonce, "cointype": CoinName, "amounttype": "aud", "amount" : "0.1"}
    json_params = json.dumps(params, separators=(',' , ':') )
    signature = hmac.new(API_SECRET.encode(), json_params.encode(), hashlib.sha512).hexdigest()
    headers = {
        'Content-Type': 'application/json',
        'key': API_KEY,
        'sign': signature,
    }
    response = requests.post(SELL_NOW_URL, data=json_params, headers=headers)
    if response.status_code == 200:
        records = json.loads(response.text).get('rate')
        return records
    else:
        return ''