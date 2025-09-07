import cv2
import numpy as np

pure_bw_img_created=np.ones((512,512,3), dtype=np.uint8) * 255  #creating image for background of resolution 512x512, with black in color

#Rectrangle
cv2.rectangle(pure_bw_img_created,pt1=(200,150),pt2=(300,250),color=(0,0,0),thickness=-1) #thickness=-1 for fill the image

#circle
cv2.circle(pure_bw_img_created,center=(250,110),radius=40,color=(0,0,0),thickness=2)


#line
cv2.line(pure_bw_img_created,pt1=(200,250),pt2=(190,400),thickness=2,color=(0,0,0))
cv2.line(pure_bw_img_created,pt1=(300,250),pt2=(310,400),thickness=2,color=(0,0,0))
cv2.line(pure_bw_img_created,pt1=(230,400),pt2=(250,300),thickness=2,color=(0,0,0))
cv2.line(pure_bw_img_created,pt1=(270,400),pt2=(250,300),thickness=2,color=(0,0,0))
cv2.line(pure_bw_img_created,pt1=(190,400),pt2=(230,400),thickness=2,color=(0,0,0))
cv2.line(pure_bw_img_created,pt1=(270,400),pt2=(310,400),thickness=2,color=(0,0,0))






#test
cv2.putText(pure_bw_img_created,text="Pure Black and White",org=(130,40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0),thickness=2)


save_path = r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\pure_bw_img_created.png"
cv2.imwrite(save_path, pure_bw_img_created)

cv2.imshow("image",pure_bw_img_created)
cv2.waitKey(0)