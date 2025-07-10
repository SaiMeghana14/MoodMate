import streamlit as st
import datetime
import pandas as pd
import plotly.express as px

def gamification_page():
    st.subheader("🏆 Gamification – Your Positivity Journey")

    today = datetime.date.today()
    streak = st.session_state.get("streak", 0)
    last_checkin = st.session_state.get("last_checkin")
    checkin_dates = st.session_state.get("checkin_dates", [])

    # Record today's check-in if not already
    if last_checkin != today:
        streak += 1
        st.session_state["streak"] = streak
        st.session_state["last_checkin"] = today
        checkin_dates.append(str(today))
        st.session_state["checkin_dates"] = sorted(set(checkin_dates))
        st.balloons()

    # Display current streak
    st.metric("🔥 Current Streak", f"{st.session_state['streak']} days")

    # Dynamic badge unlocking
    badges = []
    if streak >= 1: badges.append("🌱 First Step")
    if streak >= 3: badges.append("🌟 3‑Day Consistency")
    if streak >= 7: badges.append("🧘 Zen Seeker")
    if streak >= 14: badges.append("🦸 Mindfulness Hero")
    if streak >= 30: badges.append("🏅 1‑Month Master")

    st.markdown("### 🎖️ Badges Earned")
    for badge in badges:
        st.markdown(f"- {badge}")

    # Display calendar heatmap
    st.markdown("### 📅 Check‑In Calendar Heatmap")
    if checkin_dates:
        df = pd.DataFrame({"date": pd.to_datetime(checkin_dates)})
        df["count"] = 1
        heat = df.groupby("date").sum().reset_index()
        heat["dow"] = heat["date"].dt.weekday  # Monday=0
        heat["week"] = heat["date"].dt.isocalendar().week

        fig = px.density_heatmap(
            heat, x="week", y="dow", z="count",
            labels={"week": "Week", "dow": "Day of Week", "count": "Check‑ins"},
            nbinsx=heat["week"].nunique(),
            nbinsy=7,
            color_continuous_scale="Blues",
            height=300,
        )
        fig.update_yaxes(
            tickvals=[0,1,2,3,4,5,6],
            ticktext=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            autorange="reversed"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No check‑ins yet — start journaling today!")

