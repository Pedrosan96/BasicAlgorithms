from moviepy.editor import VideoFileClip
from time import sleep
import os

PROJECT_DIR = os.path(__file__)


full_video = r"C:\Users\pdsan\Videos\2024-08-03 10-12-06.mkv"
current_duration = VideoFileClip(full_video).duration
divide_into_count = 11.5
single_duration = current_duration/divide_into_count
current_video = f"{current_duration}.mkv"

while current_duration > single_duration:
    clip = VideoFileClip(full_video).subclip(current_duration-single_duration, current_duration)
    current_duration -= single_duration
    current_video = f"{current_duration}.mkv"
    clip.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')

    print("-----------------###-----------------")