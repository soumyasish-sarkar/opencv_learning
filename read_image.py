import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\grey.jpg")
print(type(img))
print(img)
print(img.shape)  # output in (resolution x,resolution y, number of channels)

cv2.imshow("image", img)  # here image is window name, can be anything
cv2.waitKey(0)  # 0 gives delays of infite, with out waitKey(0) image will appear for very minor time only
