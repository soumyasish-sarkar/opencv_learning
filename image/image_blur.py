import cv2
import numpy as np

img = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\soumyasish.jpg")
img=cv2.resize(img,(380,380))

gaussian = cv2.GaussianBlur(img,(9,9),0)
median = cv2.medianBlur(img,5)
bilatery = cv2.bilateralFilter(img,9,75,75)


#cv2.imshow("gaussian blur",gaussian)
#cv2.imshow("img",img)

h =np.hstack((img,gaussian,median,bilatery))
cv2.imshow("origina -> gaussian -> median -> bilatery",h)
cv2.waitKey(0)
cv2.destroyAllWindows()

