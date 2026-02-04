
from gemini_client import generate
from utils import chunk_text
from prompts import SYSTEM_PROMPTS

def summarize(text, mode):
    chunks = chunk_text(text, max_chars=6000)
    summaries = []

    for chunk in chunks:
        prompt = SYSTEM_PROMPTS[mode].format(text=chunk)
        summaries.append(generate(prompt))

    return "\n\n".join(summaries)
