import streamlit as st

def language_settings_page():
    st.subheader("🌐 Multilingual Support")

    lang = st.selectbox("Choose your language:", ["English", "Telugu", "Hindi", "Tamil"])
    affirmations = {
        "English": "You are strong and capable.",
        "Telugu": "మీరు బలంగా ఉన్నారు మరియు మీకు ఇది సాధ్యమే.",
        "Hindi": "आप सक्षम और मजबूत हैं।",
        "Tamil": "நீங்கள் திறமையானவரும் வலிமையானவரும் நீங்கள்."
    }

    st.markdown(f"### ✨ Today's Affirmation in {lang}:")
    st.success(affirmations[lang])
