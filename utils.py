
def chunk_text(text, max_chars=6000):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
