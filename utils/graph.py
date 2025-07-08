import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_mood_trend(history_data):
    if not history_data:
        st.warning("No mood data to plot.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(history_data)

    # Ensure columns exist
    if "timestamp" not in df.columns or "mood" not in df.columns:
        st.error("Invalid data format for plotting.")
        return

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
    df.dropna(subset=["timestamp"], inplace=True)

    # Map mood to score
    mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
    df["mood_score"] = df["mood"].map(mood_map)

    # Sort and plot
    df.sort_values("timestamp", inplace=True)
    fig, ax = plt.subplots()
    ax.plot(df["timestamp"], df["mood_score"], marker='o')
    ax.set_title("Mood Trend Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Mood Score")
    ax.grid(True)

    st.pyplot(fig)
