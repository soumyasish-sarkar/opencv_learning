import cv2
import numpy as np

img_create=np.zeros((512,512,3)) #creating image for background of resolution 512x512, with black in color

#Rectrangle
cv2.rectangle(img_create,pt1=(150,100),pt2=(350,300),color=(255,0,0),thickness=2) #thickness=-1 for fill the image

#circle
cv2.circle(img_create,center=(250,200),radius=50,color=(0,255,0),thickness=2)

#line
cv2.line(img_create,pt1=(150,400),pt2=(350,400),thickness=2,color=(0,0,255))

#test
cv2.putText(img_create,text="Shape and Text",org=(150,90),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,255,255),thickness=2)


save_path = r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\img_create.png"
cv2.imwrite(save_path, img_create)

cv2.imshow("image",img_create)
cv2.waitKey(0)