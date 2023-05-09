import os
import cv2


def preimage(dir_path, dir_path_save):

    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Set the new width and height
    new_width = 500
    new_height = 500

    # Loop through all the image files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Read the image file
            img = cv2.imread(os.path.join(dir_path, filename))

            # Resize the image
            resized_img = cv2.resize(img, (new_width, new_height))
            gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cropped_img = gray[y:y+h, x:x+w]

            try:
                cropped_img = cv2.resize(cropped_img, (50, 37))
                # Save the resized image with a new filename
                new_filename = os.path.splitext(filename)[0] + "_resized.jpg"
                cv2.imwrite(os.path.join(dir_path_save, new_filename), cropped_img)
            except:
                pass




preimage("images/post_processing/abram", "images/pre_processing/abram")
preimage("images/post_processing/mahmoud", "images/pre_processing/mahmoud")
preimage("images/post_processing/mariam_m", "images/pre_processing/mariam_m")
preimage("images/post_processing/mina", "images/pre_processing/mina")
preimage("images/post_processing/mariam_h", "images/pre_processing/mariam_h")
