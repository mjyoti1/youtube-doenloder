from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube("https://www.youtube.com/watch?v=0BoBTbnFK8A&list=PLf0LpPWikpPe5gc6fT9wDj3Y6e97z6ZD_&index=60")

print("Title:",yt.title)

print("view:",yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('C:/Users/admin/Desktop/Downloaded video/youtube Download')
