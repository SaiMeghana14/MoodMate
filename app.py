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

# ✅ Load CSS styling
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Main App Logic
st.set_page_config(page_title="MoodMate", layout="wide")
st.title("🧠 MoodMate – Your AI-Powered Mental Health Buddy")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("Login"):
        username, password = login_form()
        submit = st.form_submit_button("Login")
        if submit and authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success("Login successful!")
        elif submit:
            st.error("Invalid credentials")
else:
    st.sidebar.success("Logged in")
    menu = ["Mood Journal", "Dashboard", "MoodBot", "Activities", "Meditation", "Achievements"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Journal":
        st.subheader("📝 Daily Journal")
        st.markdown("<div class='frame'>", unsafe_allow_html=True)
        journal_entry()
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("📤 Export Journal as PDF"):
            export_pdf()

    
    elif choice == "Dashboard":
        st.subheader("📊 Mood Insights")
        st.markdown("<div class='frame'>", unsafe_allow_html=True)
        plot_mood_trends()
        mood_heatmap()
        show_wordcloud()
        st.markdown("</div>", unsafe_allow_html=True)

    elif choice == "MoodBot":
        st.subheader("🤖 Talk to MoodBot")
        user_input = st.text_input("You:")
        if user_input:
            response = chat_with_bot(user_input)
            st.markdown(f"**MoodBot:** {response}")

     elif choice == "Activities":
        st.subheader("🧠 Mood-Boosting Activities")

        st.markdown("<div class='frame mood-card neutral'>", unsafe_allow_html=True)
        gratitude_spinner()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='frame mood-card happy'>", unsafe_allow_html=True)
        journal_prompt()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='frame mood-card anxious'>", unsafe_allow_html=True)
        uplifting_quote()
        st.markdown("</div>", unsafe_allow_html=True)
         
    elif choice == "Meditation":
        st.subheader("🧘‍♀️ Mindfulness Zone")
        breathing_exercise()
        play_meditation()

    elif choice == "Achievements":
        st.subheader("🏅 Your Emotional Growth")
        show_achievements()
