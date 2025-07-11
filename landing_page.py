import streamlit as st
from utils.lottie_loader import render_lottie

def show_landing_page_with_animations():
    # ✅ Inline styles for gradient backgrounds
    st.markdown("""
        <style>
            .section {
                padding: 5rem 2rem;
                border-radius: 20px;
                margin-bottom: 3rem;
            }
            .hero { background: linear-gradient(to right, #ffdde1, #ee9ca7); text-align: center; }
            .features { background: linear-gradient(to right, #c9ffbf, #ffafbd); }
            .testimonials { background: linear-gradient(to right, #fbc2eb, #a6c1ee); }
            .team { background: linear-gradient(to right, #d4fc79, #96e6a1); }
            .faq { background: linear-gradient(to right, #84fab0, #8fd3f4); }
            .impact { background: linear-gradient(to right, #fccb90, #d57eeb); }
            .cta { background: linear-gradient(to right, #fdfbfb, #ebedee); text-align: center; }
            h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Hero Section
    with st.container():
        render_lottie("assets/meditation.json", height=200)
        st.markdown('<div class="section hero">', unsafe_allow_html=True)
        st.markdown("""
            ## 🌈 Welcome to MoodMate  
            #### Your smart companion for emotional wellness
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ✅ Features Section
    with st.container():
        render_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json", height=200, is_url=True)
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

    # ✅ Testimonials Section
    with st.container():
        render_lottie("assets/achievements.json", height=200)
        st.markdown('<div class="section testimonials">', unsafe_allow_html=True)
        st.markdown("""
            ## 💬 What Users Say  
            > *"MoodMate has changed how I check in with myself each day. I feel heard and supported."* – Ananya  
            > *"The breathing and affirmations really help me stay grounded during exams."* – Rahul
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ✅ Developer Section
    with st.container():
        st.markdown('<div class="section team">', unsafe_allow_html=True)
        st.markdown("""
            ## 👤 Developer Spotlight  
            - **K.N.V. Sai Meghana** – Developer, Designer & Creator of MoodMate  
            Passionate about emotional well-being, I built MoodMate as a smart mental health companion blending AI, journaling, and self-care features.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ✅ FAQ Section
    with st.container():
        st.markdown('<div class="section faq">', unsafe_allow_html=True)
        st.markdown("""
            ## ❓ Frequently Asked Questions  
            **Is my data private?** Yes, MoodMate supports end-to-end encryption.  
            **Do I need internet for this?** Only for syncing and AI features.  
            **Can I use this offline?** Yes, basic journaling and breathing tools work offline.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ✅ Impact Section
    with st.container():
        st.markdown('<div class="section impact">', unsafe_allow_html=True)
        st.markdown("""
            ## 💡 Real Impact  
            *"Before MoodMate, I used to bottle everything inside. Now I reflect and heal every day."* – Priya, Student  
            *"Our college mental health club recommends MoodMate to help students cope better."* – Mentor
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ✅ Call to Action Section
    with st.container():
        render_lottie("assets/meditation.json", height=150)
        st.markdown('<div class="section cta">', unsafe_allow_html=True)
        st.markdown("""
            ## 🚀 Ready to start your mood journey?  
            Click any section from the sidebar to begin 💖
        """)
        st.markdown("</div>", unsafe_allow_html=True)
