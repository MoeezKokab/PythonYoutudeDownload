# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:09:14 2021

@author: moeez
"""








import pytube  
from pytube import YouTube  
# paste
url = "https://www.youtube.com/watch?v=IICfQKTfqCQ"
youtube = pytube.YouTube(url)  
downloadVideo = youtube.streams.first()
#location
location = 'E:/Local Disk/'
downloadVideo.download(location)

video =  pytube.YouTube(url)   
#info about vidoe
print(video.title)  
print(video.video_id)  
print(video.description)  
print(video.length)  
print(video.thumbnail_url)  
print(video.views)  
print(video.rating)  
print(video.age_restricted)  
print("ok")