import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime

import pandas as pd

df = pd.read_csv("Attendance.csv")
df.to_excel("Attendance.xlsx", index=False)
# Load images
path = "images"
images = []
classNames = []

myList = os.listdir(path)

for cl in myList:
    img = cv2.imread(f"{path}/{cl}")
    if img is not None:
        images.append(img)
        classNames.append(os.path.splitext(cl)[0])

print("Known Faces:", classNames)


# Encode faces
def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodes = face_recognition.face_encodings(img)

        if len(encodes) > 0:
            encodeList.append(encodes[0])

    return encodeList


# Mark attendance
def markAttendance(name):
    with open("Attendance.csv", "a+") as f:
        f.seek(0)
        data = f.readlines()

        nameList = []

        for line in data:
            entry = line.split(",")
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            timeString = now.strftime("%H:%M:%S")
            dateString = now.strftime("%Y-%m-%d")

            f.write(f"\n{name},{dateString},{timeString}")


print("Encoding faces...")
encodeListKnown = findEncodings(images)
print("Encoding Complete")


# Start webcam
cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()

    if not success:
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(
        imgS,
        facesCurFrame
    )

    for encodeFace, faceLoc in zip(
        encodesCurFrame,
        facesCurFrame
    ):

        matches = face_recognition.compare_faces(
            encodeListKnown,
            encodeFace
        )

        faceDis = face_recognition.face_distance(
            encodeListKnown,
            encodeFace
        )

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc

            y1 *= 4
            x2 *= 4
            y2 *= 4
            x1 *= 4

            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.rectangle(
                img,
                (x1, y2 - 35),
                (x2, y2),
                (0, 255, 0),
                cv2.FILLED
            )

            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2
            )

            markAttendance(name)

    cv2.imshow("Face Recognition Attendance", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()