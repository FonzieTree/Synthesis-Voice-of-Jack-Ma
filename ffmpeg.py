import os
files = os.listdir('./primary/')
for file in files:
    command = 'ffmpeg.exe -i ./primary/' + file + ' -ac 1 -ar 16000 ' + './wavs/' + file.split('.')[0] + '.wav' 
    os.system(command)
