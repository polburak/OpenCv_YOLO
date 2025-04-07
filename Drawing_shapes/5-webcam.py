import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    deger, kare = cap.read()
    cv2.imshow("My Webcam", kare)

    if cv2.waitKey(1) & 0xFF == ord('q'): # waitkey değeri '0' olursa video oynamaz
        break

cap.release()
cv2.destroyAllWindows()