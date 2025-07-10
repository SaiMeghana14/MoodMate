import nltk

# Ensure VADER lexicon is available
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')
    
import streamlit as st
from landing_page import show_landing_page_with_animations
from utils.mood_journal import mood_journal_app
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
from utils.mood_tracker import mood_tracker_page
from utils.achievements import achievements_page
from utils.meditation import show_breathing_animation
from utils.dashboard_utils import plot_mood_line_chart, plot_sentiment_bar_chart
from utils.calendar_sync import show_calendar_integration


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

import streamlit as st

# Display logo (adjust path if needed)
st.image("assets/logo.png", width=200)

# Optional: App title and slogan
st.markdown("## MoodMate")
st.caption("Your Mind’s Best Mate")
# Centered Logo, Title, and Slogan
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/logo.png", width=200)
    st.markdown("### MoodMate")
    st.caption("Your Mind’s Best Mate")

# Sidebar Menu
st.sidebar.title("🧠 MoodMate Navigation")
menu = [
    "Home", "Mood Journal", "Mood Tracker", "Achievements", "Chatbot", "Dashboard", "Activities", "Therapy Bot", 
    "Gamification", "Emergency", "Privacy", "Language", "Mood Predictor", "Meditation", "Mood Dashboard", "Calendar Sync"
]
choice = st.sidebar.radio("Go to", menu)

# Routing Logic
if choice == "Home":
    show_landing_page_with_animations()
elif choice == "Mood Journal":
    mood_journal_page()
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
elif choice == "Mood Tracker":
    mood_tracker_page()
elif choice == "Achievements":
    achievements_page()
elif choice == "Meditation":
    show_breathing_animation()
elif choice == "Mood Dashboard":
    user_data = load_user_data(username)
    journals = user_data.get("journals", {})
    plot_mood_line_chart(journals)
    plot_sentiment_bar_chart(journals)
elif choice == "Calendar Sync":
    show_calendar_integration()
