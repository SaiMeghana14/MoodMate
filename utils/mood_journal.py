import streamlit as st
import json
import os
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Optional: for voice input
import speech_recognition as sr
from tempfile import NamedTemporaryFile

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

# Mood-based suggestions and YouTube music
mood_suggestions = {
    "😊": {
        "suggestion": "Keep spreading positivity! How about writing a gratitude list?",
        "music": "https://www.youtube.com/embed/ZbZSe6N_BXs"
    },
    "😢": {
        "suggestion": "It's okay to feel sad. Try deep breathing or talk to someone you trust.",
        "music": "https://www.youtube.com/embed/2Vv-BfVoq4g"
    },
    "😐": {
        "suggestion": "Neutral day? Take a mindful walk or journal to reflect.",
        "music": "https://www.youtube.com/embed/y6120QOlsfU"
    },
    "😴": {
        "suggestion": "Rest is important. Maybe try a guided meditation.",
        "music": "https://www.youtube.com/embed/aEqlQvczMJQ"
    },
    "😠": {
        "suggestion": "Anger is valid. Try breathing deeply and note your triggers.",
        "music": "https://www.youtube.com/embed/2vjPBrBU-TM"
    },
    "😍": {
        "suggestion": "Feeling the love? Send someone a nice message!",
        "music": "https://www.youtube.com/embed/JGwWNGJdvx8"
    },
    "🤯": {
        "suggestion": "Overwhelmed? Write it out. Let it flow.",
        "music": "https://www.youtube.com/embed/MYSVMgRr6pw"
    },
    "😰": {
        "suggestion": "Feeling anxious? Try 4-7-8 breathing or write your worries.",
        "music": "https://www.youtube.com/embed/1ZYbU82GVz4"
    },
    "🤢": {
        "suggestion": "Not feeling well? Rest and hydrate. Come back when you feel better.",
        "music": "https://www.youtube.com/embed/E1ZVSFfCk9g"
    }
}

# Transcribe audio file to text
def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        try:
            return r.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Speech recognition service error."

# Main journaling function
def mood_journal_app(username):
    st.title("🎙️ Mood Journal with Voice Input")
    st.caption("Speak or type your thoughts, track your moods, and get support.")

    user_data = load_user_data(username)
    today = datetime.now().strftime("%Y-%m-%d")

    mood = st.selectbox("How are you feeling today?", list(mood_suggestions.keys()))
    st.markdown(f"💡 {mood_suggestions[mood]['suggestion']}")

    # Voice input section
    st.subheader("🎤 Voice Journal (Optional)")
    audio_file = st.file_uploader("Upload your voice journal (WAV preferred)", type=["wav", "mp3", "ogg"])
    voice_text = ""
    if audio_file:
        with NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            tmp_path = tmp.name
        voice_text = transcribe_audio(tmp_path)
        st.success("✅ Transcription complete:")
        st.write(voice_text)

    # Text journal
    st.subheader("📝 Write or edit your journal entry")
    entry = st.text_area("Your thoughts...", value=voice_text, height=200)

    # Sentiment detection
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

    # Save Entry
    if st.button("💾 Save Today's Entry"):
        user_data["journals"][today] = {
            "mood": mood,
            "text": entry,
            "sentiment": sentiment_label
        }
        save_user_data(username, user_data)
        st.success("✅ Your journal entry has been saved!")

    # Music playback
    st.subheader("🎵 MoodMate Music")
    st.components.v1.html(
        f'<iframe width="100%" height="315" src="{mood_suggestions[mood]["music"]}" frameborder="0" allowfullscreen></iframe>',
        height=340
    )

    # Show past entries
    st.markdown("---")
    st.subheader("📅 Journal History")
    if user_data.get("journals"):
        for date, entry in sorted(user_data["journals"].items(), reverse=True):
            st.markdown(f"**{date}** — Mood: {entry['mood']}")
            st.markdown(f"> {entry['text']}")
            if entry.get("sentiment"):
                st.markdown(f"_Sentiment: {entry['sentiment']}_")
            st.markdown("---")
    else:
        st.info("No entries yet. Start writing today!")
