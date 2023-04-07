import cv2
import face_recognition
import face_recognition_models
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("/home/buddy/PycharmProjects/faceR/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facer-e4a8c-default-rtdb.firebaseio.com/",
    'storageBucket' : "facer-e4a8c.appspot.com"
})

# Import img
folderPath = '/home/buddy/PycharmProjects/faceR/Images'
pathList = os.listdir(folderPath)

#print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    #print(path)
    #print(os.path.splitext(path)[0])
#print(imgList)
#print(len(imgList))
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encode = encodings[0]
            encodeList.append(encode)
            print(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
#encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds]

print("Encoding Complete!!!")

#print(encodeListKnown)

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
