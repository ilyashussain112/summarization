from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from gtts import gTTS
import os

def generate_audio(text, filename):
    if not text.strip():
        print("Empty text received. Skipping audio generation.")
        return

    tts = gTTS(text=text, lang='en')
    output_path = os.path.join("static", filename)
    tts.save(output_path)
    print(f"Audio saved at {output_path}")

def preprocessing(url):
    try:
        parsed_url = urlparse(url)
        if "youtube.com" in parsed_url.netloc:
            query = parse_qs(parsed_url.query)
            return query.get("v", [None])[0]
        elif "youtu.be" in parsed_url.netloc:
            return parsed_url.path.strip("/")
        else:
            return None
    except:
        return None


def get_transcript(video_id):
    if not video_id:
        print("Empty video_id passed to get_transcript")
        return "Invalid video ID."

    try:
        fetched_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([snippet["text"] for snippet in fetched_transcript])
        return text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return "Could not fetch transcript."
