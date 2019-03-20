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

    def predict(self,path):
        frames_predictions_dictionary = {}
        #checking whether the given path is a directory
        if os.path.isdir(path):
            fnames = [os.path.join(path, f) for f in os.listdir(path)
                      if os.path.isfile(os.path.join(path, f))]

        else:
            fnames = [path]
            flag = False

        for f in tqdm(fnames, desc='Processing Batch'):
            image = cv2.imread(f)
            labels_limited = [None]*10
            labels = self.inf_model.predict(image.copy())
            size = len(labels)
            for i in range(size):
                if(i==10):
                    break
                labels_limited[i] = labels[i]
            test = str(f)[len(path):]
            frames_predictions_dictionary[str(f)[len(path):]] = labels_limited
            print (labels_limited)




        print ("Process Finished")
        return frames_predictions_dictionary