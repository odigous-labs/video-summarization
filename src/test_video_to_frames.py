'''
Within this script, focus to test the script in video_to_frames.py.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path and output file path.
Or can make the folders in the similar folder as ./data/input_video and as ./data/generated_frames according to the script.
The input video can move to the ./data/input_video location and rename as input_video.mp4

As done in the this testing script, can use the video_to_frames.py script in other programs.
'''

import video_to_frames

def run():
    video_input_path = "./data/input_video/input_video.mp4"
    frame_output_path = "./data/generated_frames/"
    video_to_frames.get_frames(video_input_path, frame_output_path)

if __name__ == "__main__":
    run()

