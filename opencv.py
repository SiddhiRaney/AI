import cv2

# Step 1: Read the original image
image = cv2.imread('example.jpg')
cv2.imshow('Image Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 2: Resize the image
resized_image = cv2.resize(image, (300, 200))  # width=300, height=200
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 3: Rotate the image 90 degrees clockwise
rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Convert to grayscale
gray_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 6: Perform Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)
cv2.imshow('Edge Detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Find contours from edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 8: Draw contours on a copy of the rotated image
contour_image = rotated_image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green contours

cv2.imshow('Contours on Image', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 9: Save the final image with contours
cv2.imwrite('output_with_contours.jpg', contour_image)
