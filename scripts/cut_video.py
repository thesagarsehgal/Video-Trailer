from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("../../video1.mp4", 16.07, 16.07+1.564, targetname="./test.mp4")