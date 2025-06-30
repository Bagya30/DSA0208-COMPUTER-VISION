import cv2
img = cv2.imread("C:\Users\BAGYA LAKSHMI\OneDrive\Desktop\open cv programs\sample.jpeg")  
edges = cv2.Canny(img, 100, 200)  
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
