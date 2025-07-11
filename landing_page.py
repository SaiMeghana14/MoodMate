import streamlit as st
from utils.lottie_loader import render_lottie

def show_landing_page_with_animations():
    st.markdown("""
        <style>
        .glass-section {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }
        .gradient-heading {
            font-size: 2rem;
            font-weight: bold;
            background: linear-gradient(90deg, #ff758c, #ff7eb3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 1rem;
        }
        .scroll-top-button {
            position: fixed;
            bottom: 30px;
            right: 25px;
            z-index: 100;
            background-color: #6c63ff;
            color: white;
            padding: 10px 16px;
            border-radius: 50px;
            font-size: 18px;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        .scroll-top-button:hover {
            background-color: #4e47c2;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='gradient-heading'>🌈 Welcome to MoodMate</div>", unsafe_allow_html=True)
    st.caption("Your smart companion for emotional wellness")

    # 🌟 Features
    with st.expander("✨ Core Features", expanded=True):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        render_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json", height=180, is_url=True)
        st.markdown("""
        - Mood Detection via Journal and Voice  
        - Empathetic AI Chatbot  
        - Visual Mood Tracker Dashboard  
        - Guided Meditations & Breathing  
        - Gamified Progress Tracking
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # 💬 Testimonials
    with st.expander("💬 What Users Say"):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        render_lottie("assets/achievements.json", height=180)
        st.markdown("""
        > *"MoodMate has changed how I check in with myself each day. I feel heard and supported."* – Ananya  
        > *"The breathing and affirmations really help me stay grounded during exams."* – Rahul
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # 👤 Developer Spotlight
    with st.expander("👤 Developer Spotlight"):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        st.markdown("""
        - **K.N.V. Sai Meghana** – Developer, Designer & Creator of MoodMate  
        Passionate about emotional well-being, I built MoodMate as a smart mental health companion blending AI, journaling, and self-care features.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ❓ FAQ
    with st.expander("❓ Frequently Asked Questions"):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        st.markdown("""
        **Is my data private?** Yes, MoodMate supports end-to-end encryption.  
        **Do I need internet for this?** Only for syncing and AI features.  
        **Can I use this offline?** Yes, basic journaling and breathing tools work offline.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # 💡 Impact
    with st.expander("💡 Real Impact"):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        st.markdown("""
        *"Before MoodMate, I used to bottle everything inside. Now I reflect and heal every day."* – Priya, Student  
        *"Our college mental health club recommends MoodMate to help students cope better."* – Mentor
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # 🚀 CTA
    with st.expander("🚀 Ready to Start?"):
        st.markdown("<div class='glass-section'>", unsafe_allow_html=True)
        render_lottie("assets/meditation.json", height=150)
        st.markdown("Click any section above to begin your journey 💖")
        st.markdown("</div>", unsafe_allow_html=True)

    # ⬆️ Scroll to top button
    st.markdown("""
        <button class="scroll-top-button" onclick="window.scrollTo({top: 0, behavior: 'smooth'});">↑</button>
    """, unsafe_allow_html=True)
