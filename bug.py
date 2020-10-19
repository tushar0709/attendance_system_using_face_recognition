import cv2
import numpy as np
import face_recognition
import os
import os.path
import io
import csv
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)


for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)


def findEncodings(image):
    encodeList = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):

    today = datetime.today()
    strToday = today.strftime('%y-%m-%d')
    csvstr = strToday + '.csv'


    dir = r"C:\Users\DELL\PycharmProjects\Mini_project_SDL\attendance_sheet"
    if not os.path.exists(dir):
        os.mkdir(dir)
    open(os.path.join(dir, csvstr), "a+")
    


    with open(os.path.join(dir, csvstr), "r+",newline= '') as f:
        csvfile = io.StringIO()
        data = f.readlines()


        # for a in csvfile.getvalue():
        #     f.writelines(a)

        myDataList = csv.reader(f)

        nameList = []

        print(myDataList)
        for line in data:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines({f'\n{name},{dtstring}'})





    # today = datetime.today()
    # strToday = today.strftime('%y-%m-%d')
    # csvstr = strToday + '.csv'
    #
    # csvFileName  = os.path.join(pth,csvstr)
    # print(csvFileName)
    #
    #
    #
    # with open(csvFileName, 'r+') as f:
    #     myDataList = f.readlines()
    #     nameList = []
    #
    #     # print(myDataList)
    #     for line in myDataList:
    #         entry = line.split(',')
    #         nameList.append(entry[0])
    #
    #     if name not in nameList:
    #         now = datetime.now()
    #         dtstring = now.strftime('%H:%M:%S')
    #         f.writelines(f'\n{name},{dtstring}')


encodeListKnown = findEncodings(images)
print('encoding completed')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodeCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    cv2.imshow('webcam', img)
    cv2.waitKey(1)
