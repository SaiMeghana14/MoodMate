import random

def get_motivational_quote(mood):
    positive_quotes = [
        "Keep shining, the world needs your light!",
        "Your smile can change someone’s day.",
        "Great things are coming your way!"
    ]
    negative_quotes = [
        "It's okay to feel down. Brighter days are ahead.",
        "Take a deep breath, you’re doing great.",
        "This too shall pass. You’ve got this!"
    ]
    neutral_quotes = [
        "Every moment is a fresh beginning.",
        "Keep moving forward, even small steps count.",
        "Stay grounded and trust the process."
    ]

    if mood == "Positive":
        return random.choice(positive_quotes)
    elif mood == "Negative":
        return random.choice(negative_quotes)
    else:
        return random.choice(neutral_quotes)
