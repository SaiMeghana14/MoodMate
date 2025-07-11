import streamlit as st
from utils.lottie_loader import render_lottie  # ✅ Correct import

# ✅ Load custom styles.css
def show_landing_page_with_animations():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("""...""", unsafe_allow_html=True)  # Keep your style block as is

    # Hero Section
    with st.container():
        render_lottie("assets/meditation.json", 200)
        st.markdown('<div class="section hero">', unsafe_allow_html=True)
        st.markdown("""
            ## 🌈 Welcome to MoodMate
            #### Your smart companion for emotional wellness
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # Features Section
    with st.container():
        render_lottie("assets/chatbot.json", 200)
        st.markdown('<div class="section features">', unsafe_allow_html=True)
        st.markdown("""
            ## ✨ Core Features
            - Mood Detection via Journal and Voice
            - Empathetic AI Chatbot
            - Visual Mood Tracker Dashboard
            - Guided Meditations & Breathing
            - Gamified Progress Tracking
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # Testimonials Section
    with st.container():
        render_lottie("assets/achievements.json", 200)
        st.markdown('<div class="section testimonials">', unsafe_allow_html=True)
        st.markdown("""
            ## 💬 What Users Say
            > *"MoodMate has changed how I check in with myself each day. I feel heard and supported."* – Ananya

            > *"The breathing and affirmations really help me stay grounded during exams."* – Rahul
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # Solo Developer Section
    with st.container():
        st.markdown('<div class="section team">', unsafe_allow_html=True)
        st.markdown("""
            ## 👤 Developer Spotlight  
            - **K.N.V. Sai Meghana** – Developer, Designer & Creator of MoodMate  
            Passionate about emotional well-being, I built MoodMate as a smart mental health companion blending AI, journaling, and self-care features.  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # FAQ Section
    with st.container():
        st.markdown('<div class="section faq">', unsafe_allow_html=True)
        st.markdown("""
            ## ❓ Frequently Asked Questions
            **Is my data private?** Yes, MoodMate supports end-to-end encryption.

            **Do I need internet for this?** Only for syncing and AI features.

            **Can I use this offline?** Yes, basic journaling and breathing tools work offline.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # Impact Stories
    with st.container():
        st.markdown('<div class="section impact">', unsafe_allow_html=True)
        st.markdown("""
            ## 💡 Real Impact
            "Before MoodMate, I used to bottle everything inside. Now I reflect and heal every day." – Priya, Student

            "Our college mental health club recommends MoodMate to help students cope better." – Mentor
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # CTA Section
    with st.container():
        render_lottie("assets/meditation.json", 150)
        st.markdown('<div class="section cta">', unsafe_allow_html=True)
        st.markdown("""
            ## 🚀 Ready to start your mood journey?
            Click any section from the sidebar to begin 💖
        """)
        st.markdown("</div>", unsafe_allow_html=True)
