import streamlit as st
from utils.auth import load_users, save_users
import datetime

def achievements_page(user):
    st.subheader("🏅 Your Achievements")
    if "user" not in st.session_state:
        st.warning("Please login to see your streaks.")
        return

    users = load_users()
    user = st.session_state.user
    if user not in users:
        st.warning(f"No data found for user **{user}**.")
        return
    journals = users[user].get("journals", {})

    today = datetime.date.today()
    streak = 0
    for i in range(10):
        day = str(today - datetime.timedelta(days=i))
        if day in journals:
            streak += 1
        else:
            break

    users[user]["streak"] = streak
    save_users(users)

    st.metric("🔥 Current Streak", f"{streak} days")

    badges = []
    if streak >= 3:
        badges.append("⭐ 3-Day Journaler")
    if streak >= 5:
        badges.append("🌟 5-Day Mood Master")
    if streak >= 7:
        badges.append("🏆 7-Day Wellness Champion")

    for b in badges:
        st.success(b)

    if streak >= 3:
        st.balloons()
