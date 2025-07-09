import streamlit as st
import base64
import json

# Helper to load Lottie animations
from streamlit.components.v1 import html

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def show_landing_page_with_animations():
    st.markdown("""
        <style>
            .section {
                padding: 5rem 2rem;
                border-radius: 20px;
                margin-bottom: 3rem;
            }
            .hero {
                background: linear-gradient(to right, #ffdde1, #ee9ca7);
                text-align: center;
            }
            .features {
                background: linear-gradient(to right, #c9ffbf, #ffafbd);
            }
            .testimonials {
                background: linear-gradient(to right, #fbc2eb, #a6c1ee);
            }
            .team {
                background: linear-gradient(to right, #d4fc79, #96e6a1);
            }
            .faq {
                background: linear-gradient(to right, #84fab0, #8fd3f4);
            }
            .impact {
                background: linear-gradient(to right, #fccb90, #d57eeb);
            }
            .cta {
                background: linear-gradient(to right, #fdfbfb, #ebedee);
                text-align: center;
            }
            h1, h2, h3 {
                font-family: 'Segoe UI', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section
    with st.container():
        st_lottie("assets/meditation.json", 200)
        st.markdown('<div class="section hero">', unsafe_allow_html=True)
        st.markdown("""
            ## 🌈 Welcome to MoodMate
            #### Your smart companion for emotional wellness
        """)
        st.image("assets/logo.png", width=150)
        st.markdown("</div>", unsafe_allow_html=True)

    # Features Section
    with st.container():
        st_lottie("assets/chatbot.json", 200)
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
        st_lottie("assets/achievements.json", 200)
        st.markdown('<div class="section testimonials">', unsafe_allow_html=True)
        st.markdown("""
            ## 💬 What Users Say
            > *"MoodMate has changed how I check in with myself each day. I feel heard and supported."* – Ananya

            > *"The breathing and affirmations really help me stay grounded during exams."* – Rahul
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # Team Section
    with st.container():
        st.markdown('<div class="section team">', unsafe_allow_html=True)
        st.markdown("""
            ## 👥 Meet the Team
            - **Sai Meghana K** – Product Lead & Frontend
            - **John Doe** – AI/ML Engineer
            - **Jane Smith** – UX Designer & Research
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
        st_lottie("assets/meditation.json", 150)
        st.markdown('<div class="section cta">', unsafe_allow_html=True)
        st.markdown("""
            ## 🚀 Ready to start your mood journey?
            Click any section from the sidebar to begin 💖
        """)
        st.markdown("</div>", unsafe_allow_html=True)


def st_lottie(filepath, height=300):
    with open(filepath, "r") as f:
        animation_data = json.load(f)
        encoded = base64.b64encode(json.dumps(animation_data).encode()).decode()
        html(f"""
        <script src='https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js'></script>
        <lottie-player src='data:application/json;base64,{encoded}' background='transparent' speed='1' style='width:100%; height:{height}px;' loop autoplay></lottie-player>
        """, height=height)
