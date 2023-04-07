import os
import pickle
import numpy as np
import cv2
import cvzone
import face_recognition
#firebase data storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

#setup firebase>>
cred = credentials.Certificate("/home/buddy/PycharmProjects/faceR/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facer-e4a8c-default-rtdb.firebaseio.com/",
    'storageBucket' : "facer-e4a8c.appspot.com"
})
#firbase<<

#camera >>linux(0)|index cam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(3, 480)

imgBackground = cv2.imread("/home/buddy/PycharmProjects/faceR/Resources/background.jpg")

folderModePath = '/home/buddy/PycharmProjects/faceR/Resources/Modes'
ModePathList = os.listdir(folderModePath)
imgModeList = []
print(ModePathList)
for path in ModePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#load and encode data
print("Loading Encode File...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

print(studentIds)
print("Encode File Load...")
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print("matches", matches)
        #print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        #print("Match Index",matchIndex)


        if matches[matchIndex]:
            print("Face detected in database")
            print(studentIds[matchIndex])
            #y1, x2, y2, x1 = faceLoc
            #y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            #bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            #imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)


    imgBackground[320:320 + 480, 190:190 + 640] = img                       #->camera
    #imgBackground[420:420 + 450, 220:220 + 600] = imgModeList[0]           ->line 73,73++

    imgModeListResized = cv2.resize(imgModeList[1], (600, 450))             #->modes
    imgBackground[320:320 + 450, 600:600 + 600] = imgModeListResized


    #cv2.imshow("Webcam", img)  #cam
    cv2.imshow("FACE ATTENDANCE", imgBackground)
    cv2.waitKey(1)

