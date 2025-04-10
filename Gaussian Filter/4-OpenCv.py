import cv2
import numpy as np

image = cv2.imread("gorsel.png", cv2.IMREAD_GRAYSCALE)
sigma = 1  #
bulanik_gorsel = cv2.GaussianBlur(image, (3, 3), sigma)

yan_yana = np.hstack((image, bulanik_gorsel))

cv2.imshow("Orijinal ve Gaussian Bulanık Görsel", yan_yana)
cv2.waitKey(0)
cv2.destroyAllWindows()