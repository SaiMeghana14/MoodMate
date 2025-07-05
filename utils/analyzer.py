import streamlit as st

# Try importing OpenAI only if available
try:
    import openai
    openai_available = True
except ImportError:
    openai_available = False

def analyze_mood(user_input, use_openai=True):
    """
    Analyze user mood using OpenAI (online) or simple keyword detection (offline).
    Controlled by the toggle from Streamlit UI.
    """

    # ✅ Check if OpenAI mode is selected and API key is present
    if use_openai and openai_available and "api" in st.secrets and "openai_key" in st.secrets["api"]:
        openai.api_key = st.secrets["api"]["openai_key"]

        # GPT-based mood analysis prompt
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

            result_json = response['choices'][0]['message']['content']
            st.write("🧠 Raw OpenAI response:", result_json)  # Debug print

            import json
            result = json.loads(result_json)
            return result["mood"], result["emoji"]

        except json.JSONDecodeError:
            st.error("⚠️ OpenAI response was not valid JSON.")
            st.write("🔍 Raw response:", result_json)
            return "Neutral", "😐"

        except Exception as e:
            st.error(f"⚠️ OpenAI API Error: {e}")
            return "Neutral", "😐"

    else:
        # 🚫 Offline fallback: Rule-based mood analysis
        st.info("🧪 Running in Offline (Keyword-based) Mode")
        user_input = user_input.lower()

        positive_words = ["happy", "great", "excited", "good", "amazing", "joy", "love", "fun"]
        negative_words = ["sad", "depressed", "bad", "angry", "tired", "upset", "worried", "hate"]

        if any(word in user_input for word in positive_words):
            return "Positive", "😊"
        elif any(word in user_input for word in negative_words):
            return "Negative", "😞"
        else:
            return "Neutral", "😐"
