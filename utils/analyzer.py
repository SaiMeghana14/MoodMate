import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure VADER lexicon is downloaded
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

# Initialize VADER
vader = SentimentIntensityAnalyzer()

# Hugging Face transformer
from transformers import pipeline

@st.cache_resource
def get_hf_pipeline():
    return pipeline("sentiment-analysis")

try:
    hf_analyzer = get_hf_pipeline()
except Exception as e:
    hf_analyzer = None
    st.warning("⚠️ Hugging Face model not available. Using offline mode only.")

def analyze_mood(user_input, mode="Offline"):
    if mode == "Offline":
        scores = vader.polarity_scores(user_input)
        compound = scores["compound"]
        if compound >= 0.05:
            return "Positive", "😊"
        elif compound <= -0.05:
            return "Negative", "😔"
        else:
            return "Neutral", "😐"

    elif mode == "Online" and hf_analyzer is not None:
        try:
            result = hf_analyzer(user_input)[0]
            label = result["label"]
            if label == "POSITIVE":
                return "Positive", "😊"
            elif label == "NEGATIVE":
                return "Negative", "😔"
            else:
                return "Neutral", "😐"
        except Exception as e:
            st.error(f"⚠️ Error using Hugging Face: {e}")
            return "Neutral", "😐"
    else:
        return "Neutral", "😐"
