import cv2
import numpy as np

foto = cv2.imread("dubai.jpg",0) # fotoyu gri yapar.
#foto = cv2.imread("dubai.jpg") # fotoyu orijinal gösterir.


cv2.imshow("Fotograf", foto)
cv2.waitKey(0)
cv2.destroyAllWindows()
