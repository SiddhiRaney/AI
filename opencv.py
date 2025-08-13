# Step 10: Apply binary thresholding
_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 11: Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)
cv2.imshow('Adaptive Threshold', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 12: Morphological operations (Erosion & Dilation)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
eroded = cv2.erode(binary_image, kernel, iterations=1)
cv2.imshow('Eroded Image', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilated = cv2.dilate(binary_image, kernel, iterations=1)
cv2.imshow('Dilated Image', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 13: Histogram Equalization for better contrast
equalized_image = cv2.equalizeHist(gray)
cv2.imshow('Histogram Equalized', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 14: Convert to HSV color space
hsv_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 15: Mask a color range (e.g., green)
lower_green = (40, 40, 40)
upper_green = (70, 255, 255)
mask = cv2.inRange(hsv_image, lower_green, upper_green)
cv2.imshow('Green Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 16: Draw a polygon
polygon_image = rotated_image.copy()
points = [(100, 50), (200, 80), (250, 200), (120, 250)]
pts = np.array(points, np.int32).reshape((-1, 1, 2))
cv2.polylines(polygon_image, [pts], isClosed=True, color=(255, 255, 0), thickness=2)
cv2.imshow('Polygon Drawn', polygon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 17: Blend two images
# For blending, resize another image to match the rotated image
overlay_image = cv2.imread('example2.jpg')
overlay_resized = cv2.resize(overlay_image, (rotated_image.shape[1], rotated_image.shape[0]))
blended_image = cv2.addWeighted(rotated_image, 0.7, overlay_resized, 0.3, 0)
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 18: Save the final blended image
cv2.imwrite('final_blended_image.jpg', blended_image)
