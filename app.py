import streamlit as st
import datetime
import pandas as pd
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
from utils.graph import plot_mood_trend
from utils.music import play_motivational_music
from utils.voice_input import record_and_transcribe
from utils.auth import login_form, authenticate_user
import firebase_admin
from firebase_admin import credentials, firestore
import base64

# ------------------
# 🎨 Custom CSS Theme
# ------------------
def load_custom_css():
    css = """
    <style>
        .main {background-color: #f5f7fa;}
        .stApp {padding: 1rem;}
        .sidebar .sidebar-content {background-color: #e6f2ff;}
        .st-bb {border-radius: 0.5rem; padding: 1rem;}
        .stButton>button {border-radius: 8px; background-color: #4a90e2; color: white; font-weight: bold;}
        .stButton>button:hover {background-color: #357ABD;}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_custom_css()

# ------------------------
# 🔐 Firebase Initialization
# ------------------------
firebase_config = dict(st.secrets["firebase"])
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# ------------------------
# 👤 Login & Auth Check
# ------------------------
login_form()
if "uid" not in st.session_state:
    st.warning("Please login to use MoodMate features.")
    st.stop()
user_uid = st.session_state["uid"]
user_email = st.session_state["email"]

# -----------------------------
# 🧭 Sidebar Navigation (Dashboard)
# -----------------------------
st.sidebar.title("🧠 MoodMate Dashboard")
page = st.sidebar.radio("Go to", ["Mood Tracker", "Mood History", "Journal", "Achievements"])

# ----------------------------
# ⚙️ Settings (OpenAI Toggle)
# ----------------------------
st.sidebar.header("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=False)

# ----------------------------
# 📘 Mood Tracker Page
# ----------------------------
if page == "Mood Tracker":
    st.title("📝 How are you feeling today?")
    user_input = st.text_area("Write something...", placeholder="I'm feeling neutral.")

    if st.button("🎤 Use Voice Input"):
        user_input = record_and_transcribe()
        st.success("Captured voice input!")

    if st.button("🔍 Analyze Mood") and user_input:
        mood, emoji = analyze_mood(user_input, use_openai)
        st.markdown(f"### Your mood is **{mood}** {emoji}")

        quote = get_motivational_quote(mood)
        st.info(f"💬 {quote}")

        play_motivational_music(mood)

        db.collection("moods").add({
            "text": user_input,
            "mood": mood,
            "emoji": emoji,
            "user": user_uid,
            "email": user_email,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

# ----------------------------
# 📊 Mood History Page
# ----------------------------
elif page == "Mood History":
    st.title("📊 Your Mood History")

    try:
        docs = db.collection("moods").where("user", "==", user_uid).stream()
        mood_data = []

        for doc in docs:
            data = doc.to_dict()
            if "timestamp" in data and "mood" in data:
                mood_data.append({
                    "timestamp": pd.to_datetime(data["timestamp"].isoformat()),
                    "mood": data["mood"],
                    "emoji": data.get("emoji", "")
                })

        if mood_data:
            df = pd.DataFrame(mood_data).sort_values("timestamp")
            df["mood_icon"] = df["emoji"] + " " + df["mood"]
            st.dataframe(df[["timestamp", "mood_icon"]].rename(columns={"mood_icon": "Mood"}))

            st.download_button("📥 Download as CSV", df.to_csv(index=False), "mood_history.csv")

            plot_mood_trend(user_uid, db)
        else:
            st.info("No mood history found.")
    except Exception as e:
        st.error("⚠️ Failed to load mood history.")
        st.exception(e)

# ----------------------------
# 📓 Journal Page
# ----------------------------
elif page == "Journal":
    st.title("📓 Daily Journal")
    journal_text = st.text_area("Write your thoughts for the day")
    if st.button("Save Journal Entry"):
        db.collection("journals").add({
            "text": journal_text,
            "user": user_uid,
            "timestamp": datetime.datetime.now()
        })
        st.success("📝 Journal entry saved!")

    st.markdown("### 📚 Past Entries")
    entries = db.collection("journals").where("user", "==", user_uid).order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    for entry in entries:
        data = entry.to_dict()
        st.markdown(f"**{data['timestamp'].strftime('%Y-%m-%d %H:%M')}**: {data['text']}")

# ----------------------------
# 🏆 Achievements Page
# ----------------------------
elif page == "Achievements":
    st.title("🏆 Your MoodMate Achievements")
    st.markdown("### 🎯 Based on your mood tracking:")

    docs = db.collection("moods").where("user", "==", user_uid).stream()
    mood_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    total = 0
    for doc in docs:
        mood = doc.to_dict().get("mood")
        if mood in mood_counts:
            mood_counts[mood] += 1
            total += 1

    if total:
        st.metric("Total Moods Tracked", total)
        st.metric("😊 Positive Days", mood_counts["Positive"])
        st.metric("😐 Neutral Days", mood_counts["Neutral"])
        st.metric("☹️ Negative Days", mood_counts["Negative"])

        if mood_counts["Positive"] >= 5:
            st.success("🏅 Positivity Badge Unlocked!")
        if total >= 10:
            st.success("🌟 Consistency Badge Unlocked!")
    else:
        st.info("Track your mood to unlock achievements!")
