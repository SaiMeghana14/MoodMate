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
from utils.auth import login_form, signup_form
from utils.daily_journal import daily_journal_page
from utils.mood_tracker import mood_tracker_page
from utils.achievements import achievements_page

# Show login first
if "user" not in st.session_state:
    st.sidebar.title("🔐 Authentication")
    auth_choice = st.sidebar.radio("Login or Signup", ["Login", "Signup"])
    if auth_choice == "Login":
        if not login_form():
            st.stop()
    else:
        signup_form()
        st.stop()

# Sidebar Menu
st.sidebar.title("🧠 MoodMate Navigation")
menu = [
    "Home", "Daily Journal", "Mood Tracker", "Achievements",
    "Voice Journal", "Chatbot", "Dashboard", "Activities", "Therapy Bot", "Gamification", "Emergency", "Privacy", "Language", "Mood Predictor"
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
elif choice == "Daily Journal":
    daily_journal_page()
elif choice == "Mood Tracker":
    mood_tracker_page()
elif choice == "Achievements":
    achievements_page()
