# Convert voice input to text using SpeechRecognition
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import streamlit as st

def record_and_transcribe():
    r = sr.Recognizer()
    st.info("🎙️ Listening... Please speak now.")
    
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        st.success("✅ Voice captured!")

    try:
        text = r.recognize_google(audio)
        st.info(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.warning("❌ Couldn't understand the audio.")
    except sr.RequestError:
        st.error("⚠️ API unavailable.")
    return ""
