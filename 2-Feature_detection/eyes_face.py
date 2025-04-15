import cv2

# Yüz ve göz cascade dosyalarını yüklüyoruz
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Gri tonlamaya çevir ve histogram eşitlemesi yap
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Yüzleri algıla
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Yüzü dikdörtgenle çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Yüz bölgesini gri görüntüden al
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Gözleri sadece yüz içinde ara
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)

            for (ex, ey, ew, eh) in eyes:
                eye_center = (ex + ew // 2, ey + eh // 2)
                cv2.ellipse(roi_color, eye_center, (ew // 2, eh // 2), 0, 0, 360, (255, 0, 255), 2)

        # Son görüntüyü göster
        cv2.imshow("Face and Eye Detection", frame)

        # 'q' tuşu ile çıkış
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Kamerayı ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
