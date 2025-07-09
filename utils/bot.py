import random

def chat_with_bot(user_input):
    responses = {
        "sad": ["I'm here for you 💙", "It's okay to feel sad. Let's talk."],
        "happy": ["That's great to hear! 😄", "Keep spreading joy! 🌟"],
        "anxious": ["Try a deep breath. You're doing great.", "It's okay to feel anxious. Let's work through it."],
        "neutral": ["Want to talk or reflect a bit today?", "How about a gratitude entry?"],
    }

    for mood, res_list in responses.items():
        if mood in user_input.lower():
            return random.choice(res_list)

    return "Tell me more about how you're feeling."
