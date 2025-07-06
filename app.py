import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote

# 🧠 App config
st.set_page_config(page_title="MoodMate", page_icon="🧠")

# -----------------------------------
# 🔐 Firebase Initialization
# -----------------------------------
firebase_config = dict(st.secrets["firebase"])

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------------------------
# 🟢 Sidebar: Toggle OpenAI API Mode
# -----------------------------------
st.sidebar.header("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=True)

# -----------------------------------
# 💬 User Input
# -----------------------------------
st.title("🧠 MoodMate – Your Mental Health Companion")
user_input = st.text_area("📝 How are you feeling today?", placeholder="I'm feeling a bit off...")

if st.button("🔍 Analyze Mood"):
    if user_input.strip():
        mood, emoji = analyze_mood(user_input, use_openai)
        quote = get_motivational_quote(mood)

        st.subheader("🧭 Mood Analysis")
        st.write(f"**Mood:** {mood} {emoji}")
        st.write(f"**Quote:** _{quote}_")

        # 🔥 Save to Firestore
        doc_ref = db.collection("mood_logs").document()
        doc_ref.set({
            "message": user_input,
            "mood": mood,
            "emoji": emoji,
            "quote": quote
        })
    else:
        st.warning("Please enter your message before analyzing.")
