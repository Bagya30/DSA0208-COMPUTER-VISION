import numpy as np
import cv2
src = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float32)
dst = np.array([[0, 0], [1.2, 0.1], [1.1, 1.1], [-0.1, 1.0]], dtype=np.float32)
A = []
for (x, y), (u, v) in zip(src, dst):
    A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
    A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])
A = np.array(A)
_, _, V = np.linalg.svd(A)
H = V[-1].reshape(3, 3) 
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")
h, w = img.shape[:2]
warped = cv2.warpPerspective(img, H, (w, h))
cv2.imshow('DLT Transform', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
