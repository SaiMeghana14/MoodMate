# ✅ utils/journal.py
import json
from datetime import datetime
import os
from fpdf import FPDF

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

def export_pdf():
    entries = get_entries()
    if not entries:
        st.warning("No journal entries to export.")
        return
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="MoodMate Journal Entries", ln=1, align="C")
    for entry in entries:
        date = entry["timestamp"][:10]
        mood = entry["mood"]
        text = entry["entry"]
        pdf.multi_cell(0, 10, txt=f"[{date}] Mood: {mood}\n{text}\n")
    pdf.output("MoodMate_Journal.pdf")
    with open("MoodMate_Journal.pdf", "rb") as f:
        st.download_button("Download PDF", f, file_name="MoodMate_Journal.pdf")
