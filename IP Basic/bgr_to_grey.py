import cv2
import numpy as np

img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\rgb2.jpg")

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)  # output in (resolution x,resolution y, number of channels)
print(img_grey.shape)  # output in (resolution x,resolution y, number of channels) here no channel will show for greyscale image

cv2.namedWindow("Grey Image", cv2.WINDOW_NORMAL)  # allow window resize
cv2.imshow("Grey Image",img_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()