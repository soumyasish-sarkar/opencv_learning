import cv2
import numpy as np

img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\tinkesh.jpg")

# Resize the image to 500x500
img = cv2.resize(img, (500, 500))
print("Resized image shape:", img.shape)

# Apply Canny edge detection
new_img = cv2.Canny(img, 50, 50) #less the threshold value more the edges
print("Canny image shape:", new_img.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Image", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
