from textblob import TextBlob

def detect_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.5:
        return "Happy"
    elif polarity > 0.1:
        return "Content"
    elif polarity < -0.5:
        return "Sad"
    elif polarity < 0:
        return "Anxious"
    else:
        return "Neutral"
