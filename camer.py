import cv2, time
import numpy as np
from PIL import ImageGrab
import cv2


video=cv2.VideoCapture(0)

a=0

while True:
    a = a + 1

    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tela = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
    tela_cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
    rostos = cascade_rostos.detectMultiScale(tela_cinza)


    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)

cv2.waitKey(0)

video.release()

cv2.destroyAllWindows
