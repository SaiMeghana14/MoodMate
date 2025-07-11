import streamlit as st
import webbrowser
import json
from utils.lottie_loader import render_lottie

def activities_page():
    st.subheader("🎧 AI-Based Suggestions & Relaxation")

    mood = st.selectbox("How are you feeling?", ["Happy", "Sad", "Stressed", "Energetic", "Calm"])
    
    if mood == "Stressed":
        st.video("https://www.youtube.com/watch?v=ZToicYcHIOU")  # Breathing exercise
    elif mood == "Happy":
        st.video("https://www.youtube.com/watch?v=3GwjfUFyY6M")  # Celebration music
    elif mood == "Sad":
        st.video("https://www.youtube.com/watch?v=ho9rZjlsyYY")  # Peaceful piano
    elif mood == "Calm":
        st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")  # Guided meditation
    elif mood == "Energetic":
        st.video("https://www.youtube.com/watch?v=BoEKWtgJQAU")  # Workout beats

    if st.button("🎵 Open Spotify Wellness Playlist"):
        webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0")

    st.markdown("## 🧘 Breathing Animation")
    render_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json", height=300, is_url=True)

def st_lottie(filepath, height=300):
    with open(filepath, "r") as f:
        data = json.load(f)
        st.components.v1.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src='data:application/json;base64,{json.dumps(data)}' background='transparent' speed='1' style='width:100%; height:{height}px;' loop autoplay></lottie-player>
        """, height=height)
