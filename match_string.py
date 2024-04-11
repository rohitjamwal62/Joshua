import re
from main import handle_message
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
        
     
    
String = """
Pair: $KSM/USDT
Direction: LonG
Exchanges: ByBit USDTLeverage: 3x
entry: 40.7 -41.5 -  42.85
TARGETS: 43.5 - 44 - 45 - 46 - 48 - 50 - 52 - 55 - 58 - 61
STOP LOSS: 6
"""

# entry = Entry_Purchage(String)
# print(entry,"==")
# def sell_percentage():
    
    



# data = StopLoss(String)
# entry = float(re.findall(r'ENTRY:\s*([\d.-]+)', String)[0])
# print(entry,"===")
# stop_loss = float(re.findall(r'STOP LOSS:\s*([\d.-]+)', String)[0])

# if entry - stop_loss >= 5 and entry - stop_loss <= 10:
#     print("yess")
    
# - I can adjust the parameters myself (i.e. stop loss percentage from 3% to 10%, or the profit sell off from 10% to 20% of purchase price)

    


