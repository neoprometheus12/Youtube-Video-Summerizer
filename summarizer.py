from gemini_client import generate
from utils import chunk_text
from prompts import PROMPTS

def summarize(text, mode):
    chunks = chunk_text(text, max_chars=6000)
    outputs = []

    for chunk in chunks:
        prompt = PROMPTS[mode].format(text=chunk)
        outputs.append(generate(prompt))

    return "\n\n".join(outputs)
