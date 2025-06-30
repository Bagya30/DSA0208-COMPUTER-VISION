import cv2
import numpy as np

img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")  # Replace with your image path
rows, cols = img.shape[:2]

# Define 3 points from the original image and their new positions
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[60, 70], [210, 60], [70, 220]])

# Get affine matrix and apply it
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Affine Transform', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
