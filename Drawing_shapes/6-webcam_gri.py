import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    deger, kare = cap.read()
    gray = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    cv2.imshow("My Webcam", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'): # waitkey değeri '0' olursa tek görüntü verir.
        break

cap.release()
cv2.destroyAllWindows()