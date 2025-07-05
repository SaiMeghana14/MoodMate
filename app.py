import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote
import pandas as pd
import json

# Set Streamlit page config
st.set_page_config(page_title="MoodMate", page_icon="🧠")

# ---------------------------------------
# 🔐 Firebase Initialization from secrets
# ---------------------------------------
import streamlit as st
import firebase_admin
from firebase_admin import credentials

# ✅ Convert to native Python dict
firebase_config = dict(st.secrets["firebase"])

# ✅ Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

# ✅ Optional test message (you can remove later)
st.success("✅ Firebase initialized successfully.")

# -----------------------
# 🎯 Main App UI
# -----------------------
st.title("🧠 MoodMate – Your AI Mental Health Buddy")
st.markdown("Welcome! Let’s understand how you're feeling today.")

user_input = st.text_area("📝 How are you feeling right now?", height=150)

if st.button("🔍 Analyze Mood"):
    if user_input.strip():
        mood, emoji = analyze_mood(user_input)
        st.success(f"Your mood is: **{mood}** {emoji}")

        # Show motivational quote
        st.subheader("🌟 Here's something for you:")
        st.info(get_motivational_quote(mood))

        # Save to Firestore
        try:
            doc_ref = db.collection("mood_entries").document()
            doc_ref.set({
                "text": user_input,
                "mood": mood,
                "timestamp": firestore.SERVER_TIMESTAMP
            })
            st.success("✅ Your response has been securely saved.")
        except Exception as e:
            st.error(f"⚠️ Failed to save: {e}")
    else:
        st.warning("Please enter how you're feeling.")

# -----------------------
# 📊 Mood History Viewer
# -----------------------
st.markdown("---")
st.subheader("📚 Mood History")

try:
    mood_entries = db.collection("mood_entries").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    entries = []

    for doc in mood_entries:
        data = doc.to_dict()
        entries.append({
            "Text": data.get("text", ""),
            "Mood": data.get("mood", ""),
            "Timestamp": data.get("timestamp")
        })

    if entries:
        df = pd.DataFrame(entries)
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

        st.dataframe(df, use_container_width=True)

        # Mood chart
        mood_counts = df["Mood"].value_counts()
        st.bar_chart(mood_counts)

        # Export as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Mood Logs (CSV)", csv, "mood_logs.csv", "text/csv")

    else:
        st.info("No entries found yet.")

except Exception as e:
    st.error(f"⚠️ Failed to fetch data: {e}")
