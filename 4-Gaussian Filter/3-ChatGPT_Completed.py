import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import convolve2d  # Gaussian çekirdeği ile konvolüsyon için

def gaussian(x, y, sigma):
    payda = 2 * math.pi * (sigma ** 2)
    us_ifadesi = -((x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    return (1 / payda) * math.exp(us_ifadesi) if payda != 0 else 0

matris_veri = [(-1, -1), (0, -1), (1, -1),
               (-1,  0), (0,  0), (1,  0),
               (-1,  1), (0,  1), (1,  1)]

sigma = 1
gauss_agirliklari = [gaussian(x, y, sigma) for x, y in matris_veri]
gauss_matrisi = [gauss_agirliklari[i:i + 3] for i in range(0, 9, 3)]

toplam_agirlik = sum(sum(row) for row in gauss_matrisi)
normalize_gauss_matrisi = [[val / toplam_agirlik for val in row] for row in gauss_matrisi]

image = Image.open("gorsel.png").convert("L")
image_array = np.array(image)

bulanik_gorsel = convolve2d(image_array, normalize_gauss_matrisi, mode='same', boundary='symm')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Orijinal Görsel")
plt.imshow(image_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Gaussian ile Bulanık Görsel")
plt.imshow(bulanik_gorsel, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
