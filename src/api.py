from youtube_transcript_api import YouTubeTranscriptApi
video_id = ""


def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    text = []
    for snippet in fetched_transcript:
        text.append(snippet.text)

    text = " ".join(text)
    return text