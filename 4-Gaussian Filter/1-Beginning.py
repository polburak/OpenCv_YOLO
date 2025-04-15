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

# Tanımladığımız sigma değeri
sigma = 1
# Çarpım değerlerini tutmak için tanımlanan dizi.
gauss_agirliklari = []

# For döngüsü kullanarak matris değerleri hesaplanır.
for x, y in matris_veri:
  agirlik = gaussian(x, y, sigma)
  gauss_agirliklari.append(agirlik)

# Hesaplanan veriler matrise dönüştürülerek yerlerine yazılır.
gauss_matrisi = [gauss_agirliklari[i:i + 3] for i in range(0, len(gauss_agirliklari), 3)]

# Yazılan veriler virgünden sonra 3 basamak olacak şekilde ekrana yazdırılır.
print("\n3. Adımda Hesaplanan Matris")
for row in gauss_matrisi:
  print([f"{val:.3f}" for val in row])