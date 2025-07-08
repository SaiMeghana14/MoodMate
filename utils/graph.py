import streamlit as st
import pandas as pd
import altair as alt

def plot_mood_trend(user, db):
    docs = db.collection(\"mood_entries\").where(\"user\", \"==\", user).stream()
    data = [{
        \"timestamp\": doc.to_dict()[\"timestamp\"],
        \"mood\": doc.to_dict()[\"mood\"]
    } for doc in docs]

    if not data:
        st.warning(\"No mood history found.\")
        return

    df = pd.DataFrame(data)
    df[\"timestamp\"] = pd.to_datetime(df[\"timestamp\"])

    chart = alt.Chart(df).mark_line(point=True).encode(
        x='timestamp:T',
        y=alt.Y('mood:N', sort=['Negative', 'Neutral', 'Positive']),
        tooltip=['timestamp:T', 'mood:N']
    ).properties(title=\"Mood Over Time\", width=600)

    st.altair_chart(chart, use_container_width=True)
