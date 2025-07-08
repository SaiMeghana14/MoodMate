# Sentiment analysis logic using VADER and Hugging Face Transformers
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Download required resources
nltk.download("vader_lexicon", quiet=True)

# Initialize analyzers
vader = SentimentIntensityAnalyzer()
huggingface_pipeline = pipeline("sentiment-analysis")

def analyze_mood(text, use_transformer=False):
    """
    Returns (mood, emoji) based on input text.
    Uses Hugging Face if use_transformer=True, else VADER (offline).
    """
    if use_transformer:
        result = huggingface_pipeline(text)[0]
        label = result["label"]

        if "POSITIVE" in label:
            return "Positive", "😊"
        elif "NEGATIVE" in label:
            return "Negative", "😞"
        else:
            return "Neutral", "😐"
    else:
        scores = vader.polarity_scores(text)
        compound = scores["compound"]
        if compound >= 0.05:
            return "Positive", "😊"
        elif compound <= -0.05:
            return "Negative", "😞"
        else:
            return "Neutral", "😐"
