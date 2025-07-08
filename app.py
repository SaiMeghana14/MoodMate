import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
from utils.music import recommend_music
from utils.voice_input import transcribe_voice
from utils.auth import user_login
from utils.graph import plot_mood_trend
import pandas as pd
import datetime

# Set Streamlit page config
st.set_page_config(page_title="MoodMate", page_icon="🧠")

# -------------------------------
# 🔐 Firebase Initialization
# -------------------------------
firebase_config = dict(st.secrets["firebase"])
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# -------------------------------
# 👤 User Login
# -------------------------------
user = user_login()
if not user:
    st.stop()

# -------------------------------
# 🎙️ Voice or Text Input
# -------------------------------
st.title("🧠 MoodMate – Your Mood Companion")
input_mode = st.radio("Choose Input Mode:", ["📝 Text", "🎤 Voice"])

user_input = ""
if input_mode == "📝 Text":
    user_input = st.text_area("How are you feeling today?")
elif input_mode == "🎤 Voice":
    user_input = transcribe_voice()

# -------------------------------
# 💬 Chatbot Toggle
# -------------------------------
chatbot_mode = st.toggle("Enable AI Chatbot Response")

# -------------------------------
# 🧠 Analyze Mood
# -------------------------------
if st.button("🔍 Analyze Mood") and user_input:
    mood, emoji = analyze_mood(user_input)
    st.subheader(f"Your mood is {mood} {emoji}")

    # 🔖 Motivational Quote
    quote = get_motivational_quote(mood)
    st.info(f"💡 Motivation: {quote}")

    # 🎶 Music Suggestion
    track = recommend_music(mood)
    st.audio(track)

    # 🗒️ Save Entry
    entry = {
        "text": user_input,
        "mood": mood,
        "emoji": emoji,
        "timestamp": datetime.datetime.now(),
        "user": user
    }
    db.collection("mood_entries").add(entry)

# -------------------------------
# 📈 Mood History Graph
# -------------------------------
st.markdown("---")
st.subheader("📊 Mood Trend")

# 🔍 View Mood History with Trend
docs = db.collection("moods").where("user", "==", user).stream()
history_data = []

for doc in docs:
    doc_dict = doc.to_dict()
    if "timestamp" in doc_dict and "mood" in doc_dict:
        history_data.append({
            "timestamp": doc_dict["timestamp"],
            "mood": doc_dict["mood"]
        })

if history_data:
    history_data.sort(key=lambda x: x["timestamp"])  # (Optional)
    plot_mood_trend(history_data)
else:
    st.info("No mood history found to plot.")

# -------------------------------
# 📓 Daily Journal
# -------------------------------
st.subheader("📓 Daily Journal")
journal_text = st.text_area("Write your thoughts for the day")
if st.button("Save Journal Entry"):
    db.collection("journals").add({"text": journal_text, "user": user, "timestamp": datetime.datetime.now()})
    st.success("📝 Journal entry saved!")
