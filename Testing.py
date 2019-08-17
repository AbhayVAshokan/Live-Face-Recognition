import cv2
import numpy as np
from Generation import preprocess

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def test(model, names):
    cap = cv2.VideoCapture(0)

    while True:
        faces, coordinates = [], []
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = face_cascade.detectMultiScale(gray, 1.3, 5)

        for x, y, h, w in face_coordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (53, 26, 232), 2)
            print('If crashed values are: ', x, y, h, w, len(faces))
            faces.append(np.array(preprocess(gray[x:x+w, y:y+h])))
            coordinates.append((x, y, h, w))

        prediction = list(model.predict(np.array(faces)))

        for i in range(len(faces)):
            x, y, h, w = coordinates[i]
            cv2.putText(frame, names[list(prediction[0]).index(max(prediction[0]))] + ': ' + str(round(max(prediction[0]) * 100, 2)) + "%", (x, y - 10),cv2.FONT_HERSHEY_TRIPLEX, 0.75, (70, 26, 232), 2)

        cv2.imshow("Predictions", frame)
        if cv2.waitKey(1) in [13, 27]:
            cap.release()
            cv2.destroyAllWindows()
            break
