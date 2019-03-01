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
import os
from os.path import isfile, join

def convert_frames_to_video(input_frames_path, output_video_path, output_video_name, fps):

    if (os.path.isdir(input_frames_path)):

        frame_array = []

        files = [file for file in os.listdir(input_frames_path) if isfile(join(input_frames_path, file))]

        # Sort the frames order by the name
        files.sort(key=lambda x: int(x[5:-4]))

        if(len(files)!=0):

            try:
                # validate the exitence of the output location to save the output video
                if not os.path.exists(output_video_path):
                    os.makedirs(output_video_path)
            except OSError:
                print('Error: Creating directory of data')

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
            out = cv2.VideoWriter(output_video_path+output_video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

            for i in range(len(frame_array)):
                # writing to a image array
                out.write(frame_array[i])
            out.release()
        else:
            print("Need to include frames in the required format within the given location of frames.")
    else:
        print("Given path of the frames not exists.")

def run():
    input_frames_path = "./data/generated_frames/"
    output_video_path = "./data/output_video/"
    output_video_name = "output_video.avi"
    fps = 25.0
    convert_frames_to_video(input_frames_path, output_video_path, output_video_name, fps)

if __name__ == "__main__":
    run()