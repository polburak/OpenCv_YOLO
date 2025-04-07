import cv2

image_path = "dubai.jpg"
image = cv2.imread(image_path)
image_shape = image.shape

point1 =(int(image_shape[0] * 0.1), int(image_shape[1] * 0.1))
point2 =(int(image_shape[0] * 0.6), int(image_shape[1] * 0.6))
cv2.line(image,point1,point2,(0,0,255), thickness=2)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()