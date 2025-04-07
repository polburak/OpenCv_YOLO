import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("opencv.png",0)
plt.imshow(foto, cmap="gray", interpolation="bicubic")
plt.show()