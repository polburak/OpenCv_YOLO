import cv2

# Daha yaygın yüz algılayıcı dosya yolu
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
      #  frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        image_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        image_gray = cv2.equalizeHist(image_gray)

        faces = face_cascade.detectMultiScale(image_gray)

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
