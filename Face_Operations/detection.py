# KAYIT EDİLEN YÜZLERİ TESPİT ETME
import face_recognition
import cv2
import os
import pickle
import numpy as np

# Kayıtlı yüzlerin bulunduğu klasör
KAYITLI_YUZLERIN_OLDUGU_KLASOR = "kaydedilen_yuzler"

# Kayıtlı yüz verilerini yükleme
kayitli_yuzlerin_isim_listesi = []
kayitli_yuzlerin_paket_listesi = []

for dosya in os.listdir(KAYITLI_YUZLERIN_OLDUGU_KLASOR):
    if dosya.endswith(".pk1"):  # NOT: Dosya uzantıları ".pk1" olmalı
        sadece_dosya_ismi = os.path.splitext(dosya)[0]
        with open(os.path.join(KAYITLI_YUZLERIN_OLDUGU_KLASOR, dosya), "rb") as d:
            yuz_paketi = pickle.load(d)
            # Yüz paketi listesi içinde liste olabilir (çoklu yüz kodlandıysa)
            if isinstance(yuz_paketi, list):
                kayitli_yuzlerin_paket_listesi.extend(yuz_paketi)
                kayitli_yuzlerin_isim_listesi.extend([sadece_dosya_ismi] * len(yuz_paketi))
            else:
                kayitli_yuzlerin_paket_listesi.append(yuz_paketi)
                kayitli_yuzlerin_isim_listesi.append(sadece_dosya_ismi)

# Kamera başlatılıyor
kayit = cv2.VideoCapture(0)

while True:
    durum, kare = kayit.read()

    if durum:
        yuz_konumlari = face_recognition.face_locations(kare)
        yuz_paketleri = face_recognition.face_encodings(kare, yuz_konumlari)

        for (ust, sag, alt, sol), yuz_paketi in zip(yuz_konumlari, yuz_paketleri):

            tespit_edilen_yuz_etiketi = "Bilinmeyen"

            if kayitli_yuzlerin_paket_listesi:
                # Yüz karşılaştırması
                eslesmeler = face_recognition.compare_faces(kayitli_yuzlerin_paket_listesi, yuz_paketi)
                yuz_mesafesi = face_recognition.face_distance(kayitli_yuzlerin_paket_listesi, yuz_paketi)

                en_yakin_indeks = np.argmin(yuz_mesafesi)

                if eslesmeler[en_yakin_indeks]:
                    tespit_edilen_yuz_etiketi = kayitli_yuzlerin_isim_listesi[en_yakin_indeks]

            # Yüz etiketleme ve dikdörtgen çizme
            cv2.rectangle(kare, (sol, ust), (sag, alt), (0, 255, 0), 3)
            cv2.putText(kare, tespit_edilen_yuz_etiketi, (sol, ust - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Ekrana göster
        cv2.imshow("Taninan yuzleri tespit etme", kare)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Çıkış yapılıyor..")
            break

# Kaynakları serbest bırak
kayit.release()
cv2.destroyAllWindows()
