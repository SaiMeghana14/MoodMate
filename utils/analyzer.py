# ✅ analyzer.py (VADER-based offline mood detection)

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Toggle: select TextBlob or VADER
use_textblob = st.sidebar.toggle("Use TextBlob (Simple)", value=False)

if use_textblob:
    from textblob import TextBlob

def analyze_mood(user_input):
    try:
        if use_textblob:
            analysis = TextBlob(user_input)
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                return "Positive", "😊"
            elif polarity < 0:
                return "Negative", "😔"
            else:
                return "Neutral", "😐"
        else:
            score = analyzer.polarity_scores(user_input)
            compound = score["compound"]
            if compound >= 0.3:
                return "Positive", "😊"
            elif compound <= -0.3:
                return "Negative", "😔"
            else:
                return "Neutral", "😐"
    except Exception as e:
        st.error(f"⚠️ Mood analysis failed: {e}")
        return "Neutral", "😐"
