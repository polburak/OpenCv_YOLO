import cv2

image_path = "dubai.jpg"
image = cv2.imread(image_path)
#image = cv2.resize(image, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)


text = "Dubai / Burc Halife "
position = (400,50)
color = (0, 0, 255)
font_size = 1
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX

# Resim üzerine text yazdırma
cv2.putText(image, text, position, font, font_size, color, thickness)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()