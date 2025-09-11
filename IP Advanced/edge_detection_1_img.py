import cv2
import numpy as np

img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\road1.jpg")
img=cv2.resize(img,(400,400))

cv2.imshow("image",img)

#Canny Edge detection Without applying GaussianBlur without greyscale convert
canny=cv2.Canny(img,50,150)
cv2.imshow("Canny ED - without Gaussian Blur, without Greyscale convert",canny)

img_g = cv2.GaussianBlur(img, (5,5), 0)
canny_g=cv2.Canny(img_g,50,150)
cv2.imshow("Canny ED - with Gaussian Blur, without Greyscale convert",canny_g)

#Canny Edge detection Without applying GaussianBlur with greyscale convert
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(img,50,150)
cv2.imshow("Canny ED - without Gaussian Blur",canny)

img_g = cv2.GaussianBlur(img, (5,5), 0)
canny_g=cv2.Canny(img_g,50,150)
cv2.imshow("Canny ED - with Gaussian Blur",canny_g)

print(img.shape)
print(canny.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()