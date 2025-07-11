import datetime
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import streamlit as st

# Define the scope (Google Calendar API)
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# Get or refresh Google credentials
def get_credentials():
    creds = None
    token_path = 'token.pickle'
    credentials_path = 'credentials.json'

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                st.error("Missing credentials.json file. Please provide OAuth credentials.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Add event to calendar
def add_journal_reminder():
    creds = get_credentials()
    if not creds:
        return

    try:
        service = build('calendar', 'v3', credentials=creds)

        today = datetime.date.today()
        start_time = datetime.datetime.combine(today, datetime.time(21, 0))  # 9:00 PM today
        end_time = start_time + datetime.timedelta(minutes=15)

        event = {
            'summary': '📝 MoodMate Journal Reminder',
            'description': 'Time to reflect on your day with MoodMate!',
            'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                    {'method': 'email', 'minutes': 15},
                ],
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        st.success(f"📅 Event added: {event.get('htmlLink')}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
