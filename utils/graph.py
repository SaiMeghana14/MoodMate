# Graph plotting utilities for mood trend
import streamlit as st
import pandas as pd
import altair as alt

def plot_mood_trend(data):
    if not data:
        st.info("No mood data to show.")
        return

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
    df["mood_value"] = df["mood"].map(mood_map)

    st.markdown("### 📈 Mood Over Time")
    chart = alt.Chart(df).mark_line(point=True).encode(
        x="timestamp:T",
        y="mood_value:Q",
        tooltip=["timestamp", "mood"]
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)

    # 📤 Export CSV
    st.download_button("⬇️ Export CSV", df.to_csv(index=False), "mood_history.csv", "text/csv")
