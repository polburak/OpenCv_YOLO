import cv2
import numpy as np

foto = cv2.imread("opencv.png",0) # fotoyu gri yapar.

cv2.imshow("Fotograf", foto)
cv2.imwrite("Opencv_Gri.png", foto)

