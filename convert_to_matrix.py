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

convert_to_mat("mina_george_pre_images",images,0)
convert_to_mat("mina_prepocessing_images",images,1)
convert_to_mat("abram_pre",images,2)



# Save the list to a file using pickle
with open("output_file.pkl", "wb") as f:
    pickle.dump(images, f)
