import streamlit as st
import json

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def show_landing_page_with_animations():
    st.markdown("""
        <style>
            .section {padding: 4rem 2rem; border-radius: 20px; margin-bottom: 3rem;}
            .hero {background: linear-gradient(to right, #ffdde1, #ee9ca7); text-align: center;}
            .features {background: linear-gradient(to right, #c9ffbf, #ffafbd);}
            .testimonials {background: linear-gradient(to right, #fbc2eb, #a6c1ee);}
            .cta {background: linear-gradient(to right, #fdfbfb, #ebedee); text-align: center;}
            h1, h2, h3 {font-family: 'Segoe UI', sans-serif;}
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section hero">', unsafe_allow_html=True)
        st.image("assets/logo.png", width=150)
        st.markdown("## 🌈 Welcome to MoodMate")
        st.markdown("#### Your smart companion for emotional wellness")
        st_lottie("assets/meditation.json", 250)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section features">', unsafe_allow_html=True)
        st.markdown("## ✨ Core Features")
        st_lottie("assets/chatbot.json", 200)
        st.markdown("""
        - Mood Detection via Journal and Voice  
        - Empathetic AI Chatbot  
        - Mood Tracker Dashboard  
        - Meditation & Breathing  
        - Gamified Check-ins  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section testimonials">', unsafe_allow_html=True)
        st.markdown("## 💬 What Users Say")
        st.markdown("> *\"MoodMate helped me track my emotional ups and downs so easily.\"* – Ananya")
        st_lottie("assets/achievements.json", 200)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section cta">', unsafe_allow_html=True)
        st.markdown("## 🚀 Ready to start your journey?")
        st.markdown("Click a tab on the sidebar to begin 💖")
        st.markdown("</div>", unsafe_allow_html=True)

def st_lottie(path, height=300):
    import streamlit.components.v1 as components
    with open(path, "r") as f:
        animation_data = json.dumps(json.load(f))
    components.html(f'''
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src='data:application/json;base64,{base64.b64encode(animation_data.encode()).decode()}' background='transparent' speed='1' style='width:100%; height:{height}px;' loop autoplay></lottie-player>
    ''', height=height)
