import streamlit as st
from transformers import pipeline

def mental_health_chatbot_page():
    st.subheader("💬 Talk to MoodMate")
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    
    user_input = st.text_input("You:")
    if user_input:
        response = chatbot(user_input, max_length=100)[0]['generated_text']
        st.text_area("MoodMate:", value=response.split(user_input)[-1], height=150)

