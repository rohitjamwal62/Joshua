import re
def StopLoss(String):
    Text = str(String).split()[-1]
    return Text

        
    
    
String = """
Pair: $KSM/USDTDirection: Long
Exchanges: ByBit USDTLeverage: 3x
ENTRY: 40 -41.5 -  42.85
TARGETS: 43.5 - 44 - 45 - 46 - 48 - 50 - 52 - 55 - 58 - 61
STOP LOSS: 6
"""
data = StopLoss(String)
entry = float(re.findall(r'ENTRY:\s*([\d.-]+)', String)[0])
print(entry,"===")
stop_loss = float(re.findall(r'STOP LOSS:\s*([\d.-]+)', String)[0])

if entry - stop_loss >= 5 and entry - stop_loss <= 10:
    print("yess")
    
# - I can adjust the parameters myself (i.e. stop loss percentage from 3% to 10%, or the profit sell off from 10% to 20% of purchase price)

    
