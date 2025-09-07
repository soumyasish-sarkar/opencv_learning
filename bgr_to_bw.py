import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\rgb4.jpg")

# convert to grayscale first
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold to make it pure black & white
_, img_bw = cv2.threshold(img_grey, 127, 255, cv2.THRESH_BINARY)

print(img_bw.shape)  # still (height, width), only black & white

# display
cv2.namedWindow("Black & White Image", cv2.WINDOW_NORMAL)
cv2.imshow("Black & White Image", img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
