import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\rgb3.jpg")

#flip_image = cv2.flip(img,0) #flip upside down/ vertically

#flip_image = cv2.flip(img,1) # flip in horizontal axis

flip_image = cv2.flip(img,-1)  #flip vertically and horizontally simultaneously

cv2.namedWindow("image", cv2.WINDOW_NORMAL)  # allow window resize
cv2.imshow("image", flip_image)  # here image is window name, can be anything
cv2.waitKey(0)  # 0 gives delays of infite, with out waitKey(0) image will appear for very minor time only

