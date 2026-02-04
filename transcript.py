from youtube_transcript_api import YouTubeTranscriptApi

def get_timestamped_transcript(url):
    try:
        video_id = url.split("v=")[1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        lines = []
        for item in transcript:
            seconds = int(item["start"])
            minutes = seconds // 60
            sec = seconds % 60
            timestamp = f"{minutes:02d}:{sec:02d}"
            lines.append(f"[{timestamp}] {item['text']}")

        return "\n".join(lines)

    except Exception:
        return None
