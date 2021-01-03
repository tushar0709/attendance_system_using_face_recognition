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

print("Loading.......")

def name_sheet():
    session = "unknown.csv"

    now = datetime.now()
    hour = now.strftime('%H:%M')

    if hour >= '9' and hour <= '11':
        session = "session_1.csv"
        return session

    if hour >= '11:15' and hour <= '12:15':
        session = "session_2.csv"
        return session

    if hour >= '12:15' and hour <= '15:15':
        session = "session_3.csv"
        return session
    return session
    # print(session1, session2, session3)




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
    # csvstr = strToday + '.csv'




    dir = "C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/session/"
    date_dir = "C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/session/" + strToday
    if not os.path.exists(dir):
        os.mkdir(dir)

    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    open(os.path.join(date_dir, name_sheet()), "a+")



    with open(os.path.join(date_dir, name_sheet()), "r+",newline= '') as f:
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

        if name[2:] not in nameList:

            session = " "

            now = datetime.now()
            hour = now.strftime('%H:%M')

            if hour >= '9' and hour <= '11':
                session = "session 1"


            if hour >= '11:15' and hour <= '12:15':
                session = "session 2"


            if hour >= '12:15' and hour <= '15:15':
                session = "session 3"



            roll = name.split('-')
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            date = now.strftime('%d-%m-%y')
            f.writelines({f'\n{name[2:]},{roll[0]},{dtstring},{date},{session}'})

        if name[2:] in nameList:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (255,0,0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, 'DETECTED', (x1 + 4, y2 - 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)





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
            cv2.putText(img, name[2:], (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

        if not matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,0, 255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    cv2.imshow('webcam', img)
    cv2.waitKey(1)
