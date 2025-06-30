import cv2
import numpy as np
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")                    
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  
sobelxy = np.sqrt(sobelx**2 + sobely**2)           
cv2.imshow('Sobel XY', sobelxy / sobelxy.max())    
cv2.waitKey(0)
cv2.destroyAllWindows()
