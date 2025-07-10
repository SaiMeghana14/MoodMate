import streamlit as st

def chatbot_page():
    st.header("🧠 MoodMate Chatbot")
    st.write("This will be your mental health chatbot interface.")
    # Optional: Add a simple text-based chatbot
    user_input = st.text_input("You:")
    if user_input:
        st.write(f"🤖 MoodMate: I'm here for you. You said: '{user_input}'")
