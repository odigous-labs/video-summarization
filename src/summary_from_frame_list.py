def summary_from_frame_list(frame_list_with_objects, threshold_of_objects_in_frame):
    object_array = []
    summary_frames = []

    for i in range(len(frame_list_with_objects)):
        obj_list = frame_list_with_objects[list(frame_list_with_objects.keys())[i]]

        for j in range(threshold_of_objects_in_frame):
            if (obj_list[j] not in object_array):
                object_array.append(obj_list[j])

                frame_name = list(frame_list_with_objects.keys())[i]
                if (frame_name not in summary_frames):
                    summary_frames.append(frame_name)

    return summary_frames
