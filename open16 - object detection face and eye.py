import numpy as np
import cv2, time
import cv2
import np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

video=cv2.VideoCapture(0)

a=0

while True:
    a = a + 1

    check, frame = video.read()

    print(check)
    print(frame)

    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    faces = (face_cascade.detectMultiScale(gray, 1.3, 5))

    key=cv2.waitKey(1)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff

    if key == 27:
        break


    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)


        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,255,0),2)


print(a)


cv2.waitKey(0)

video.release()

cv2.destroyAllWindows
