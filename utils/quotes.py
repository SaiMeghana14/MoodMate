import random

positive_quotes = [
    "Keep going, you're doing great!",
    "Happiness is a direction, not a place.",
    "Every day may not be good, but there’s something good in every day."
]

negative_quotes = [
    "Tough times never last, but tough people do.",
    "You are stronger than you think.",
    "This feeling is temporary. Keep going."
]

neutral_quotes = [
    "Take a deep breath. You're doing just fine.",
    "Stay grounded and be kind to yourself.",
    "Not every moment needs to be intense—calm is good too."
]

def get_motivational_quote(mood):
    mood = mood.lower()
    if mood == "positive":
        return random.choice(positive_quotes)
    elif mood == "negative":
        return random.choice(negative_quotes)
    else:
        return random.choice(neutral_quotes)
