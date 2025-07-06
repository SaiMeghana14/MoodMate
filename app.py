import streamlit as st
import pandas as pd
from utils.analyzer import analyze_mood
from utils.quotes import get_motivational_quote

st.set_page_config(page_title="MoodMate", page_icon="🧠")

st.title("🧠 MoodMate – Your Mood Companion")

# Sidebar toggle for local sentiment engine
st.sidebar.header("⚙️ Settings")
st.sidebar.toggle("Use TextBlob (Simple)", value=False, key="use_textblob")

st.write("📝 How are you feeling today?")
user_input = st.text_area("Enter your thoughts here", placeholder="I'm feeling happy today!")

if st.button("🔍 Analyze Mood") and user_input.strip() != "":
    mood, emoji = analyze_mood(user_input)
    st.success(f"Your mood is **{mood}** {emoji}")

    quote = get_motivational_quote(mood)
    st.info(f"💬 Motivation: *{quote}*")
