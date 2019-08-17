import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def generate(N):
    status = 0
    faces = []
    cap = cv2.VideoCapture(0)
    counter = 0

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, h, w in face_coordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 61, 214), 2)

            if status == 1:
                faces.append(preprocess(gray[x:x+w, y:y+h]))
                counter += 1

        if status == 1:
            cv2.putText(frame, 'RECORDING', (445, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 220, 0))
        if status == 0:
            cv2.putText(frame, 'PAUSED', (485, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (60, 11, 221))
            cv2.putText(frame, 'PRESS SPACEBAR TO START RECORDING', (35, 470), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 255))

        cv2.putText(frame, str(counter) + '/' + str(N), (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0))
        cv2.imshow("Face Detected", frame)

        key = cv2.waitKey(1)
        if key == 32:
            status = 0 if status == 1 else 1

        elif key in [13, 27] or counter == N:
            cap.release()
            cv2.destroyAllWindows()
            return faces


def preprocess(image):
    image = cv2.GaussianBlur(image, (3, 3), 0)
    image = cv2.resize(image, (64, 64), cv2.INTER_AREA)
    image = image / 255
    return list(image)
