import cv2


def face_detection(img):

    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5)

    # Draw rectangles around the detected faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    max = 0
    for i in range(len(faces)):
        if faces[i][2] * faces[i][3] > max:
            max = faces[i][2] * faces[i][3]
            real_face = faces[i]

    x, y, w, h = real_face
    # cropped_img = gray[y:y+h, x:x+w]
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img
