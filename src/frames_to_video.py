'''
Within this script, focus to convert given set of frames to a video.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path and output file path.

If need to use this script within another code then can import the script and call the functions with relevant arguments.
'''

import cv2
import numpy as np
import os
from os.path import isfile, join

def convert_frames_to_video(input_frames_path, output_video_path, fps):
    frame_array = []
    files = [file for file in os.listdir(input_frames_path) if isfile(join(input_frames_path, file))]

    # Sort the frames order relevant to the name
    files.sort(key=lambda x: int(x[5:-4]))

    if(len(files)!=0):
        for i in range(len(files)):
            # reading image files
            filename = input_frames_path + files[i]
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            print(filename)

            # inserting the current frame into the frame array
            frame_array.append(img)

        # Initiate the output video file
        out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(frame_array)):
            # writing to a image array
            out.write(frame_array[i])
        out.release()
    else:
        print("Need to include frames in the required format within the given location of frames.")

def run():
    input_frames_path = "./data/generated_frames/"
    output_video_path = "./data/output_video/output_video.avi"
    fps = 25.0
    convert_frames_to_video(input_frames_path, output_video_path, fps)

if __name__ == "__main__":
    run()