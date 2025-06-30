import cv2
import numpy as np
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")  
rows, cols = img.shape[:2]
pts_src = np.float32([[50, 50], [250, 50], [50, 200], [250, 200]])
pts_dst = np.float32([[60, 60], [240, 40], [70, 220], [230, 210]])
H, _ = cv2.findHomography(pts_src, pts_dst)
warped_img = cv2.warpPerspective(img, H, (cols, rows))
cv2.imshow('Homography Transform', warped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
