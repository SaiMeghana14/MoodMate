# streamlit_app.py – Streamlit version of MoodMate

import streamlit as st
from transformers import pipeline
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
sentiment_pipeline = pipeline("sentiment-analysis")

st.set_page_config(page_title="MoodMate", page_icon="😊", layout="centered")
st.title("🧠 MoodMate – Your Mental Health Buddy")

user_id = st.text_input("Enter your User ID", value="user123")

# Chat section
st.header("💬 Chat with MoodMate")
user_input = st.text_area("How are you feeling today?", height=100)

if st.button("Send") and user_input.strip():
    result = sentiment_pipeline(user_input)[0]
    mood = "happy" if "positive" in result['label'].lower() else "sad" if "negative" in result['label'].lower() else "neutral"
    
    if mood == "happy":
        response = "I'm glad you're feeling happy today! 😊"
    elif mood == "sad":
        response = "I'm here for you. Want to talk about it? 💙"
    else:
        response = "Tell me more, I'm here to help."

    # Save to Firestore
    db.collection("mood_logs").add({
        "user_id": user_id,
        "message": user_input,
        "response": response,
        "mood": mood,
        "timestamp": datetime.datetime.utcnow()
    })

    st.success(f"🧠 MoodMate: {response} (Mood: {mood})")

# Journal section
st.header("📝 Journal Entry")
journal_input = st.text_area("Write about your day...")

if st.button("Save Journal") and journal_input.strip():
    db.collection("journals").add({
        "user_id": user_id,
        "entry": journal_input,
        "timestamp": datetime.datetime.utcnow()
    })
    st.success("✅ Journal entry saved.")

# Mood history section
st.header("📊 Your Recent Mood History")
if st.button("Refresh History"):
    logs = db.collection("mood_logs").where("user_id", "==", user_id).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(10).stream()
    for log in logs:
        log_data = log.to_dict()
        st.write(f"🗓️ {log_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} – {log_data['mood'].capitalize()} – {log_data['message']}")

st.markdown("---")
st.caption("Made with ❤️ for mental well-being")
