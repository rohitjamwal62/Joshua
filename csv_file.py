import csv
CSV_FILE_PATH = 'trade_data.csv'  # Path to your CSV file

def Filtered_records(string_lower):
    lines = string_lower.split('\n')
    pair = None
    entry = None
    for line in lines:
        if line.startswith('pair:'):
            pair = line
        elif line.startswith('entry:'):
            entry = line 
    data = [pair,entry]
    return data

def match_lists(lista, listb):
    for sublist in listb:
        if sublist == lista:
            return True
    return False

def Create_Row(input_string):
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input_string])
        print("Successfully created the row in the CSV file")
 
def read_trade_data(pair_live_list):
    Store_data = ''
    with open(CSV_FILE_PATH, mode='r', newline='') as file:
        values = csv.reader(file)
        if values:
            data = [Filtered_records(str(k).lower().replace('\r','').rstrip().replace(' ','')) for row in values for k in row]
            rec = match_lists(pair_live_list,data)
            Store_data = rec
        else:
            print("No data found in the specified row.")
            return None
        return Store_data

# read_trade_data()
