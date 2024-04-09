import re
def StopLoss(String):
    store_list = list()
    stop_loss_pattern = r"STOP LOSS: (\d+\.\d+)"
    stop_loss_match = re.search(stop_loss_pattern, String)
    if stop_loss_match:
        stop_loss_value = stop_loss_match.group(1)
        print("Stop Loss:", stop_loss_value)
        store_list.append(stop_loss_match)
    return stop_loss_value

        
    
    
String = """
Pair: $KSM/USDTDirection: Long
Exchanges: ByBit USDTLeverage: 3x
ENTRY: 40 -41.5 -  42.85
TARGETS: 43.5 - 44 - 45 - 46 - 48 - 50 - 52 - 55 - 58 - 61
STOP LOSS: 38.73
"""
data = StopLoss(String)