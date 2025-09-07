import cv2
import numpy as np

img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\rgb2.jpg")

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Grey Image", cv2.WINDOW_NORMAL)  # allow window resize
cv2.imshow("Grey Image",img_grey)

#saving an image
#cv2.imwrite("img_grey.png",img_grey)

# Save image to specific location
save_path = r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\img_grey.png"
cv2.imwrite(save_path, img_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()