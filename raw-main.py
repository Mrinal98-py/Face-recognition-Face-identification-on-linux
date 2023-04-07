import os
import cv2
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
while True:
    success, img = cap.read()
    imgBackground[320:320 + 480, 100:100 + 640] = img       #cam pos
    #imgBackground[420:420 + 450, 220:220 + 600] = imgModeList[0]

    imgModeListResized = cv2.resize(imgModeList[1], (600, 450)) #modes
    imgBackground[320:320 + 450, 599:599 + 600] = imgModeListResized


    #cv2.imshow("Webcam", img)  #cam
    cv2.imshow("FACE ATTENDANCE", imgBackground)
    cv2.waitKey(1)

