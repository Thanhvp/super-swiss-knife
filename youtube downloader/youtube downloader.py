#https://pytube.io/en/latest/index.html
from pytube import YouTube

#init
yt = YouTube("https://www.youtube.com/watch?v=3ETNUbfnj70")

#print video title
print(yt.title)    

#print video thumbnail image url
print(yt.thumbnail_url)

#print video views
print(yt.views)

#print video description
print(yt.description)

#get video stream
video = yt.streams.get_highest_resolution()

#download
video.download()

#wait until finished
print('finished')