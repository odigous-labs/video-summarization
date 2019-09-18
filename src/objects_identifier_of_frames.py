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

from yolo.model import YOLO


def generate_object_list_of_frames(input_frames_path):
    return YOLO().predict(input_frames_path)


def run():
    # image folder
    input_frames_path = "./data/generated_frames/"

    a = generate_object_list_of_frames(input_frames_path)
    print(a)


if __name__ == "__main__":
    run()
