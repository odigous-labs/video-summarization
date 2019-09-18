from shutil import copyfile, rmtree
import os


class FrameSeperator:
    shot_boundaries = []
    path_to_generated_shots = None

    def __init__(self, shot_boundaries, path_to_generated_shots):
        self.shot_boundaries = shot_boundaries
        self.path_to_generated_shots = path_to_generated_shots

        if os.path.isdir(self.path_to_generated_shots):
            rmtree(self.path_to_generated_shots)
            os.mkdir(self.path_to_generated_shots)
        else:
            os.mkdir(self.path_to_generated_shots)

    def create_folders(self, path_to_generated_shots, shot_frame_path):
        prev_val = 0

        try:
            if not os.path.exists(shot_frame_path):
                os.makedirs(shot_frame_path)
        except OSError:
            print('Error: Creating directory of shot frames')

        for i, val in enumerate(self.shot_boundaries):
            shot_path = shot_frame_path + str(i + 1)
            try:
                if not os.path.exists(shot_path):
                    os.makedirs(shot_path)
            except OSError:
                print('Error: Creating directory of shot frames')

            int_val = int(val)
            for num in range(prev_val, int(val)):
                src = path_to_generated_shots + "frame" + str(num) + ".jpg"
                dst = shot_path + "/frame" + str(num) + ".jpg"
                copyfile(src, dst)
            prev_val = int(val)
