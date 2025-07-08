# Motivational quotes based on mood

def get_motivational_quote(mood):
    quotes = {
        "Positive": [
            "Keep shining and stay awesome!",
            "Your positivity is contagious!",
            "Stay grateful and keep growing!"
        ],
        "Neutral": [
            "Every day is a new chance to grow.",
            "Stay balanced and keep moving.",
            "Take one step at a time."
        ],
        "Negative": [
            "Tough times never last, but tough people do.",
            "You're stronger than you think.",
            "Every storm runs out of rain."
        ]
    }
    return quotes.get(mood, ["You're doing great!"])[0]
