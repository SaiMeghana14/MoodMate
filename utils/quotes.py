import random

quotes = {
    "Positive": [
        "Keep shining, the world needs your light!",
        "Happiness looks good on you!",
        "You're doing great! Keep it up!"
    ],
    "Negative": [
        "It's okay to feel down. Tomorrow is a new day.",
        "Every storm runs out of rain. You've got this.",
        "You're stronger than you think."
    ],
    "Neutral": [
        "Balance is a beautiful thing.",
        "Stay grounded and centered.",
        "Sometimes, just being is enough."
    ]
}

def get_motivational_quote(mood):
    return random.choice(quotes.get(mood, quotes["Neutral"]))
