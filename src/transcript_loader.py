import re
from youtube_transcript_api import YouTubeTranscriptApi


class TranscriptLoader:

    @staticmethod
    def extract_video_id(url):

        patterns = [
            r"(?:v=)([a-zA-Z0-9_-]{11})",
            r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})"
        ]

        for pattern in patterns:

            match = re.search(pattern, url)

            if match:
                return match.group(1)

        raise ValueError("Invalid URL")

    @staticmethod
    def get_transcript(url):

        video_id = TranscriptLoader.extract_video_id(url)

        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id,
            languages=["en", "hi"]
        )

        text = " ".join(
            snippet.text
            for snippet in transcript
        )

        return text