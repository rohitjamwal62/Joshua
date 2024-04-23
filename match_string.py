import re

def StopLoss(String):
    Text = str(String).split()[-1]
    return Text

def Entry_Purchage(String):
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

def Filtered_records(string_lower):
    lines = str(string_lower).split('\n')
    pair = None
    entry = None
    for line in lines:
        if line.startswith('pair:'):
            pair = line
        elif line.startswith('entry:'):
            entry = line 
    data = [pair,entry]
    return data