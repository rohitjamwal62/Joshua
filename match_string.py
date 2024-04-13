import re

def StopLoss(String):
    Text = str(String).split()[-1]
    return Text

def Entry_Purchage(String):
    print("yess")
    Purchage_Entry = 0
    pattern = r"entry:\s*([\d\.\s-]+)"
    match = re.search(pattern, String)
    if match:
        entry_values = match.group(1).split()
        entry = [value.replace('-','') for value in entry_values if value !='-']
        min_value = min(entry)
        Purchage_Entry = min_value
    
    return Purchage_Entry
        
def Coin_Name(String):
    Coin = str(String).split('$')[1].split('/')[0].strip()
    return Coin
    
String = """
Pair: $KSM/USDT
Direction: LonG
Exchanges: ByBit USDTLeverage: 3x
entry: 40.7 -41.5 -  42.85
TARGETS: 43.5 - 44 - 45 - 46 - 48 - 50 - 52 - 55 - 58 - 61
STOP LOSS: 6
"""

