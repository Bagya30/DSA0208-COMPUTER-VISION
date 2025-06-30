import cv2
import numpy as np
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")
rows, cols = img.shape[:2]
pts1 = np.float32([[50, 50], [250, 50], [50, 200], [250, 200]])
pts2 = np.float32([[30, 60], [270, 40], [50, 250], [250, 250]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))
cv2.imshow('Perspective Transform', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
