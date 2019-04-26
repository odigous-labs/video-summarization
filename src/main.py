import os
import glob
import datetime
from shutil import copyfile

import video_to_frames
from frame_seperater import FrameSeperator
import create_shot_boundaries
import objects_identifier_of_frames
import summary_from_frames_with_obj


def run():
    t1 = datetime.datetime.now()
    print("**************** Give the details of the video which need to summarise ****************\n")

    original_video_location = input("Enter the video path (Ex: ./data/input_video/input_video.mp4) :\n")

    location_to_store_all_frames = "./test_data/generated_frames/"
    location_to_store_shot_frames = "./test_data/shot_frames/"
    location_to_store_summary_keyframes = "./test_data/generated_summary_keyframes/"

    try:
        if not os.path.exists(location_to_store_all_frames):
            os.makedirs(location_to_store_all_frames)
        else:
            files = glob.glob(location_to_store_all_frames + '*')
            for f in files:
                os.remove(f)
    except OSError:
        print('Error: Creating directory of data')

    # video broken to frames
    video_to_frames.get_frames(original_video_location, location_to_store_all_frames)

    # shot boundaries are identified
    shot_boundaries = create_shot_boundaries.run(location_to_store_all_frames)

    print("Folder Creating Process Started")
    frame_seperator = FrameSeperator(shot_boundaries, location_to_store_shot_frames)
    frame_seperator.create_folders(location_to_store_all_frames, location_to_store_shot_frames)
    print("Process Finished Successfully")

    object_identified_dictionary = objects_identifier_of_frames.generate_object_list_of_frames(
        location_to_store_shot_frames
    )

    print("\n**************** Objects identified Successfully ****************")

    print(object_identified_dictionary)

    summary_list_of_shots = []
    for i in object_identified_dictionary:
        summary_list_of_shots.append(summary_from_frames_with_obj.summary_from_frames_with_obj(i))

    summary_frame_name_list = [item for sublist in summary_list_of_shots for item in sublist]

    print("\n**************** Keyframe identities of the Summary ****************")

    print(summary_frame_name_list)

    try:
        if not os.path.exists(location_to_store_summary_keyframes):
            os.makedirs(location_to_store_summary_keyframes)
        else:
            files = glob.glob(location_to_store_summary_keyframes + '*')
            for f in files:
                os.remove(f)

    except OSError:
        print('Error: Creating directory of summary data')

    for frame_name in summary_frame_name_list:
        source = location_to_store_all_frames + frame_name
        destination = location_to_store_summary_keyframes + frame_name
        copyfile(source, destination)

    print(
        "\n**************** Keyframes moved to the ./test_data/generated_summary_keyframes/ location ****************")
    elapsed_time = datetime.datetime.now() - t1
    print("elapsed time is " + str(elapsed_time))


if __name__ == "__main__":
    run()
