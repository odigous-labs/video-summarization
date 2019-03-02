'''
Within this script, focus to identify the existing objects in a given set of frames.
Output is a dictionary, key represet the frame name and the value is the predcitions list.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
If need to run this script seperately, then can edit the relevant input file path.

If need to use this script within another code then can import the script and call the functions with relevant arguments.
'''

import numpy as np
from keras.preprocessing import image
from keras.applications import resnet50
import os

def generate_object_list_of_frames(input_frames_path,img_width, img_height):

    images = []                       # List to keep scaled frame data
    frame_names = []                  # List to keep names of frames

    # Load Keras' ResNet50 model that was pre-trained against the ImageNet database
    model = resnet50.ResNet50()

    frames_list = os.listdir(input_frames_path)
    frames_list.sort(key=lambda x: int(x[5:-4]))

    for image_name in frames_list:
        frame_names.append(image_name)
        img = image.load_img(input_frames_path+image_name, target_size=(img_width, img_height))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        images.append(img)

    images = np.vstack(images)
    images = resnet50.preprocess_input(images)
    predictions = model.predict(images)
    predicted_classes = resnet50.decode_predictions(predictions, top=10)

    index = 0
    frames_predictions_dictionary = {}
    for i in predicted_classes:
        object_list = []
        for imagenet_id, name, likelihood in i:
            #print(" - {}: {:2f} likelihood".format(name, likelihood))
            #if(likelihood>20):
            object_list.append(name)

        frames_predictions_dictionary[frame_names[index]] = object_list
        index += 1

    return frames_predictions_dictionary

def run():
    # image folder
    input_frames_path = "./data/generated_frames/"

    # dimensions of images
    img_width, img_height = 224, 224

    generate_object_list_of_frames(input_frames_path,img_width, img_height )

if __name__ == "__main__":
    run()