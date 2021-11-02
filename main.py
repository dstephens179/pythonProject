from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'python_key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of the spreadsheet.
sheet_id = '1AkmronHQmdAfpOTwS8MLHGwje9piovifUaddOOnWfZg'
range_name = 'Centro!A:I'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=sheet_id,
                            range=range_name).execute()

values = result.get('values', [])

print(values)
