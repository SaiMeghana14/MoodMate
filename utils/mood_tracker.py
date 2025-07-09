import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.auth import load_users

def mood_tracker_page():
    st.subheader("📊 Mood Tracker")
    if "user" not in st.session_state:
        st.warning("Login required to view your mood data.")
        return

    users = load_users()
    user_data = users.get(st.session_state.user, {})
    journals = user_data.get("journals", {})

    if not journals:
        st.info("No data yet. Start journaling!")
        return

    df = pd.DataFrame([
        {"date": date, "mood": entry["mood"]}
        for date, entry in journals.items()
    ])
    df["date"] = pd.to_datetime(df["date"])
    mood_map = {"😊": 5, "😇": 4, "😴": 3, "😢": 2, "😨": 1, "😡": 0}
    df["mood_score"] = df["mood"].map(mood_map)

    st.line_chart(df.set_index("date")["mood_score"])

    st.markdown("### 📅 Mood Calendar (Heatmap)")
    st.dataframe(df.pivot_table(values="mood_score", index=df["date"].dt.month, columns=df["date"].dt.day, fill_value=0))
