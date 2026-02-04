import whisper
import yt_dlp
import os

def transcribe_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    model = whisper.load_model("base")
    result = model.transcribe("audio.webm")

    os.remove("audio.webm")

    return result["text"]

