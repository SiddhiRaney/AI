import cv2
import numpy as np

# ==========================
# Step 1: Read an image
# ==========================
image = cv2.imread('example.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 3: Resize image
resized_image = cv2.resize(image, (400, 300))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Rotate image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Flip image
flipped = cv2.flip(image, 1)
cv2.imshow('Flipped Image', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 6: Draw a line
line_img = image.copy()
cv2.line(line_img, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.imshow('Line Drawn', line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Draw a rectangle
rect_img = image.copy()
cv2.rectangle(rect_img, (100, 100), (300, 300), (0, 255, 0), 2)
cv2.imshow('Rectangle Drawn', rect_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 8: Draw a circle
circle_img = image.copy()
cv2.circle(circle_img, (250, 250), 80, (0, 0, 255), 3)
cv2.imshow('Circle Drawn', circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 9: Put text on image
text_img = image.copy()
cv2.putText(text_img, 'OpenCV Demo', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('Text Image', text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

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

# Step 13: Histogram Equalization
equalized_image = cv2.equalizeHist(gray)
cv2.imshow('Histogram Equalized', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 14: Convert to HSV color space
hsv_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 15: Mask a color range (Green)
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
overlay_image = cv2.imread('example2.jpg')
overlay_resized = cv2.resize(overlay_image, (rotated_image.shape[1], rotated_image.shape[0]))
blended_image = cv2.addWeighted(rotated_image, 0.7, overlay_resized, 0.3, 0)
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 18: Save blended image
cv2.imwrite('final_blended_image.jpg', blended_image)

# Step 19: Edge Detection (Canny)
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

# Step 24: Edge-preserving Filter
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

# Step 26: Face Detection (Haar Cascades)
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

# Step 28: Object Detection with DNN (MobileNet-SSD)
net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt.txt",
    "res10_300x300_ssd_iter_140000_fp16.caffemodel"
)
(h, w) = rotated_image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(rotated_image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
net.setInput(blob)
detections = net.forward()
dnn_img = rotated_image.copy()
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        cv2.rectangle(dnn_img, (startX, startY), (endX, endY), (0, 255, 255), 2)
cv2.imshow("DNN Object Detection", dnn_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 29: Feature Matching (ORB)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(rotated_image, None)
kp2, des2 = orb.detectAndCompute(overlay_resized, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
match_img = cv2.drawMatches(rotated_image, kp1, overlay_resized, kp2, matches[:20], None, flags=2)
cv2.imshow("Feature Matching", match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 30: Video Capture and Live Processing
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges_live = cv2.Canny(gray_frame, 100, 200)
    cv2.imshow("Live Edges", edges_live)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
