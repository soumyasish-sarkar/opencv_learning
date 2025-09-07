import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\rgb2.jpg")

#in image (0,0) start from top left imagine as a matrix position

crop_img = img[500:1000,1000:1500]  #same as doing slicing in numpy array

cv2.imshow("image", crop_img)  # here image is window name, can be anything

cv2.waitKey(0)  # 0 gives delays of infite, with out waitKey(0) image will appear for very minor time only

