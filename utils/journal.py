import json
from datetime import datetime
import os

DB_FILE = "journal_entries.json"

def save_entry(entry, mood):
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    data.append({
        "timestamp": datetime.now().isoformat(),
        "entry": entry,
        "mood": mood
    })

    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def get_entries():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)
