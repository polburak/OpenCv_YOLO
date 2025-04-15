import numpy as np

# 9x9'luk giriş görüntüsü
input_image = np.array([
    [10, 20, 30, 40, 50, 60, 70, 80, 90],
    [100, 110, 120, 130, 140, 150, 160, 170, 180],
    [190, 200, 210, 220, 230, 240, 250, 260, 270],
    [280, 290, 300, 310, 320, 330, 340, 350, 360],
    [370, 380, 390, 400, 410, 420, 430, 440, 450],
    [460, 470, 480, 490, 500, 510, 520, 530, 540],
    [550, 560, 570, 580, 590, 600, 610, 620, 630],
    [640, 650, 660, 670, 680, 690, 700, 710, 720],
    [730, 740, 750, 760, 770, 780, 790, 800, 810]
], dtype=np.float32)

# 3x3 kenar tespit filtresi
kernel = np.array([
    [2, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])


# Konvolüsyon işlemi
def convolve2d(image, kernel):
    output_image = np.zeros((image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[1] + 1))

    for i in range(output_image.shape[0]):
        for j in range(output_image.shape[1]):
            # 3x3'lük bölgeyi al
            region = image[i:i + kernel.shape[0], j:j + kernel.shape[1]]
            # Konvolüsyon işlemi: bölgedeki elemanlarla filtreyi çarpıp topla
            output_image[i, j] = np.sum(region * kernel)

    return output_image


# Sonuç görüntüsünü al
output_image = convolve2d(input_image, kernel)

# Giriş ve çıkış görüntüsünü yazdır
print("Giriş Görüntüsü (9x9):")
print(input_image)
print("\nÇıkış Görüntüsü (Konvolüsyon Sonucu):")
print(output_image)
