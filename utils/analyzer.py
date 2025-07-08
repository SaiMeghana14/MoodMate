import streamlit as st

USE_HUGGINGFACE = st.secrets.get("use_huggingface", False)

if USE_HUGGINGFACE:
    from transformers import pipeline
    classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")
else:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()

def analyze_mood(user_input):
    if USE_HUGGINGFACE:
        result = classifier(user_input)[0]
        label = result['label'].capitalize()
        if label in ["Joy", "Love"]:
            mood = "Positive"
            emoji = "😊"
        elif label in ["Anger", "Sadness", "Fear"]:
            mood = "Negative"
            emoji = "😢"
        else:
            mood = "Neutral"
            emoji = "😐"
    else:
        scores = analyzer.polarity_scores(user_input)
        compound = scores["compound"]
        if compound >= 0.05:
            mood = "Positive"
            emoji = "🙂"
        elif compound <= -0.05:
            mood = "Negative"
            emoji = "☹️"
        else:
            mood = "Neutral"
            emoji = "😐"
    return mood, emoji
