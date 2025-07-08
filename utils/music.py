# Play motivational music based on mood
import streamlit as st

def play_motivational_music(mood):
    tracks = {
        "Positive": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Neutral": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Negative": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    }
    audio_url = tracks.get(mood)
    if audio_url:
        st.audio(audio_url)
