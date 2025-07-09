# app.py – MoodMate with Premium Features
import streamlit as st
from utils.auth import login_form, authenticate_user
from utils.mood import detect_mood
from utils.journal import save_entry, get_entries, export_pdf
from utils.dashboard import plot_mood_trends, show_wordcloud, mood_heatmap
from utils.bot import chat_with_bot
from utils.suggestions import get_suggestions
from utils.meditation import play_meditation, breathing_exercise
from utils.gamify import show_achievements, update_streaks
from utils.ui import set_theme_by_mood
import datetime

st.set_page_config(page_title="MoodMate – Your AI Buddy", layout="centered")

# Load style sheet
try:
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ Custom CSS file not found. Using default styles.")

st.markdown("<h1 class='title'>🌈 MoodMate – Your AI Mental Health Buddy</h1>", unsafe_allow_html=True)

# Authenticate User
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_form()
else:
    st.sidebar.success("Logged in")
    menu = ["Mood Journal", "Dashboard", "MoodBot", "Activities", "Meditation", "Achievements"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Mood Journal":
        st.subheader("📝 Mood Journal")
        entry = st.text_area("How are you feeling today?", height=200)
        if st.button("Submit Entry"):
            mood = detect_mood(entry)
            save_entry(entry, mood)
            st.success(f"Your entry has been saved! Detected mood: {mood}")
            set_theme_by_mood(mood)
            update_streaks(mood)

        if st.button("📤 Export Journal as PDF"):
            export_pdf()

    elif choice == "Dashboard":
        st.subheader("📊 Your Mood Dashboard")
        plot_mood_trends()
        mood_heatmap()
        show_wordcloud()

    elif choice == "MoodBot":
        st.subheader("🤖 Talk to MoodBot")
        user_input = st.text_input("You:")
        if user_input:
            response = chat_with_bot(user_input)
            st.markdown(f"**MoodBot:** {response}")

    elif choice == "Activities":
        st.subheader("🧠 Mood-Boosting Activities")
        st.markdown("<div class='mood-card neutral'>", unsafe_allow_html=True)
        from utils.activities import gratitude_spinner, journal_prompt, uplifting_quote
        gratitude_spinner()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='mood-card happy'>", unsafe_allow_html=True)
        journal_prompt()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='mood-card anxious'>", unsafe_allow_html=True)
        uplifting_quote()
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "Meditation":
        st.subheader("🧘‍♀️ Mindfulness Zone")
        breathing_exercise()
        play_meditation()

    elif choice == "Achievements":
        st.subheader("🏅 Your Emotional Growth")
        show_achievements()
