import requests
import json,re

Client_Id = "319825298674-b4jv0vm504ic4fpt7ub9oc1nms7qpofn.apps.googleusercontent.com"
Client_Secret = "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"
Refresh_Token = "1//04v1HceH5dWmrCgYIARAAGAQSNwF-L9IrGJxlvguiAuYwEW_b-s9LvqDm6pCVFPgiQ1yVJSZBgT8pXuVBYpFiZt1dHj98OWWd1sc"
Sheet_Id = "1L9FR8KVZ6sZplljUZKL6GyHeHERrbTirfdfxJ7uRq_w"

def Access_Token():
    url = "https://oauth2.googleapis.com/token"
    payload = {
        'client_id': Client_Id,
        'client_secret': Client_Secret,
        'refresh_token': Refresh_Token,
        'grant_type': 'refresh_token'
        }
    response = requests.request("POST", url,  data=payload)
    if response.status_code == 200:
        Token = json.loads(response.text).get('access_token')
        return Token
    else:
        print("Token Error")

data = Access_Token()
print(data)


Main_Header = {'Content-Type': 'application/json','Authorization': f'Bearer {Access_Token()}'}


def Create_Row(input_string):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{Sheet_Id}/values/Sheet1!A1:append?valueInputOption=USER_ENTERED"
    payload = json.dumps({
        "values": [
            [input_string]
        ]
    })
    response = requests.request("POST", url, headers=Main_Header, data=payload)
    if response.status_code == 200:
        print("Successfully Create the row")
    
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

def get_sheet_row(pair_live_list):
    Store_data = ''
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{Sheet_Id}/values/Sheet1!A:Z"
    response = requests.get(url, headers=Main_Header)
    if response.status_code == 200:
        data = response.json()
        values = data.get('values', [])
        if values:
            data = [Filtered_records(str(k).lower().replace('\r','').rstrip().replace(' ','')) for row in values for k in row]
            rec = match_lists(pair_live_list,data)
            Store_data = rec
        else:
            print("No data found in the specified row.")
            return None
    else:
        print("Failed to retrieve data from Google Sheets.")
        return None
    return Store_data
