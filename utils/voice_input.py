import streamlit as st
import speech_recognition as sr

def transcribe_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak now.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        st.success("✅ Transcription complete!")
        return text
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio.")
        return ""
    except sr.RequestError:
        st.error("❌ Error with the speech recognition service.")
        return ""
