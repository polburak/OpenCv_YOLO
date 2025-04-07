import cv2
import numpy as np

foto = cv2.imread("opencv.png",0) # fotoyu gri yapar.
cv2.imshow("Fotograf", foto)
klavye = cv2.waitKey(0)
if klavye == 27:  #27 hexedecimal'de ESC tuşunun karşılığı
    cv2.destroyAllWindows()
elif klavye == ord('s'):
    cv2.imwrite("Opencv_s_tus.png", foto)

