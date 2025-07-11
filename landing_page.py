import streamlit as st
from utils.lottie_loader import render_lottie

def show_landing_page_with_animations():
    # 🌈 Apply Global Custom CSS
    st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #fdfbfb, #ebedee);
        }
        h2, h3 {
            color: #333;
            font-family: 'Segoe UI', sans-serif;
        }
        a {
            text-decoration: none;
            color: #ff6ec4;
            font-weight: bold;
        }
        .card {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
    </style>
    """, unsafe_allow_html=True)

    # 🧭 Top Navigation Links
    st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <a href="#features">✨ Features</a> |
        <a href="#testimonials">💬 Testimonials</a> |
        <a href="#developer">👤 Developer</a> |
        <a href="#faq">❓ FAQ</a> |
        <a href="#impact">💡 Impact</a>
    </div>
    """, unsafe_allow_html=True)

    # 🌈 Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("## 🌈 Welcome to MoodMate")
        st.markdown("Your smart companion for emotional wellness")
    with col2:
        render_lottie("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=160, is_url=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ✨ Features
    st.markdown('<h3 id="features">✨ Core Features</h3>', unsafe_allow_html=True)
    render_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json", height=180, is_url=True)
    st.markdown("""
    - 🧠 Mood Detection via Journal and Voice  
    - 🤖 Empathetic AI Chatbot  
    - 📊 Visual Mood Tracker Dashboard  
    - 🧘 Guided Meditations & Breathing  
    - 🏆 Gamified Progress Tracking
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 💬 Testimonials
    st.markdown('<h3 id="testimonials">💬 What Users Say</h3>', unsafe_allow_html=True)
    render_lottie("assets/achievements.json", height=160)

    st.markdown("""
    <div class='card'>
        “MoodMate has changed how I check in with myself each day. I feel heard and supported.”  
        <br><small>– Ananya</small>
    </div>
    <div class='card'>
        “The breathing and affirmations really help me stay grounded during exams.”  
        <br><small>– Rahul</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 👤 Developer
    st.markdown('<h3 id="developer">👤 Developer Spotlight</h3>', unsafe_allow_html=True)
    st.markdown("""
    - **K.N.V. Sai Meghana** – Developer, Designer & Creator of MoodMate  
    Passionate about emotional well-being, I built MoodMate as a smart mental health companion blending AI, journaling, and self-care features.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ❓ FAQs
    st.markdown('<h3 id="faq">❓ Frequently Asked Questions</h3>', unsafe_allow_html=True)
    st.markdown("""
    **Is my data private?** Yes, MoodMate supports end-to-end encryption.  
    **Do I need internet for this?** Only for syncing and AI features.  
    **Can I use this offline?** Yes, basic journaling and breathing tools work offline.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 💡 Real Impact
    st.markdown('<h3 id="impact">💡 Real Impact</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        “Before MoodMate, I used to bottle everything inside. Now I reflect and heal every day.”  
        <br><small>– Priya, Student</small>
    </div>
    <div class='card'>
        “Our college mental health club recommends MoodMate to help students cope better.”  
        <br><small>– Mentor</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 🚀 CTA
    st.markdown("### 🚀 Ready to Start?")
    render_lottie("assets/meditation.json", height=140)
    st.markdown("👉 Click any section from the sidebar to begin your journey 💖")

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

    # Footer
    st.markdown("""
    <hr>
    <center>
    <small>Made with 💖 by Sai Meghana | © 2025 MoodMate</small>
    </center>
    """, unsafe_allow_html=True)
