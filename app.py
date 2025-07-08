import streamlit as st
import datetime
import pandas as pd
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
from utils.graph import plot_mood_trend
from utils.music import play_motivational_music
from utils.voice_input import record_and_transcribe
from utils.auth import login_form, authenticate_user

# --------------------------------------
# 📘 Custom CSS Theme
# --------------------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------
# 🔐 Login / Signup UI
# --------------------------------------
login_form()
if "uid" not in st.session_state:
    st.warning("Please login to use MoodMate features.")
    st.stop()

# 🔑 Logged in user's info
user_uid = st.session_state["uid"]
user_email = st.session_state["email"]
db = st.session_state["db"]  # db reference from auth.py

# --------------------------------------
# 🧭 Navigation
# --------------------------------------
page = st.sidebar.radio("📂 Pages", ["Welcome", "Home", "Achievements", "Mood Tracker"])
st.sidebar.info(f"👤 {user_email}")

# Optional override from session state (used by Get Started button)
if "page" in st.session_state:
    page = st.session_state["page"]
    del st.session_state["page"]

# --------------------------------------
# ⚙️ Settings
# --------------------------------------
st.sidebar.header("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=False)

# --------------------------------------
# 🚀 Welcome Page with Animated Splash & Get Started
# --------------------------------------
if page == "Welcome":
    st.markdown(
        """
        <div class="splash fade-in">
            <h1 class="title">🧠 MoodMate</h1>
            <p class="subtitle">Your AI-Powered Mood Companion & Journal</p>
            <img src="https://cdn-icons-png.flaticon.com/512/4727/4727420.png" class="splash-img">
            <p class="description">Track your moods, stay motivated, and reflect every day.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🚀 Get Started"):
        st.session_state["page"] = "Home"
        st.experimental_rerun()


# --------------------------------------
# 🏠 Home Page
# --------------------------------------

if page == "Home":
    st.title("🧠 MoodMate – Your Mood Companion")
    st.markdown("### 📝 How are you feeling today?")

    user_input = st.text_area("Write something...", placeholder="I'm feeling neutral.")

    if st.button("🎤 Use Voice Input"):
        user_input = record_and_transcribe()
        st.success("Captured voice input!")

    if st.button("🔍 Analyze Mood") and user_input:
        mood, emoji = analyze_mood(user_input)
        st.markdown(f"**Your mood is:** {mood} {emoji}")

        db.child("moods").push({
            "text": user_input,
            "mood": mood,
            "emoji": emoji,
            "user": user_uid,
            "email": user_email,
            "timestamp": str(datetime.datetime.now())
        })

        st.session_state["mood"] = mood

        quote = get_motivational_quote(mood)
        st.info(f"💬 {quote}")

        play_motivational_music(mood)

    st.subheader("📓 Daily Journal")
    journal_text = st.text_area("Write your thoughts for the day")
    if st.button("Save Journal Entry"):
        db.child("journals").push({
            "text": journal_text,
            "user": user_uid,
            "timestamp": str(datetime.datetime.now())
        })
        st.success("📝 Journal entry saved!")

# --------------------------------------
# 🏆 Achievements Page
# --------------------------------------
elif page == "Achievements":
    st.title("🏆 Achievements")
    try:
        moods = db.child("moods").get()
        mood_count = {"Positive": 0, "Neutral": 0, "Negative": 0}
        streak = 0
        last_day = None

        if moods.each():
            sorted_moods = sorted(moods.each(), key=lambda m: m.val().get("timestamp"))
            for m in sorted_moods:
                data = m.val()
                if data.get("user") == user_uid:
                    mood = data.get("mood")
                    if mood in mood_count:
                        mood_count[mood] += 1

                    # Streak Counter
                    ts = pd.to_datetime(data.get("timestamp")).date()
                    if last_day is None or (ts - last_day).days == 1:
                        streak += 1
                    elif (ts - last_day).days > 1:
                        streak = 1
                    last_day = ts

        st.metric("🌟 Mood Streak", f"{streak} days in a row")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.success(f"😊 Positive: {mood_count['Positive']}")
            st.image("https://cdn-icons-png.flaticon.com/512/4201/4201973.png", width=50)
        with col2:
            st.warning(f"😐 Neutral: {mood_count['Neutral']}")
            st.image("https://cdn-icons-png.flaticon.com/512/4201/4201993.png", width=50)
        with col3:
            st.error(f"😞 Negative: {mood_count['Negative']}")
            st.image("https://cdn-icons-png.flaticon.com/512/4201/4201971.png", width=50)

    except Exception as e:
        st.warning("No achievement data available.")
        st.exception(e)

# --------------------------------------
# 📈 Mood Tracker Page
# --------------------------------------
elif page == "Mood Tracker":
    st.title("📈 Mood Trend & Export")
    try:
        moods = db.child("moods").get()
        mood_data = []
        if moods.each():
            for m in moods.each():
                data = m.val()
                if data.get("user") == user_uid and "timestamp" in data and "mood" in data:
                    mood_data.append({
                        "timestamp": pd.to_datetime(data["timestamp"]),
                        "mood": data["mood"],
                        "emoji": data.get("emoji", "")
                    })

        if not mood_data:
            st.info("No mood history found.")
        else:
            df = pd.DataFrame(mood_data)
            mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
            df["mood_value"] = df["mood"].map(mood_map)
            df = df.sort_values("timestamp")

            mood_filter = st.selectbox("Filter by Mood", ["All"] + list(mood_map.keys()))
            if mood_filter != "All":
                df = df[df["mood"] == mood_filter]

            st.bar_chart(df.set_index("timestamp")["mood_value"])

            if st.button("📤 Export to CSV"):
                st.download_button("Download", df.to_csv(index=False), "mood_history.csv")

    except Exception as e:
        st.error("⚠️ Failed to load mood trend data.")
        st.exception(e)
