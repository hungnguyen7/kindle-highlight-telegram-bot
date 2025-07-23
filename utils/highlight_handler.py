import re
import json
import random
import os
from database.highlights import Highlights

# Initialize highlights database
highlights_db = Highlights()


def process_highlights_from_content(content):
    """Process highlights from file content and return list of highlights"""
    # * Split content by \n and remove empty lines
    lines = content.split("\n")
    lines = [line for line in lines if line.strip()]
    # * Determine the index of =======
    indices = [i for i, line in enumerate(lines) if "==========" in line]

    # * Pre-proceed the highlights
    pre_proceeded_highlights = []
    for i in range(len(indices)):
        if i == 0:
            pre_proceed_highlight = lines[:indices[i]]
        else:
            pre_proceed_highlight = lines[indices[i - 1]+1:indices[i]]

        # * If the highlight is less than 3 lines, skip it because that highlight is not complete
        if len(pre_proceed_highlight) < 3:
            continue

        pre_proceeded_highlights.append(pre_proceed_highlight)

    highlights = []

    pattern = r"^- Your (Highlight|Bookmark|Note) on (page [0-9]+ \| )?Location ([0-9]+(?:-[0-9]+)?) \| Added on (.*?)$"
    for highlight in pre_proceeded_highlights:
        match = re.findall(pattern, highlight[1], re.MULTILINE | re.DOTALL)
        if not match:
            continue
            
        book_title = highlight[0].strip()
        location = match[0][2].strip()
        timestamp = match[0][3].strip()
        text = highlight[2].strip()
        highlights.append({
            "book_title": book_title,
            "location": location,
            "timestamp": timestamp,
            "text": text
        })

    return highlights


def store_and_process_highlights(chat_id, file_content):
    """Store and process highlights from uploaded file content"""
    # Decode content if it's bytes
    if isinstance(file_content, bytes):
        content = file_content.decode('utf-8')
    else:
        content = file_content
    
    # Process highlights from content
    highlights = process_highlights_from_content(content)
    
    # Store in database
    highlights_db.add_highlights(chat_id, highlights)


def load_random_highlight(chat_id):
    """Load a random highlight for the given chat_id"""
    return highlights_db.get_random_highlight(chat_id)


# * Helper function to format the highlights
def format_highlight(highlights):
    if highlights is None:
        return "No highlights found. Please import highlights first using /import."

    return (f"📚 *{highlights['book_title']}*"
            f"\n📍 Location: {highlights['location']}"
            f"\n🕒 Added on: {highlights['timestamp']}"
            f"\n\n{highlights['text']}")
