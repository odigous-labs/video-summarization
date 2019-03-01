'''
Within this script, focus to test the script in frames_to_video.py.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path and output file path.
Or can make the folders in the similar folder as ./data/generated_frames and as ./data/output_video/ according to the script.
It needs to include set of frames as .jpg files within the ./data/generated_frames folder. For that an use the video_to_frames.py script or test_video_to_frames.py script

As done in the this testing script, can use the video_to_frames.py script in other programs.
'''

import frames_to_video

def run():
    input_frames_path = "./data/generated_frames/"
    output_video_path = "./data/output_video/"
    output_video_name = "output_video.avi"
    fps = 25.0
    frames_to_video.convert_frames_to_video(input_frames_path, output_video_path, output_video_name, fps)

if __name__ == "__main__":
    run()

