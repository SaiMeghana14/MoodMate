# ✅ utils/ui.py
import streamlit as st

def set_theme_by_mood(mood):
    color_map = {
        "Happy": "#FFF176",
        "Sad": "#90CAF9",
        "Anxious": "#B39DDB",
        "Tired": "#B0BEC5",
        "Neutral": "#E0E0E0"
    }
    color = color_map.get(mood, "#E0E0E0")
    st.markdown(f"""
        <style>
        body {{
            background-color: {color};
        }}
        </style>
    """, unsafe_allow_html=True)
