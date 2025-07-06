import streamlit as st
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote

# Page settings
st.set_page_config(page_title="🧠 MoodMate", layout="centered")

st.title("🧠 MoodMate – Your Mood Companion")
st.subheader("📝 How are you feeling today?")

# Input from user
user_input = st.text_input("Describe your mood or day:", "")

# Mode selection
mode = st.radio("Select Mode:", ["Offline", "Online"])

if st.button("🔍 Analyze Mood") and user_input.strip():
    mood, emoji = analyze_mood(user_input, mode)
    st.markdown(f"### Your mood is **{mood}** {emoji}")
    
    if mood != "Neutral":
        quote = get_motivational_quote()
        st.success(f"💬 Motivational Quote: _\"{quote}\"_")
