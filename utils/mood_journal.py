import streamlit as st
import json
import os
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Load user data from JSON
def load_user_data(username):
    if not os.path.exists("users.json"):
        return {"journals": {}, "streak": 0}
    with open("users.json", "r") as f:
        data = json.load(f)
    return data.get(username, {"journals": {}, "streak": 0})

# Save user data to JSON
def save_user_data(username, user_data):
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            all_data = json.load(f)
    else:
        all_data = {}

    all_data[username] = user_data
    with open("users.json", "w") as f:
        json.dump(all_data, f, indent=4)

# Main journaling function
def mood_journal_app(username):
    st.title("📓 Mood Journal")
    st.caption("Track your feelings, one day at a time.")

    user_data = load_user_data(username)
    today = datetime.now().strftime("%Y-%m-%d")

    # Input section
    mood = st.selectbox("How are you feeling today?", ["😊", "😐", "😢", "😠", "😴", "😍", "🤯", "😰", "🤢"])
    entry = st.text_area("Write your journal entry here...", height=200)

    sentiment = None
    sentiment_label = None

    if entry:
        sentiment = sid.polarity_scores(entry)
        compound = sentiment["compound"]
        if compound >= 0.05:
            sentiment_label = "Positive"
        elif compound <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        st.markdown(f"🧠 Sentiment: **{sentiment_label}** (*{compound:.2f}*)")

    if st.button("💾 Save Today's Entry"):
        user_data["journals"][today] = {
            "mood": mood,
            "text": entry,
            "sentiment": sentiment_label
        }
        save_user_data(username, user_data)
        st.success("✅ Journal entry saved!")

    # Display previous entries
    st.markdown("---")
    st.subheader("📅 Previous Entries")
    journals = user_data.get("journals", {})
    if journals:
        for date, content in sorted(journals.items(), reverse=True):
            st.markdown(f"**📌 {date} — Mood:** {content.get('mood', '')}")
            st.markdown(f"> {content.get('text', '')}")
            if content.get("sentiment"):
                st.markdown(f"_Sentiment: {content['sentiment']}_")
            st.markdown("---")
    else:
        st.info("No journal entries found. Write your first one today!")
