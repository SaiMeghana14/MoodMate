import streamlit as st
from utils.landing import show_landing_page_with_animations
from utils.mood_journal import mood_journal_page
from utils.voice_journal import voice_journal_page
from utils.chatbot import chatbot_page
from utils.dashboard import dashboard_page
from utils.activities import activities_page
from utils.therapy_bot import therapy_bot_page
from utils.gamification import gamification_page
from utils.emergency import emergency_page
from utils.privacy import privacy_settings_page
from utils.lang_support import language_settings_page
from utils.mood_predictor import mood_predictor_page

# Sidebar Menu
st.sidebar.title("🧠 MoodMate Navigation")
menu = [
    "Home", "Mood Journal", "Voice Journal", "Chatbot", "Dashboard",
    "Activities", "Therapy Bot", "Gamification", "Emergency",
    "Privacy", "Language", "Mood Predictor"
]
choice = st.sidebar.radio("Go to", menu)

# Routing Logic
if choice == "Home":
    show_landing_page_with_animations()
elif choice == "Mood Journal":
    mood_journal_page()
elif choice == "Voice Journal":
    voice_journal_page()
elif choice == "Chatbot":
    chatbot_page()
elif choice == "Dashboard":
    dashboard_page()
elif choice == "Activities":
    activities_page()
elif choice == "Therapy Bot":
    therapy_bot_page()
elif choice == "Gamification":
    gamification_page()
elif choice == "Emergency":
    emergency_page()
elif choice == "Privacy":
    privacy_settings_page()
elif choice == "Language":
    language_settings_page()
elif choice == "Mood Predictor":
    mood_predictor_page()
