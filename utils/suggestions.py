def get_suggestions(mood):
    suggestions = {
        "Happy": ["Celebrate your joy!", "Share your smile with someone."],
        "Sad": ["Listen to soothing music.", "Write down your feelings."],
        "Anxious": ["Try a breathing exercise.", "Take a short walk in nature."],
        "Tired": ["Get some rest.", "Stretch or meditate for 5 minutes."],
        "Neutral": ["Try journaling your thoughts.", "Watch an inspiring video."]
    }
    return suggestions.get(mood, ["Take a deep breath.", "You’re doing well!"])
