# ✅ utils/meditation.py
import streamlit as st
import time

def breathing_exercise():
    st.write("### 🫁 Deep Breathing Exercise")
    with st.empty():
        for i in range(3):
            st.markdown("<div style='font-size:32px;'>Inhale... 🫧</div>", unsafe_allow_html=True)
            time.sleep(4)
            st.markdown("<div style='font-size:32px;'>Hold... ✨</div>", unsafe_allow_html=True)
            time.sleep(2)
            st.markdown("<div style='font-size:32px;'>Exhale... 🌬️</div>", unsafe_allow_html=True)
            time.sleep(4)
    st.success("Well done! ✨")

def play_meditation():
    st.write("### 🎧 Play a Short Meditation Audio")
    st.audio("assets/meditation.mp3")
