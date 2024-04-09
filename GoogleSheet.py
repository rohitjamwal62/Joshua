import requests
import json,re

Client_Id = "319825298674-b4jv0vm504ic4fpt7ub9oc1nms7qpofn.apps.googleusercontent.com"
Client_Secret = "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"
Refresh_Token = "1//04E3wbyeZS5TwCgYIARAAGAQSNwF-L9Ir3VZDnSLYI0Qg0ixShTsA2iDK1n9BgTxUCHAVXP4WPwKdH1xgmFR6521QJTQatdWE8LE"
Base_Url = ""
Sheet_Id = "1t6v6f6BgUumwspwURDJVhi_3b_FyYH3a4xXWIdhIunw"

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

Main_Header = {'Content-Type': 'application/json','Authorization': f'Bearer {Access_Token()}'}


def Create_Row(input_string):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{Sheet_Id}/values/Sheet1!A1:append?valueInputOption=USER_ENTERED"
    payload = json.dumps({
        "values": [
            [input_string]
        ]
    })
    response = requests.request("POST", url, headers=Main_Header, data=payload)
    print(response.text)

def get_sheet_row(row_number):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{Sheet_Id}/values/Sheet1!A{row_number}:Z{row_number}"
    response = requests.get(url, headers=Main_Header)
    if response.status_code == 200:
        data = response.json()
        values = data.get('values', [])
        if values:
            return values[0]  # Assuming you're retrieving a single row
        else:
            print("No data found in the specified row.")
            return None
    else:
        print("Failed to retrieve data from Google Sheets.")
        return None
