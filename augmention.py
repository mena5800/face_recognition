import imgaug.augmenters as iaa
from PIL import Image
import numpy as np
import os

def image_augmention(dir_path):
    # Load the image
    for filename in os.listdir(dir_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Read the image file
            try :
                img = Image.open(os.path.join(dir_path, filename))

                # Convert the Pillow image to a NumPy array
                img_array = np.asarray(img)

                # Define the augmentation pipeline
                aug_pipeline = iaa.Sequential([
                    iaa.Fliplr(p=0.5), # flip the image horizontally with a probability of 0.5
                    iaa.Flipud(p=0.5), # flip the image vertically with a probability of 0.5
                    iaa.Crop(percent=(0, 0.2)), # crop the image by a random amount between 0% and 20%
                    iaa.Affine(rotate=(-45, 45), shear=(-20, 20)), # rotate and shear the image by a random amount
                    iaa.GaussianBlur(sigma=(0, 3.0)), # apply Gaussian blur with a random standard deviation between 0 and 3.0
                    iaa.AddToHueAndSaturation((-20, 20)), # change the hue and saturation of the image by a random value between -20 and 20
                    iaa.Multiply((0.5, 1.5)), # multiply the pixel values of the image by a random value between 0.5 and 1.5
                    iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), # sharpen the image by a random amount
                ], random_order=True)

                # Apply the augmentation pipeline to the image array
                aug_img_array = aug_pipeline(image=img_array)

                # Convert the augmented image back to a Pillow image
                aug_img = Image.fromarray(aug_img_array)

                new_filename = os.path.splitext(filename)[0] + "_resized.jpg"
                # Save the augmented image
                aug_img.save(os.path.join(dir_path, new_filename))
            except:
                return -1


image_augmention("images/post_processing/mina")
image_augmention("images/post_processing/abram")
image_augmention("images/post_processing/mahmoud")
image_augmention("images/post_processing/mariam_h")
image_augmention("images/post_processing/mariam_m")