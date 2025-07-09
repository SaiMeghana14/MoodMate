# ✅ utils/activities.py
import streamlit as st
import random
from streamlit_lottie import st_lottie
import json

def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def gratitude_spinner():
    prompts = [
        "Something good that happened today",
        "A friend you're thankful for",
        "A personal strength you appreciate",
        "A happy memory from childhood",
        "A simple joy from today (e.g., coffee, music)"
    ]
    st_lottie(load_lottie("assets/gratitude.json"), height=200, key="grateful")
    if st.button("🎯 Spin for Gratitude Prompt"):
        st.success(random.choice(prompts))

def journal_prompt():
    questions = [
        "What emotion did you feel strongest today?",
        "Describe a moment that brought you peace.",
        "What challenged you emotionally today?",
        "Who made you smile recently, and why?",
        "How do you usually cope with stress?"
    ]
    if st.button("🌀 Random Journal Prompt"):
        st.info(random.choice(questions))

def uplifting_quote():
    quotes = [
        "You are stronger than you think.",
        "This too shall pass.",
        "One day at a time.",
        "You are enough just as you are.",
        "Even the darkest night will end and the sun will rise."
    ]
    if st.button("💫 Get a Uplifting Quote"):
        st.success(random.choice(quotes))
