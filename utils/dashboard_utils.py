import plotly.express as px
import streamlit as st
import pandas as pd

def plot_mood_line_chart(journals):
    if not journals:
        st.info("No data available for mood chart.")
        return
    data = []
    for date, entry in journals.items():
        data.append({"date": date, "mood": entry["mood"]})
    df = pd.DataFrame(data)
    fig = px.line(df, x="date", y="mood", title="Mood Over Time", markers=True)
    st.plotly_chart(fig)

def plot_sentiment_bar_chart(journals):
    sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for entry in journals.values():
        sentiment = entry.get("sentiment")
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1
    df = pd.DataFrame(list(sentiment_counts.items()), columns=["Sentiment", "Count"])
    fig = px.bar(df, x="Sentiment", y="Count", title="Sentiment Distribution")
    st.plotly_chart(fig)
