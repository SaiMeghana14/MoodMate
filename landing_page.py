import streamlit as st
from utils.lottie_loader import render_lottie

def show_landing_page_with_animations():
    # 🌈 Hero Section
    st.markdown("## 🌈 Welcome to MoodMate")
    st.markdown("Your smart companion for emotional wellness")

    st.markdown("---")

    # ✨ Features
    st.markdown("### ✨ Core Features")
    render_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json", height=180, is_url=True)
    st.markdown("""
    - Mood Detection via Journal and Voice  
    - Empathetic AI Chatbot  
    - Visual Mood Tracker Dashboard  
    - Guided Meditations & Breathing  
    - Gamified Progress Tracking
    """)

    st.markdown("---")

    # 💬 Testimonials
    st.markdown("### 💬 What Users Say")
    render_lottie("assets/achievements.json", height=180)
    st.markdown("""
    > *"MoodMate has changed how I check in with myself each day. I feel heard and supported."* – Ananya  
    > *"The breathing and affirmations really help me stay grounded during exams."* – Rahul
    """)

    st.markdown("---")

    # 👤 Developer Spotlight
    st.markdown("### 👤 Developer Spotlight")
    st.markdown("""
    - **K.N.V. Sai Meghana** – Developer, Designer & Creator of MoodMate  
    Passionate about emotional well-being, I built MoodMate as a smart mental health companion blending AI, journaling, and self-care features.
    """)

    st.markdown("---")

    # ❓ FAQs
    st.markdown("### ❓ Frequently Asked Questions")
    st.markdown("""
    **Is my data private?** Yes, MoodMate supports end-to-end encryption.  
    **Do I need internet for this?** Only for syncing and AI features.  
    **Can I use this offline?** Yes, basic journaling and breathing tools work offline.
    """)

    st.markdown("---")

    # 💡 Real Impact
    st.markdown("### 💡 Real Impact")
    st.markdown("""
    *"Before MoodMate, I used to bottle everything inside. Now I reflect and heal every day."* – Priya, Student  
    *"Our college mental health club recommends MoodMate to help students cope better."* – Mentor
    """)

    st.markdown("---")

    # 🚀 CTA
    st.markdown("### 🚀 Ready to Start?")
    render_lottie("assets/meditation.json", height=150)
    st.markdown("Click any section from the sidebar to begin 💖")

# Scroll to Top Button
st.markdown("""
    <style>
    #scrollTopBtn {
        position: fixed;
        bottom: 40px;
        right: 30px;
        z-index: 99;
        border: none;
        outline: none;
        background-color: #ff6ec4;
        color: white;
        cursor: pointer;
        padding: 10px 16px;
        border-radius: 30px;
        font-size: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    #scrollTopBtn:hover {
        background-color: #e94eaa;
    }
    </style>

    <button onclick="topFunction()" id="scrollTopBtn" title="Go to top">↑ Top</button>

    <script>
    function topFunction() {
        document.documentElement.scrollTop = 0;
    }
    </script>
""", unsafe_allow_html=True)
