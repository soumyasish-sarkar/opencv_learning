import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\grey.jpg")

#img_resize = cv2.resize(img,(1080,720))  # for making to required resolution

img_resize = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))   #here we are reducing resolution by half by dividing by 2 , cand be 1/3 if divided by 3

cv2.namedWindow("image", cv2.WINDOW_NORMAL)  # allow window resize
cv2.imshow("image", img_resize)  # here image is window name, can be anything
cv2.waitKey(0)  # 0 gives delays of infite, with out waitKey(0) image will appear for very minor time only
cv2.destroyAllWindows()