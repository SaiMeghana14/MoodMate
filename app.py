# moodmate/app.py
import streamlit as st
from utils.auth import login_form, authenticate_user
from utils.mood import detect_mood
from utils.journal import save_entry, get_entries
from utils.dashboard import plot_mood_trends
from utils.bot import chat_with_bot
from utils.suggestions import get_suggestions
import datetime

st.set_page_config(page_title="MoodMate – Your AI Buddy", layout="centered")

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🌈 MoodMate – Your AI Mental Health Buddy</h1>", unsafe_allow_html=True)

# Authenticate User
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_form()
else:
    st.sidebar.success("Logged in")
    menu = ["Mood Journal", "Dashboard", "MoodBot", "Activities"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Mood Journal":
        st.subheader("📝 Mood Journal")
        entry = st.text_area("How are you feeling today?", height=200)
        if st.button("Submit Entry"):
            mood = detect_mood(entry)
            save_entry(entry, mood)
            st.success(f"Your entry has been saved! Detected mood: {mood}")

    elif choice == "Dashboard":
        st.subheader("📊 Your Mood Dashboard")
        plot_mood_trends()

    elif choice == "MoodBot":
        st.subheader("🤖 Talk to MoodBot")
        user_input = st.text_input("You:")
        if user_input:
            response = chat_with_bot(user_input)
            st.markdown(f"**MoodBot:** {response}")

    elif choice == "Activities":
        st.subheader("💡 Personalized Suggestions")
        mood = st.selectbox("Choose your current mood", ["Happy", "Sad", "Anxious", "Tired", "Neutral"])
        suggestions = get_suggestions(mood)
        for s in suggestions:
            st.markdown(f"- {s}")
