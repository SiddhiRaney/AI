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

# Step 19: Edge Detection using Canny
edges = cv2.Canny(gray, 100, 200)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 20: Contour Detection
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = rotated_image.copy()
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 21: Hough Line Transform
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
line_img = rotated_image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
cv2.imshow('Hough Lines', line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 22: Hough Circle Transform
circle_img = rotated_image.copy()
circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
    param1=50, param2=30, minRadius=10, maxRadius=100
)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(circle_img, (x, y), r, (0, 255, 0), 2)
cv2.imshow('Hough Circles', circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 23: Gaussian Blur
blurred = cv2.GaussianBlur(rotated_image, (15, 15), 0)
cv2.imshow('Gaussian Blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 24: Edge-preserving Filter (for artistic effect)
edge_preserve = cv2.edgePreservingFilter(rotated_image, flags=1, sigma_s=60, sigma_r=0.4)
cv2.imshow('Edge Preserving Filter', edge_preserve)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 25: Cartoon Effect
gray_blur = cv2.medianBlur(gray, 5)
edges_cartoon = cv2.adaptiveThreshold(
    gray_blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 9, 9
)
color = cv2.bilateralFilter(rotated_image, d=9, sigmaColor=250, sigmaSpace=250)
cartoon = cv2.bitwise_and(color, color, mask=edges_cartoon)
cv2.imshow('Cartoon Effect', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 26: Face Detection (using Haar Cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_img = rotated_image.copy()
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (255, 0, 255), 2)
cv2.imshow('Face Detection', face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 27: Save cartoon version
cv2.imwrite('cartoon_image.jpg', cartoon)

