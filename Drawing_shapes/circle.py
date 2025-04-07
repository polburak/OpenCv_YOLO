import cv2

image_path = "dubai.jpg"
image = cv2.imread(image_path)
image_shape = image.shape

center_point =(int(image_shape[0] * 0.5), int(image_shape[1] * 0.5))
radius =200
cv2.circle(image, center_point, radius, (0, 255, 255), thickness=5)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()