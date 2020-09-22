# This python script converts one format of audio/video file into another format
# using ffmpeg.
# For that, you need to install ffmpeg
# and install the python package ffmpy

from ffmpy import FFmpeg
import os

oldpath = '/path/of/original/files/'
newpath = '/path/of/converted/files/'
os.mkdir(newpath)

for i in range(n): # n corresponds to the number of files
    input = oldpath + 'recorder-' + str(i) + '.webm' # or any other format
    output = newpath + 'recorder-' + str(i) + '.wav' # or any other format
    ff = FFmpeg(
         inputs={input: None},
         outputs={output: None}
    )
    ff.run()
