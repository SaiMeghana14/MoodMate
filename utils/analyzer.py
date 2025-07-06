import streamlit as st

def analyze_mood(user_input, use_openai=True):
    if use_openai:
        import openai
        from openai import OpenAI

        client = OpenAI(api_key=st.secrets["api"]["openai_key"])

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
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and emotionally intelligent assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            import json
            result_json = response.choices[0].message.content
            result = json.loads(result_json)
            return result["mood"], result["emoji"]

        except Exception as e:
            st.error(f"⚠️ OpenAI error: {e}")
            return "Neutral", "😐"
    else:
        msg = user_input.lower()
        if any(w in msg for w in ["happy", "joy", "great", "good", "excited"]):
            return "Positive", "😊"
        elif any(w in msg for w in ["sad", "tired", "angry", "bad", "upset"]):
            return "Negative", "😔"
        else:
            return "Neutral", "😐"
    except Exception as e:
        if "insufficient_quota" in str(e):
            st.warning("⚠️ OpenAI quota exceeded. Switching to offline mode.")
            return offline_mood_analysis(user_input)  # your fallback logic
        else:
            st.error(f"⚠️ OpenAI error: {e}")
            return "Neutral", "😐"
