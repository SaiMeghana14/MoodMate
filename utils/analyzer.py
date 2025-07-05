import openai
import streamlit as st

openai.api_key = st.secrets["api"]["openai_key"]

def analyze_mood(user_input):
    prompt = f"""
You are an expert mood detection assistant. 
Classify the user's emotion from the message below into one of the following moods:
Positive, Negative, or Neutral.
Then also return a fitting emoji.

Message: "{user_input}"

Respond in this exact JSON format:
{{"mood": "Positive", "emoji": "😊"}}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and emotionally intelligent assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        import json
        result_json = response['choices'][0]['message']['content']
        result = json.loads(result_json)
        return result["mood"], result["emoji"]

    except Exception as e:
        st.error(f"⚠️ OpenAI error: {e}")
        return "Neutral", "😐"
if "api" not in st.secrets or "openai_key" not in st.secrets["api"]:
    st.error("🚨 OpenAI API key not found in Streamlit secrets!")
