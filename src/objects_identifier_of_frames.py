'''
Within this script, focus to identify the existing objects in a given set of frames.
Output is a dictionary, key represet the frame name and the value is the predcitions list.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path.

If need to use this script within another code then can import the script and call the functions with relevant arguments.
'''

import numpy as np
from keras.preprocessing import image
from keras.applications import resnet50
import os
from yolo.model import YOLO

def generate_object_list_of_frames(input_frames_path,img_width, img_height):
    return YOLO().predict(input_frames_path)

def run():
    # image folder
    input_frames_path = "./data/generated_frames/"

    # dimensions of images
    img_width, img_height = 224, 224

    generate_object_list_of_frames(input_frames_path,img_width, img_height )

if __name__ == "__main__":
    run()