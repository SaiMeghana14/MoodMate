import streamlit as st
import speech_recognition as sr

def voice_journal_page():
    st.subheader("🎤 Voice Journal")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"Transcribed Text: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio")
