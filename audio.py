from pytube import YouTube
import os

yt = YouTube('your youtube URL')

video = yt.streams.filter(only_audio=True).first()

out_file = video.download(output_path=".")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
