import streamlit as st

def emergency_alert_button():
    st.error("🚨 Emergency Help")
    if st.button("Send SOS"):
        st.warning("SOS alert sent to emergency contact.")
