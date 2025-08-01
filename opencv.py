import cv2

image = cv2.imread('example.jpg')
cv2.imshow('Image Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing image
import cv2

image = cv2.imread('example.jpg')
resized_image = cv2.resize(image, (300, 200))  # width=300, height=200

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
