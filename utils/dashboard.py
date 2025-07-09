import streamlit as st
import pandas as pd
from .journal import get_entries
import matplotlib.pyplot as plt

def plot_mood_trends():
    entries = get_entries()
    if not entries:
        st.info("No journal entries yet.")
        return

    df = pd.DataFrame(entries)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    st.line_chart(df.groupby(df['timestamp'].dt.date)['mood'].apply(lambda x: x.mode()[0] if not x.empty else None).value_counts())
