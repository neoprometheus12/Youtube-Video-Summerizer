from youtube_transcript_api import YouTubeTranscriptApi

def get_timestamped_transcript(url):
    video_id = url.split("v=")[1].split("&")[0]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    formatted = []
    for item in transcript:
        time = int(item["start"])
        minutes = time // 60
        seconds = time % 60
        timestamp = f"{minutes:02d}:{seconds:02d}"
        formatted.append(f"[{timestamp}] {item['text']}")

    return "\n".join(formatted)

