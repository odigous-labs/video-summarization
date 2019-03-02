'''
Within this script, focus to test the script in objects_identifier_of_frames.py.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path.
Or can make the folder in the this scripts' folder as ./data/generated_frames according to the script.
It needs to include set of frames as .jpg files within the ./data/generated_frames folder. For that an use the video_to_frames.py script or test_video_to_frames.py script

As done in the this testing script, can use the objects_identifier_of_frames.py script in other programs.
'''

import objects_identifier_of_frames

def run():
    # image folder
    input_frames_path = "./data/generated_frames/"

    # dimensions of images
    img_width, img_height = 224, 224
    frames_predictions_dictionary = objects_identifier_of_frames.generate_object_list_of_frames(input_frames_path, img_width, img_height )

    for the_key, the_value in frames_predictions_dictionary.items():
        print(the_key, ' ---> ', the_value)

if __name__ == "__main__":
    run()