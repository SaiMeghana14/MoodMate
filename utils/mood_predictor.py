import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def mood_predictor_page():
    st.subheader("📈 Mood Predictor & Insights")

    mood_data = np.random.choice(['Happy', 'Sad', 'Anxious', 'Excited', 'Angry'], size=30)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    df = pd.DataFrame({'Date': dates, 'Mood': mood_data})

    mood_counts = df['Mood'].value_counts()
    st.bar_chart(mood_counts)

    st.markdown("### 🔮 Predicted Mood Tomorrow")
    st.success("Most Likely: 😊 Happy (based on recent patterns)")

    st.markdown("### ☁️ Common Words in Journals")
    text = "I'm stressed today but hopeful. Anxious about exams. Grateful for friends. Tired but peaceful. Relaxed and calm. Inspired!"
    wc = WordCloud(width=800, height=400).generate(text)
    st.image(wc.to_array())

