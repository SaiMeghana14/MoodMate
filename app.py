import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
import pandas as pd

# -------------------
# 🎨 App Config
# -------------------
st.set_page_config(page_title="MoodMate", page_icon="🧠")
st.title("🧠 MoodMate – Your Mood Companion")

# -------------------------------
# 🔐 Firebase Initialization
# -------------------------------
firebase_config = {
    "type": st.secrets["firebase"]["type"],
    "project_id": st.secrets["firebase"]["project_id"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
    "universe_domain": st.secrets["firebase"]["universe_domain"]
}
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# -------------------
# ⚙️ Sidebar Settings
# -------------------
st.sidebar.title("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=True)

# -------------------
# 🗣️ Mood Input
# -------------------
user_input = st.text_area("📝 How are you feeling today?", height=100)

if st.button("🔍 Analyze Mood"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        mood, emoji = analyze_mood(user_input, use_openai)
        st.success(f"Your mood is **{mood}** {emoji}")

        # Optional: Show motivational quote
        if mood != "Positive":
            quote = get_motivational_quote()
            st.markdown(f"💡 *{quote}*")

        # Log to Firestore
        doc_ref = db.collection("mood_logs").document()
        doc_ref.set({
            "text": user_input,
            "mood": mood,
            "emoji": emoji,
            "mode": "OpenAI" if use_openai else "Offline",
            "timestamp": firestore.SERVER_TIMESTAMP
        })
