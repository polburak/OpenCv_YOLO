import cv2

# Göz algılama için Haar cascade dosyasını yüklüyoruz
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Gri tonlamaya çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Gözleri algıla
        eyes = eye_cascade.detectMultiScale(gray)

        # Her göz için elips çiz
        for (x, y, w, h) in eyes:
            center = (x + w // 2, y + h // 2)
            cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 2)

        # Görüntüyü göster
        cv2.imshow("Eye Detection", frame)

        # q tuşuna basıldığında çık
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
