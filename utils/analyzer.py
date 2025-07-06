import streamlit as st
import json
import random

# Try importing OpenAI only in online mode
try:
    import openai
    from openai import OpenAI
    openai_client = OpenAI(api_key=st.secrets["api"]["openai_key"])
except:
    openai_client = None

offline_moods = [
    {"mood": "Positive", "emoji": "😊"},
    {"mood": "Negative", "emoji": "😞"},
    {"mood": "Neutral", "emoji": "😐"}
]

def analyze_mood(user_input, use_openai=True):
    if use_openai and openai_client:
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
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and emotionally intelligent assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            result_json = response.choices[0].message.content
            result = json.loads(result_json)
            return result["mood"], result["emoji"]

        except json.JSONDecodeError:
            st.warning("⚠️ Couldn't decode OpenAI response. Falling back to Neutral.")
            return "Neutral", "😐"
        except Exception as e:
            st.error(f"⚠️ OpenAI Error: {e}")
            return "Neutral", "😐"
    else:
        return random.choice(offline_moods)
