PROMPTS = {
    "overview": """
You are an expert content analyst.

Summarize the following video transcript by clearly explaining:
- What the video is about
- The main ideas discussed
- Important points or arguments
- Key conclusions or takeaways

Write in clear, well-structured markdown.
Avoid unnecessary fluff.

Transcript:
{text}
""",

    "educational": """
You are an expert educator.

Convert the following transcript into structured learning notes.
- Use clear headings
- Break concepts into bullet points
- Explain ideas simply and logically
- Highlight examples or definitions where relevant

Transcript:
{text}
""",

    "bullet points": """
Summarize the following transcript into concise bullet points.
- Focus only on the most important ideas
- Remove repetition
- Keep each point short and clear

Transcript:
{text}
""",

    "insights": """
You are an insightful analyst.

Extract the most meaningful insights from the transcript, including:
- Important observations
- Patterns or themes
- Noteworthy statements
- Practical or real-world implications

Present the output in structured markdown.

Transcript:
{text}
""",

    "snarky": """
You are a sharp, witty summarizer.

Summarize the transcript in a slightly sarcastic, playful tone,
but remain accurate and respectful.
Do not distort facts.

Transcript:
{text}
"""
}

