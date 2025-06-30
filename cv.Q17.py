import cv2
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")            
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
