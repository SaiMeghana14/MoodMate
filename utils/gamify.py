# ✅ utils/gamify.py
import streamlit as st
from datetime import date

if "streak" not in st.session_state:
    st.session_state.streak = 0
    st.session_state.last_entry_date = None

def update_streaks(mood):
    today = date.today()
    if st.session_state.last_entry_date != today:
        st.session_state.streak += 1
        st.session_state.last_entry_date = today

def show_achievements():
    streak = st.session_state.get("streak", 0)
    st.metric("🔥 Mood Streak", f"{streak} Days")
    if streak >= 3:
        st.success("🏅 3-Day Mood Journal Streak!")
    if streak >= 7:
        st.balloons()
        st.success("🌟 7-Day Emotional Growth Champion!")
