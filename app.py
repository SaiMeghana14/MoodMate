# ✅ Updated app.py
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import json
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote

# Streamlit page config
st.set_page_config(page_title="🧠 MoodMate", page_icon="🔠", layout="centered")
st.title("\U0001f9e0 MoodMate – Your Mood Companion")

# -------------------------------
# Firebase initialization
# -------------------------------
if not firebase_admin._apps:
    firebase_config = dict(st.secrets["firebase"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

try:
    db = firestore.client()
    docs = db.collection("mood_entries").limit(1).stream()
    for doc in docs:
        st.success(f"✅ Firestore read success: {doc.id}")
except Exception as e:
    st.error(f"🚨 Firestore access error: {e}")

# -------------------------------
# Toggle Online/Offline Mode
# -------------------------------
st.sidebar.header("Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=True)

# -------------------------------
# User Input
# -------------------------------
st.subheader("\U0001f4dd How are you feeling today?")
user_input = st.text_area("", placeholder="I'm feeling happy/sad/neutral...")

if st.button("\U0001f50d Analyze Mood") and user_input:
    mood, emoji = analyze_mood(user_input, use_openai)

    st.markdown(f"### Your mood is: **{mood}** {emoji}")

    quote = get_motivational_quote(mood)
    st.info(f"\U0001f4ac Motivation: {quote}")

    # Save to Firebase (basic only)
    doc_ref = db.collection("moods").add({
        "text": user_input,
        "mood": mood,
        "emoji": emoji,
        "timestamp": firestore.SERVER_TIMESTAMP
    })

    st.success("Mood recorded successfully! ")

# -------------------------------
# View Mood History
# -------------------------------
if st.checkbox("Show Mood History"):
    docs = db.collection("moods").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    history = [{"Text": doc.to_dict()["text"], "Mood": doc.to_dict()["mood"], "Emoji": doc.to_dict()["emoji"]} for doc in docs]
    st.table(pd.DataFrame(history))
