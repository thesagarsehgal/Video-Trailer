from youtube_transcript_api import YouTubeTranscriptApi
import json

video_id = input("enter the youtube video ID:- ")

subtitles = YouTubeTranscriptApi.get_transcript(video_id,languages=["en"])
print(subtitles)

with open("subtitles.json","w") as f:
	json.dump(subtitles,f)