import streamlit as st
import datetime
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
from utils.graph import plot_mood_trend
from utils.music import play_motivational_music
from utils.voice_input import record_and_transcribe
from utils.auth import authenticate_user
import firebase_admin
from firebase_admin import credentials, firestore

# Page settings
st.set_page_config(page_title="🧠 MoodMate", page_icon="🧠")

# --------------------------------------
# 🔐 Firebase Initialization
# --------------------------------------
firebase_config = dict(st.secrets["firebase"])
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# --------------------------------------
# 👤 User Authentication
# --------------------------------------
user = authenticate_user()
if not user:
    st.warning("Please login to continue.")
    st.stop()

# --------------------------------------
# 🌐 Online/Offline Mode Toggle
# --------------------------------------
st.sidebar.header("⚙️ Settings")
use_openai = st.sidebar.toggle("Use OpenAI API (Online Mode)", value=False)

# --------------------------------------
# 🧠 Mood Input Section
# --------------------------------------
st.title("🧠 MoodMate – Your Mood Companion")
st.markdown("### 📝 How are you feeling today?")

user_input = st.text_area("Write something...", placeholder="I'm feeling neutral.")

# 🎙️ Voice Input (Optional)
if st.button("🎤 Use Voice Input"):
    user_input = record_and_transcribe()
    st.success("Captured voice input!")

if st.button("🔍 Analyze Mood") and user_input:
    mood, emoji = analyze_mood(user_input, use_openai)

    st.markdown(f"### Your mood is **{mood}** {emoji}")
    st.session_state["mood"] = mood

    quote = get_motivational_quote(mood)
    st.info(f"💬 {quote}")

    play_motivational_music(mood)

    # Save mood entry
    db.collection("moods").add({
        "user": user,
        "text": user_input,
        "mood": mood,
        "emoji": emoji,
        "timestamp": datetime.datetime.now()
    })

# Ensure user is set
user = st.session_state.get("user", "guest")

# Ensure Firebase DB is ready
from firebase_admin import firestore
db = firestore.client()

# --------------------------------------
# 📈 Mood History Graph

st.subheader("📊 Mood Trend")

# Ensure 'user' is defined
user = st.session_state.get("user", "guest")

try:
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
        df = pd.DataFrame(history_data)
        df = df.sort_values("timestamp")

        # Convert timestamp to datetime if not already
        if not pd.api.types.is_datetime64_any_dtype(df["timestamp"]):
            df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Map mood strings to values
        mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
        df["mood_value"] = df["mood"].map(mood_map)

        st.line_chart(data=df, x="timestamp", y="mood_value", use_container_width=True)
    else:
        st.info("No mood history found for this user.")

except Exception as e:
    st.error(f"⚠️ Error loading mood trend: {e}")



# -------------------------------
# 📓 Daily Journal
# -------------------------------
st.subheader("📓 Daily Journal")
journal_text = st.text_area("Write your thoughts for the day")
if st.button("Save Journal Entry"):
    db.collection("journals").add({"text": journal_text, "user": user, "timestamp": datetime.datetime.now()})
    st.success("📝 Journal entry saved!")
