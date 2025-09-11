import cv2
import numpy as np

img1= cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\walking.jpg")
img2= cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\fighter_plane.jpg")

img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))


#merge image
img_merge= cv2.addWeighted(img1,1,img2,0.8,1)
img_subs= cv2.subtract(img1,img2) #remove common color


cv2.imshow("Merge Image",img_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()