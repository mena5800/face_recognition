import cv2
import os
import numpy as np
import pickle


def convert_to_mat(dir_path,images,label):
    # Loop through all the image files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Read the image file
            img = cv2.imread(os.path.join(dir_path, filename),cv2.IMREAD_GRAYSCALE)
            img = img.flatten()

            images[0].append(img)
            images[1].append(label)





images = [[],[]]

convert_to_mat("images/pre_processing/mina",images,0)
convert_to_mat("images/pre_processing/abram",images,1)
convert_to_mat("images/pre_processing/mahmoud",images,2)
convert_to_mat("images/pre_processing/mariam_h",images,3)
convert_to_mat("images/pre_processing/mariam_m",images,4)

images.append({0:"mina",1:"abram",2:"mahmoud",3:"mariam hossam",4:"mariam mohamed"})



# Save the list to a file using pickle
with open("dataset.pkl", "wb") as f:
    pickle.dump(images, f)
