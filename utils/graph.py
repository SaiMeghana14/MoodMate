import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from io import StringIO
import matplotlib.dates as mdates

# Mood to emoji mapping
MOOD_EMOJI = {
    "Positive": "😊",
    "Neutral": "😐",
    "Negative": "😞"
}

def plot_mood_trend(user_uid, db):
    try:
        docs = db.collection("moods")\
                 .where("user", "==", user_uid)\
                 .order_by("timestamp")\
                 .stream()

        mood_data = []
        for doc in docs:
            data = doc.to_dict()
            if "mood" in data and "timestamp" in data:
                timestamp = data["timestamp"]
                if isinstance(timestamp, datetime):
                    mood_data.append({
                        "timestamp": timestamp,
                        "mood": data["mood"],
                        "emoji": data.get("emoji", MOOD_EMOJI.get(data["mood"], ""))
                    })

        if not mood_data:
            st.info("ℹ️ No mood history found. Submit a mood first!")
            return

        df = pd.DataFrame(mood_data)
        df["date"] = df["timestamp"].dt.date

        # 📌 Mood Filter
        mood_options = ["All", "Positive", "Neutral", "Negative"]
        selected_mood = st.selectbox("📌 Filter by Mood", mood_options)

        if selected_mood != "All":
            df = df[df["mood"] == selected_mood]

        # 📈 Mood count per day
        mood_count_per_day = df.groupby(["date", "mood"]).size().unstack(fill_value=0)

        # 📊 Plot
        st.markdown("### 📊 Mood Trend with Emojis")
        fig, ax = plt.subplots(figsize=(9, 5))
        bars = mood_count_per_day.plot(kind="bar", ax=ax,
                                       color={"Positive": "green", "Neutral": "gray", "Negative": "red"})
        ax.set_ylabel("Count")
        ax.set_xlabel("Date")
        ax.set_title("Mood Frequency by Date")
        ax.legend(title="Mood")

        # 🟢 Add emoji labels
        for container in ax.containers:
            for bar in container:
                height = bar.get_height()
                if height > 0:
                    label = container.get_label()
                    emoji = MOOD_EMOJI.get(label, "")
                    ax.annotate(emoji,
                                (bar.get_x() + bar.get_width() / 2, height),
                                ha='center', va='bottom', fontsize=14)

        st.pyplot(fig)

        # 📤 CSV Export
        st.markdown("### 🗂️ Export Mood History")
        csv = df[["timestamp", "mood", "emoji"]].to_csv(index=False)
        st.download_button("📥 Download Mood CSV", csv, "mood_history.csv", "text/csv")

    except Exception as e:
        st.error(f"📉 Error loading mood trend: {e}")
