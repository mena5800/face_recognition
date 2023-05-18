import pickle
from flask import Flask, render_template, request
import io
from PIL import Image
from face_detection import face_detection
import numpy as np
from face_recognition import predict_image
from pca import PCA
from sklearn.svm import SVC
import cv2


app = Flask(__name__, static_url_path='/static')


# Load the saved model from the file
with open('./last_model.pkl', 'rb') as f:
    pca, clf, names = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/transform', methods=['POST'])
def transform():
    # Get the uploaded image
    
    image_file = request.files['image-file']
    print(image_file)
    # # Load the image using PIL
    # image = Image.open(image_file)
    # # convert the pil object to numpy array
    # image = np.array(image)
    # Read the contents of the FileStorage object into a NumPy array
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)

    # Decode the image data using cv2.imdecode()
    image = cv2.imdecode(file_bytes, cv2.COLOR_BGR2RGB)


    prediction = predict_image(image, clf, pca, names)




    # Load the image using PIL
    image = Image.open(image_file)
    # convert the pil object to numpy array
    image = np.array(image)
    # use face_detection function to return image with face detection
    image = face_detection(image)
    # convert the image to pil object
    image = Image.fromarray(image)

    # Convert the output image to JPEG format
    output_buffer = io.BytesIO()
    image.save(output_buffer, format='JPEG')

    # Return the output image
    return output_buffer.getvalue(), prediction


if __name__ == '__main__':
    app.run(debug=True)
