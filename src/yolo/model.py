import os
import matplotlib.pyplot as plt
import cv2
import natsort
import numpy as np
from tqdm import tqdm
from centroid_tracker.centroidtracker import CentroidTracker

from net.netarch import YoloArchitecture, YoloInferenceModel


class YOLO(object):

    def __init__(self):
        self.debug_timings = True
        self.yolo_arch = YoloArchitecture()
        self.model = self.yolo_arch.get_model()
        self.inf_model = YoloInferenceModel(self.model)
        self.ct = CentroidTracker()

    def predict(self, path_to_frames):

        dictionary_per_shot = []

        # checking whether the given path is a directory
        if os.path.isdir(path_to_frames):
            shots = os.listdir(path_to_frames)
            shots = natsort.natsorted(shots, reverse=False)

            for j in shots:
                shot_num = os.path.join(path_to_frames, j)

                fnames = [os.path.join(shot_num, f) for f in os.listdir(shot_num)
                          if os.path.isfile(os.path.join(shot_num, f))]

                fnames = natsort.natsorted(fnames)

                frames_predictions_dictionary = {}

                for f in tqdm(fnames, desc='Processing Batch'):
                    image = cv2.imread(f)

                    rects = []
                    centroids = []

                    frame = image.copy()

                    boxes, labels = self.inf_model.predict(image.copy())

                    frames_predictions_dictionary[str(f)[(len(path_to_frames)+len(j)+1):]] = []

                    image_h, image_w, _ = frame.shape

                    for i in range(len(boxes)):
                        xmin = int(boxes[i][0] * image_w)
                        ymin = int(boxes[i][1] * image_h)
                        xmax = int(boxes[i][2] * image_w)
                        ymax = int(boxes[i][3] * image_h)

                        temp = np.array([xmin, ymin, xmax, ymax])

                        rects.append(temp.astype("int"))

                        centroids.append([int((xmin + xmax) / 2), int((ymin + ymax) / 2)])

                    # update our centroid tracker using the computed set of bounding
                    # box rectangles
                    objects = self.ct.update(rects)

                    # loop over the tracked objects
                    for (objectID, centroid) in objects.items():
                        # draw both the ID of the object and the centroid of the
                        # object on the output frame
                        centroid_co = [centroid[0], centroid[1]]

                        if centroid_co in centroids:
                            i = centroids.index(centroid_co)
                            text = "{} - ID {}".format(labels[i], objectID)
                            frames_predictions_dictionary[str(f)[(len(path_to_frames)+len(j)+1):]].append(text)

                dictionary_per_shot.append(frames_predictions_dictionary)

        print("\nObject Identification Process Finished\n")
        return dictionary_per_shot
