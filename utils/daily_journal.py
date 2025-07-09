import streamlit as st
import datetime
from utils.auth import load_users, save_users

def daily_journal_page():
    st.subheader("📝 Daily Journal Entry")
    if "user" not in st.session_state:
        st.warning("Please login to continue.")
        return

    today = str(datetime.date.today())
    mood = st.radio("Today's Mood:", ["😊", "😢", "😡", "😴", "😨", "😇"], horizontal=True)
    entry = st.text_area("How are you feeling today?")
    if st.button("Save Entry"):
        users = load_users()
        user = st.session_state.user
        if user in users:
            users[user]["journals"][today] = {"mood": mood, "text": entry}
            save_users(users)
            st.success("Journal saved!")
