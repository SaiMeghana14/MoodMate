import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def mood_journal_page():
    st.subheader("📝 Mood Journal")
    analyzer = SentimentIntensityAnalyzer()

    entry = st.text_area("How are you feeling today?")
    if st.button("Analyze"):
        if entry:
            score = analyzer.polarity_scores(entry)
            mood = "😊 Positive" if score['compound'] > 0.5 else "😐 Neutral" if score['compound'] >= -0.5 else "😞 Negative"
            st.success(f"Detected Mood: {mood}")
        else:
            st.warning("Please write something first.")
