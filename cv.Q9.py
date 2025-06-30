import cv2

img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")                       
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('Clockwise', clockwise)
cv2.imshow('Counter Clockwise', counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
