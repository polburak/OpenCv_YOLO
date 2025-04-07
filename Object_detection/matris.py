import numpy as np

# 3x3'lük örnek görüntü
goruntu = np.array([
                    [10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]
                    ])

# 3x3'lük kenar tespit filtresi
filtre = np.array([
                    [-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]
                    ])

# (10 * -1) + (20 * 0) + (30 * 1) = -10 + 0 + 30 = 20
# (40 * -1) + (50 * 0) + (60 * 1) = -40 + 0 + 60 = 20
# (70 * -1) + (80 * 0) + (90 * 1) = -70 + 0 + 90 = 20
# 20 + 20 + 20 = 60

# Görüntünün kenarlarını dikkate alınmaz.
# Çünkü konvolüsyon işlemi sadece iç bölgelerde yapılır.
# İlk satır ve ilk sütundaki pikseller işlenmez.


# Görüntü boyutları
yukseklik, genislik = goruntu.shape

# Filtre görüntü üzerinde kaydırarak uygulanır
sonuc = np.zeros_like(goruntu)

# Filtrenin görüntü üzerindeki her 3x3'lük alana kaydırılması
for i in range(1, yukseklik - 1):  # 1 ve yükseklik-1 arası, kenarlara yaklaşmamak için
    for j in range(1, genislik - 1):  # 1 ve genişlik-1 arası, kenarlara yaklaşmamak için
        # 3x3'lük bir alanı seçiyoruz
        bolge = goruntu[i - 1:i + 2, j - 1:j + 2]

        # Konvolüsyon işlemi: Filtre ile bölgeyi çarpıp toplama işlemi
        toplam = np.sum(bolge * filtre)

        # Sonuçta oluşan değeri yeni görüntüye atıyoruz
        sonuc[i, j] = toplam

# Sonuç görüntüsünü yazdırma
print("Sonuç Görüntüsü:")
print(sonuc)
