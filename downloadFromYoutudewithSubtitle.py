# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:09:14 2021

@author: moeez
"""








import pytube  
## paste
url = "https://www.youtube.com/watch?v=sWLur9lJ97s"
youtube = pytube.YouTube(url)  
downloadVideo = youtube.streams.first()

#location
location = 'E:/Local Disk/Mphil/Mphil Semester 2/Multimedia Retrieval Techniques/ass#1/'
downloadVideo.download(location)

en_caption = youtube.captions.get_by_language_code('en')

en_caption_convert_to_srt =(en_caption.generate_srt_captions())

print(en_caption_convert_to_srt)

text_file = open("subtitle.txt", "w")
text_file.write(en_caption_convert_to_srt)
text_file.close()

