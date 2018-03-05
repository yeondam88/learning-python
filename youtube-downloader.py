import os
import pytube
import subprocess

videoURL = input('Youtube Url?')

yt = pytube.YouTube(videoURL)
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ' , ', videos[i])

quality = int(input('Resolution? (0~21) lower is better'))

down_dir = os.getcwd()

videos[quality].download(down_dir)

question = input('Do you want to convert the video to mp3? [y/n]').lower()

if question == 'y':
    newFileName = input('Name of converting mp3 file?')
    oriFileName = videos[quality].default_filename

    subprocess.call([
        'ffmpeg', '-i',
        os.path.join(down_dir, oriFileName)
        os.path.join(down_dir, newFileName)
    ])

    print('Video download and converting completed.')
else:
    print('Your video download completed..')
