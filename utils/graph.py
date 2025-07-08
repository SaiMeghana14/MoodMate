import pandas as pd
import altair as alt
import streamlit as st

def plot_mood_trend(data):
    """
    Expects data as a list of dictionaries with keys: 'timestamp', 'mood'
    """
    if not data:
        st.warning("No mood history to show.")
        return

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    mood_colors = {
        'Positive': 'green',
        'Negative': 'red',
        'Neutral': 'gray'
    }

    chart = alt.Chart(df).mark_line(point=True).encode(
        x='timestamp:T',
        y=alt.Y('mood:N', sort=['Negative', 'Neutral', 'Positive']),
        color=alt.Color('mood:N', scale=alt.Scale(domain=list(mood_colors.keys()), range=list(mood_colors.values()))),
        tooltip=['timestamp:T', 'mood:N']
    ).properties(
        width=700,
        height=400,
        title='Mood Trend Over Time'
    )

    st.altair_chart(chart, use_container_width=True)
