import math

#Gauss hesaplaması için fonksiyon tanımla.
def gaussian(x, y, sigma):

  # Formulün payda kısmı hesaplanıyor.
  payda = 2 * math.pi * (sigma ** 2)
  # Formulün e üzeri kısmı hesaplanıyor.
  us_ifadesi = -((x ** 2 + y ** 2) / (2 * (sigma ** 2)))
  #Eğer payda 0 çıkarsa hatayı engellemek için.
  if payda == 0:
      return 0
  #Formülün sonucunu döndürür.
  return (1 / payda) * math.exp(us_ifadesi)

# Tanımladığımız çarpım matrisi
matris_veri =           [(-1, -1), (0, -1), (1, -1),
                        (-1,  0), (0,  0), (1,  0),
                        (-1,  1), (0,  1), (1,  1)]

# Matris şeklinde ekrana yazdırma
print("\n1. Adımda Tanımlanan Matris")
for i in range(0, len(matris_veri), 3):
    print([matris_veri[i], matris_veri[i+1], matris_veri[i+2]])

# Tanımladığımız sigma değeri
sigma = 1
# Çarpım değerlerini tutmak için tanımlanan dizi.
gauss_agirliklari = []

# For döngüsü kullanarak matris değerleri hesaplanır.
print("\n2. Adımda Kernel Elemanlarının Hesaplanma Aşaması:")
for x, y in matris_veri:
  agirlik = gaussian(x, y, sigma)
  gauss_agirliklari.append(agirlik)
  print(f"->({x}, {y}) için Gauss ağırlığı: {agirlik:.3f}")

# Hesaplanan veriler matrise dönüştürülerek yerlerine yazılır.
gauss_matrisi = [gauss_agirliklari[i:i + 3] for i in range(0, len(gauss_agirliklari), 3)]

# Yazılan veriler virgünden sonra 3 basamak olacak şekilde ekrana yazdırılır.
print("\n3. Adımda Hesaplanan Matris Değerleri")
for row in gauss_matrisi:
  print([f"{val:.3f}" for val in row])

# Normalize işlemi için matris değerlerini topla.
toplam_agirlik = sum(sum(row) for row in gauss_matrisi)

# Toplama işlemi için değerlerin yan yana gösterme
matris_yazdir = " + ".join(f"{eleman:.3f}" for row in gauss_matrisi for eleman in row)
print(f"\n4. Adımda Toplam Ağırlık: {matris_yazdir} = {toplam_agirlik:.3f}")


normalize_gauss_matrisi = [[agirlik / toplam_agirlik for agirlik in row] for row in gauss_matrisi]
normalize_gauss_matrisi = []

# Normalize işlemini ekrana yazdırma
print("\n5.Adımda Normalize İşleminin Hesaplanma Aşaması:")
for row in gauss_matrisi:
    normalize_row = []
    for agirlik in row:
        normalize_agirlik = agirlik / toplam_agirlik
        normalize_row.append(normalize_agirlik)
        print(f"->{agirlik:.3f} / {toplam_agirlik:.3f} = {normalize_agirlik:.3f}")
    normalize_gauss_matrisi.append(normalize_row)

print("\n6. Adımda Sonuçların Matrise İşlenmesi:")
for row in normalize_gauss_matrisi:
  print([f"{val:.3f}" for val in row])

# Piksel matrisini belirleme ve ekrana yazdırma.
piksel_matrisi = [
    [52, 55, 61],
    [54, 60, 65],
    [58, 62, 70]]

print("\n7. Adımda Tanımlanan Piksel Matris")
for row in piksel_matrisi:
    print(row)

# Piksel ve Matris Değerlerinin İşlem İle Hesaplanması.
carpim_matrisi = [[0.0 for _ in range(len(piksel_matrisi[0]))] for _ in range(len(piksel_matrisi))]

print("\n8. Adımda Yeni Değerleri Hesaplama İşlemi:")
for i in range(len(piksel_matrisi)):
    for j in range(len(piksel_matrisi[0])):
        carpim_matrisi[i][j] = piksel_matrisi[i][j] * normalize_gauss_matrisi[i][j]
        print(f"->{piksel_matrisi[i][j]} * {normalize_gauss_matrisi[i][j]:.3f} = {carpim_matrisi[i][j]:.3f}")

# Tüm Çarpım Değerlerinin Toplanması İşlemi
toplam_carpim = sum(sum(row) for row in carpim_matrisi)
toplama_yazdir = " + ".join(f"{eleman:.3f}" for row in carpim_matrisi for eleman in row)
print(f"\n9. Adımda Filtre Değeleri Toplamı: {toplama_yazdir} = {toplam_carpim:.3f}")