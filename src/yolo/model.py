import os
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm

from src.net.netarch import YoloArchitecture,YoloInferenceModel


class YOLO(object):

    def __init__(self):
        self.debug_timings = True
        self.yolo_arch = YoloArchitecture()
        self.model = self.yolo_arch.get_model()
        self.inf_model = YoloInferenceModel(self.model)


    def predict(self, path_to_frames):

        #this function will return a dictionary with predicted objects as follows
        #{frame0:[obj1,obj2,obj3],frame1:[obj1,obj2]....}

        frames_predictions_dictionary = {}
        #checking whether the given path is a directory
        if os.path.isdir(path_to_frames):
            fnames = [os.path.join(path_to_frames, f) for f in os.listdir(path_to_frames)
                      if os.path.isfile(os.path.join(path_to_frames, f))]

        else:
            fnames = [path_to_frames]
            flag = False

        for f in tqdm(fnames, desc='Processing Batch'):
            image = cv2.imread(f)
            labels = []
            labels = self.inf_model.predict(image.copy())
            frames_predictions_dictionary[str(f)[len(path_to_frames):]] = labels

        print ("Object Identification Process Finished")
        return frames_predictions_dictionary