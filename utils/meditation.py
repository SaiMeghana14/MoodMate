import streamlit as st

def show_breathing_animation():
    st.markdown("### 🧘‍♀️ Breathe In... Breathe Out")
    st.components.v1.html("""
    <html>
    <body>
    <div style='display: flex; justify-content: center; align-items: center; height: 300px;'>
      <div style='
        width: 100px;
        height: 100px;
        background-color: #A0E7E5;
        border-radius: 50%;
        animation: breathe 8s ease-in-out infinite;
      '></div>
    </div>
    <style>
    @keyframes breathe {
        0% { transform: scale(1); }
        50% { transform: scale(1.8); }
        100% { transform: scale(1); }
    }
    </style>
    </body>
    </html>
    """, height=320)
