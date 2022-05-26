#!/usr/bash/python3
''' pip install pytube '''
# Author : AmirZyber
# You Can Find Me Here : 
#                        https://zil.ink/AmirZoyber
from pytube import YouTube

# the youtube post link
yt = YouTube(input("Enter YT Video Link : "))    

# choose video or audio to download
x = input("Do You Want Video or Audio (V for Video, A for Audio) ? : ")

# input path to download on it
path = input("Enter Your path (0 for Current Directory) : ")

# get
if (x=='V' or x=='v'):
    video = yt.streams.get_highest_resolution()
elif(x=='A' or x=='a'):
    video = yt.streams.get_audio_only()

#download
if (path=='0'):
    video.download() if(x=='V' or x=='v') else video.download(filename=str(video.title)+".mp3")
else:
    video.download(path) if(x=='V' or x=='v') else video.download(path,filename=str(video.title)+".mp3")
