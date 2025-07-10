# utils/emergency.py

import streamlit as st

def emergency_page():
    st.title("🚨 Emergency Support")

    st.markdown("""
    If you're feeling overwhelmed or in crisis, please reach out immediately.

    ### 📞 Helplines:
    - **iCall (India)** – 9152987821
    - **Vandrevala Foundation** – 1860 266 2345
    - **AASRA** – 91-22-27546669
    - **NIMHANS** – 080-46110007

    ### 🧠 Coping Tools:
    - Deep breathing: Inhale for 4s, hold for 7s, exhale for 8s
    - Try a 5-minute guided meditation
    - Talk to someone you trust
    """)

    st.button("🧘 Launch Guided Breathing")
