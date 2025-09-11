import cv2
import numpy as np


img1 = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\pure_bw_img_created.png")
img2 = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\bw_house.png")

img1 = cv2.resize(img1,(300,300))
img2 = cv2.resize(img2,(300,300))

new1 = cv2.bitwise_and(img1,img2)
new2 = cv2.bitwise_or(img1,img2)
new3 = cv2.bitwise_xor(img1,img2)
new4 = cv2.bitwise_not(img1)
new5 = cv2.bitwise_not(img2)

#h = np.hstack((img1,img2,new1,new2,new3,new4,new5)) ##methods to show multiple images together in the sccreen

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("bitwise_and",new1)
cv2.imshow("bitwise_or",new2)
cv2.imshow("bitwise_xor",new3)
cv2.imshow("bitwise_not_image_1",new4)
cv2.imshow("bitwise_not_image_2",new5)

cv2.waitKey(0)
cv2.destroyAllWindows()
