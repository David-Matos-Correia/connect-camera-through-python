from PIL import ImageGrab
import numpy as np 
import cv2
import time

cascade_rostos = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_olhos = cv2.CascadeClassifier('haarcascade_eye.xml' )

while True:
    tela = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
    tela_cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
    rostos = cascade_rostos.detectMultiScale(tela_cinza)

    for (x,y,h,w) in rostos:
        tela = cv2.rectangle(tela,(x,y),(x+h, y+w),(255,0,0),2)
        roi_cinza = tela_ciza[y:y+w, x:x+w]
        roi_colorido = tela[y:y+w, x:x+w]
        olhos = cascade_olhos.detectMultiScale(roi_cinza)

        for (ox,oy,oh,ow) in olhos:
            cv2.rectangle(roi_colorido,(ox,oy), (ox+ow,oy+oh),(0,0,255),2)

    cv2.imshow('tela',cv2.cvtColor(tela, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        break



