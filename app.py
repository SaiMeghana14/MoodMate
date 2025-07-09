import streamlit as st
import datetime
import pandas as pd
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
from utils.graph import plot_mood_trend
from utils.music import play_motivational_music
from utils.voice_input import record_and_transcribe
from utils.auth import login_form, authenticate_user

import os
import sys
st.write("Current Directory:", os.getcwd())
st.write("Python Path:", sys.path)


# --------------------------------------
# 📘 Custom CSS Theme
# --------------------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------
# 🔐 Login / Signup
# --------------------------------------
login_form()
if "uid" not in st.session_state:
    st.warning("Please login to use MoodMate features.")
    st.stop()

# 🔑 Logged in user's info
user_uid = st.session_state["uid"]
user_email = st.session_state["email"]
db = st.session_state["db"]  # Firebase DB reference from auth.py

# --------------------------------------
# 🧭 Navigation Pages
# --------------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "Welcome"

# Sidebar nav
page = st.sidebar.radio("📂 Pages", ["Welcome", "Home", "Achievements", "Mood Tracker"])
st.sidebar.info(f"👤 {user_email}")

# --------------------------------------
# ⚙️ Settings
# --------------------------------------
st.sidebar.header("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=False)

# --------------------------------------
# 🙌 Welcome Page
# --------------------------------------
if page == "Welcome":
    st.markdown("<h1 class='fade-in'>🧠 Welcome to MoodMate!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='fade-in'>Your personal AI-powered mood companion.</p>", unsafe_allow_html=True)
    st.image("assets/moodmate_cover.png", use_column_width=True)

    if st.button("✨ Get Started"):
        st.session_state["page"] = "Home"
        st.experimental_rerun()

# --------------------------------------
# 🏠 Home Page
# --------------------------------------
elif page == "Home":
    st.title("🧠 MoodMate – Your Mood Companion")
    st.markdown("### 📝 How are you feeling today?")

    user_input = st.text_area("Write something...", placeholder="I'm feeling neutral.")

    if st.button("🎤 Use Voice Input"):
        user_input = record_and_transcribe()
        st.success("Captured voice input!")

    if st.button("🔍 Analyze Mood") and user_input:
        with st.spinner("Analyzing your mood..."):
            mood, emoji = analyze_mood(user_input)
            st.markdown(f"**Your mood is:** {mood} {emoji}")

            # Save mood with UID
            db.child("moods").push({
                "text": user_input,
                "mood": mood,
                "emoji": emoji,
                "user": user_uid,
                "email": user_email,
                "timestamp": str(datetime.datetime.now())
            })

            st.session_state["mood"] = mood

            # Motivational content
            quote = get_motivational_quote(mood)
            st.info(f"💬 {quote}")
            play_motivational_music(mood)

    # -------------------------------
    # 📓 Daily Journal
    # -------------------------------
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
# 🏆 Achievements Page with Streak Counter
# --------------------------------------
elif page == "Achievements":
    st.title("🏆 Achievements")
    try:
        moods = db.child("moods").get()
        mood_count = {"Positive": 0, "Neutral": 0, "Negative": 0}
        date_set = set()

        if moods.each():
            for m in moods.each():
                data = m.val()
                if data.get("user") == user_uid:
                    mood = data.get("mood")
                    timestamp = data.get("timestamp")
                    if mood in mood_count:
                        mood_count[mood] += 1
                    if timestamp:
                        date = pd.to_datetime(timestamp).date()
                        date_set.add(date)

        # 🌟 Calculate Streak
        today = datetime.date.today()
        streak = 0
        for i in range(100):  # Check up to 100 past days
            check_date = today - datetime.timedelta(days=i)
            if check_date in date_set:
                streak += 1
            else:
                break

        # 🎖️ Display Metrics
        st.metric("🔥 Current Streak", f"{streak} day(s)")
        st.metric("😊 Positive Days", mood_count["Positive"])
        st.metric("😐 Neutral Days", mood_count["Neutral"])
        st.metric("😞 Negative Days", mood_count["Negative"])

        # 🎖️ Streak Badges
        if streak >= 3:
            st.success("🏅 You're on a 3+ day mood streak!")
        if streak >= 7:
            st.success("🎖️ Amazing! 7-Day Mood Check-In Streak!")
        if streak >= 30:
            st.balloons()
            st.success("🌟 Legendary! 30-Day Mood Streak Unlocked!")

    except Exception as e:
        st.warning("No achievement data available.")
        st.exception(e)


# --------------------------------------
# 📈 Mood Tracker Page
# --------------------------------------
elif page == "Mood Tracker":
    st.title("📈 Mood Tracker & Export")
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

            mood_filter = st.selectbox("🎯 Filter by Mood", ["All"] + list(mood_map.keys()))
            if mood_filter != "All":
                df = df[df["mood"] == mood_filter]

            st.bar_chart(df.set_index("timestamp")["mood_value"])

            # Export CSV
            if st.button("📤 Export to CSV"):
                st.download_button("Download", df.to_csv(index=False), "mood_history.csv")

    except Exception as e:
        st.error("⚠️ Failed to load mood trend data.")
        st.exception(e)
