import video_to_frames
import objects_identifier_of_frames
import os
import glob
import summary_from_frame_list
import datetime
from shutil import copyfile

def run():
    t1 = datetime.datetime.now()
    print("**************** Give the details of the video which need to summarise ****************\n")

    original_video_location = input("Enter the video path (Ex: ./data/input_video/input_video.mp4) :\n")

    location_to_store_all_frames = "./test_data/generated_frames/"
    location_to_store_summary_keyframes = "./test_data/generated_summary_keyframes/"

    try:
        if not os.path.exists(location_to_store_all_frames):
            os.makedirs(location_to_store_all_frames)
        else:
            files = glob.glob(location_to_store_all_frames+'*')
            for f in files:
                os.remove(f)
    except OSError:
        print('Error: Creating directory of data')

    video_to_frames.get_frames(original_video_location, location_to_store_all_frames)
    img_width, img_height = 224, 224

    object_identified_dictionary = objects_identifier_of_frames.generate_object_list_of_frames(
        location_to_store_all_frames,
        img_width,
        img_height
    )

    print("\n**************** Objects identified Successfully ****************")

    print(object_identified_dictionary)

    summary_frame_name_list = summary_from_frame_list.summary_from_frame_list(object_identified_dictionary, 10)

    print("\n**************** Keyframe identities of the Summary ****************")

    print(summary_frame_name_list)

    try:
        if not os.path.exists(location_to_store_summary_keyframes):
            os.makedirs(location_to_store_summary_keyframes)
        else:
            files = glob.glob(location_to_store_summary_keyframes+'*')
            for f in files:
                os.remove(f)

    except OSError:
        print('Error: Creating directory of summary data')

    for frame_name in summary_frame_name_list:
        source = location_to_store_all_frames+frame_name
        destination = location_to_store_summary_keyframes+frame_name
        copyfile(source, destination)

    print("\n**************** Keyframes moved to the ./test_data/generated_summary_keyframes/ location ****************")
    elapsed_time = datetime.datetime.now() - t1
    print ("elapsed time is "+str(elapsed_time))
if __name__ == "__main__":
    run()