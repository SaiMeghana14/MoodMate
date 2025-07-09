import streamlit as st
import json

def activities_page():
    st.subheader("🎧 Relaxation & Motivation")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st_lottie("assets/meditation.json", height=200)
        st.write("Meditation")

    with col2:
        st_lottie("assets/achievements.json", height=200)
        st.write("Your Achievements")

    with col3:
        st_lottie("assets/chatbot.json", height=200)
        st.write("Mindful Chatbot")

def st_lottie(filepath, height=300):
    with open(filepath, "r") as f:
        data = json.load(f)
        st.components.v1.html(f\"\"\"\n        <script src=\"https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js\"></script>\n        <lottie-player src='data:application/json;base64,{data}' background=\"transparent\" speed=\"1\" style=\"height: {height}px;\" loop autoplay></lottie-player>\n        \"\"\", height=height)
