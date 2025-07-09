# ✅ utils/dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from .journal import get_entries
from collections import Counter
import datetime

def plot_mood_trends():
    entries = get_entries()
    if not entries:
        st.info("No entries to show.")
        return
    df = pd.DataFrame(entries)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    df['date'] = df['timestamp'].dt.date
    mood_counts = df.groupby('date')['mood'].agg(lambda x: x.mode()[0] if not x.empty else 'Neutral')
    st.line_chart(mood_counts.value_counts().sort_index())

def mood_heatmap():
    entries = get_entries()
    if not entries:
        return
    df = pd.DataFrame(entries)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['weekday'] = df['timestamp'].dt.day_name()
    df['hour'] = df['timestamp'].dt.hour
    heatmap_data = pd.crosstab(df['hour'], df['weekday'])
    st.write("### 🗓️ Mood Entry Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

def show_wordcloud():
    entries = get_entries()
    if not entries:
        return
    text = " ".join([entry['entry'] for entry in entries])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.write("### ☁️ Common Words in Your Journals")
    st.image(wordcloud.to_array())
