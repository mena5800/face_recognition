import cv2


def predict_image(img, model, pca, names):
    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



    # Resize the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5)

    max = 0
    for i in range(len(faces)):
        if faces[i][2] * faces[i][3] > max:
            max = faces[i][2] * faces[i][3]
            real_face = faces[i]

    x, y, w, h = real_face
    cropped_img = gray[y:y+h, x:x+w]

    cropped_img = cv2.resize(cropped_img, (62, 47))
    flatten_img = cropped_img.flatten().reshape(1, -1)
    flatten_img = pca.transform(flatten_img)
    result = model.predict(flatten_img)

    return names[int(result)]
