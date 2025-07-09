# MoodMate: Streamlit-Based Mental Wellness App
# Core file: app.py

import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import login_form, authenticate_user
from utils.journal import mood_journal_page
from utils.chatbot import mental_health_chatbot_page
from utils.dashboard import mood_dashboard_page
from utils.activities import activities_page
from utils.voice_journal import voice_journal_page
from utils.emergency import emergency_alert_button
from utils.landing import show_landing_page_with_animations

st.set_page_config(
    page_title="MoodMate – Smart Mental Wellness Companion",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme customization
st.markdown("""
<style>
    body {
        background-color: #f3f4f6;
    }
    .reportview-container .main .block-container {
        padding: 2rem 2rem 2rem;
        background-color: #ffffff;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.image("assets/logo.png", width=200)

    menu = ["Home", "Mood Journal", "Voice Journal", "Chatbot", "Dashboard", "Activities", "Emergency"]
    choice = option_menu(
        menu_title="MoodMate Navigation",
        options=menu,
        icons=["house", "book", "mic", "robot", "bar-chart", "sun", "exclamation-triangle"],
        menu_icon="heart",
        default_index=0,
        orientation="vertical",
    )

    if choice == "Home":
        show_landing_page()
    elif choice == "Mood Journal":
        mood_journal_page()
    elif choice == "Voice Journal":
        voice_journal_page()
    elif choice == "Chatbot":
        mental_health_chatbot_page()
    elif choice == "Dashboard":
        mood_dashboard_page()
    elif choice == "Activities":
        activities_page()
    elif choice == "Emergency":
        emergency_alert_button()

if __name__ == '__main__':
    main()
