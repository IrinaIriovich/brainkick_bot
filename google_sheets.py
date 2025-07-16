import os
import gspread
import datetime
import json
from oauth2client.service_account import ServiceAccountCredentials


def get_gspread_client():
    creds_dict = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    return gspread.authorize(creds)


def record_response(user_id, answer):
    client = get_gspread_client()
    sheet = client.open_by_key(os.getenv("SPREADSHEET_ID")).sheet1
    sheet.append_row([str(datetime.datetime.now()), str(user_id), answer])