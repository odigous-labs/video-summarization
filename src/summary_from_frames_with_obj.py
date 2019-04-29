def summary_from_frames_with_obj(frame_dic_with_objects):
    frames_with_max_obj = []
    redundant_frames = []
    summary_frames = []

    for i in range(len(frame_dic_with_objects)):
        frame = frame_dic_with_objects[list(frame_dic_with_objects.keys())[i]]

        if len(frame) != 0:
            new_obj = True
            for obj_frame_index in range(len(frames_with_max_obj)):
                if set(frame).issubset(set(frames_with_max_obj[obj_frame_index])):
                    new_obj = False
                    break
                elif set(frames_with_max_obj[obj_frame_index]).issubset(set(frame)):
                    if frames_with_max_obj[obj_frame_index] not in redundant_frames:
                        redundant_frames.append(frames_with_max_obj[obj_frame_index])

            if new_obj:
                frames_with_max_obj.append(frame)

                frame_name = list(frame_dic_with_objects.keys())[i]

                if frame_name not in summary_frames:
                    summary_frames.append(frame_name)

    for obj_set in redundant_frames:
        redundant_index = frames_with_max_obj.index(obj_set)
        frames_with_max_obj.pop(redundant_index)
        summary_frames.pop(redundant_index)

    for i in frames_with_max_obj:
        print(i)

    return summary_frames


# summary_from_frames_with_obj({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3], 'c': [1, 2, 5, 6, 7], 'e': [2, 5, 7]})
