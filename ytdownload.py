#Import Files
from pytube import YouTube
from pytube import Playlist
import os
import sys

#Code Start from Here
print("Download Playlist(2) or Video(1) Audio(3): ")
observer = int(input("Click 1 for Video , 2 for Playlist , 3 for Audio: "))

# Progess Function
def progress_func(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)

    #print(f'Total Size: {totalsz} MB')
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')




if(observer== 1):
    link = input("Enter URL Here: ")
  

    yt = YouTube(
            link,
            on_progress_callback=progress_func,   
        )


    print("Tittle: " , yt.title)
    print("View: " , yt.views)

    yd = yt.streams.get_highest_resolution()
    

    yd.download('\Shubham\Coding\Python Code\project\download')
    print("Video Downloaded")

elif(observer==2):

    p_link = input("Enter PlaylistURL Here: ")
    p = Playlist(p_link
    )
    print(f'Downloading: {p.title}')
    i = 1
    for video in p.videos:

           
            video.streams.first().download('\Shubham\Coding\Python Code\project\download')
            print(i," Video Downloaded")
            i += 1
    
    print("All Video in Playlist Downloaded")

    

elif(observer==3):
    a_link = input("Enter AudioURL Here: ")
    audio_file = YouTube(a_link).streams.filter(only_audio=True).get_by_itag(251).download('\Shubham\Coding\Python Code\project\download')
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)

  
    print("Audio Downloaded")

else:
     print("Press Correct Key")



# Code written by Shubham Kumar Jaiswal
