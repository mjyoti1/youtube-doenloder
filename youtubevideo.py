import pytube as py
from py import YouTube

from sys import argv

link = argv[1]
yt = YouTube("https://www.youtube.com/watch?v=vEQ8CXFWLZU")

print("Title:",yt.title)

print("view:",yt.views)

