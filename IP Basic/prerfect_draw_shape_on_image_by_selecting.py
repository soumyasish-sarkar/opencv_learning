#select on image, to draw different shapes

import cv2
import numpy as np
flag=0
pt1x=0
pt1y=0


#defining draw function
def draw(event,x,y,flags,param):
    #pass #nothing will hapeen
    #print("Mouse triggered") #moving cursor or click on image gives output "mouse triggered in terminal
    #print(event) #according to different click of left click right click, scroll, moving cursor , different digit genrated, here 1 for left click is considering
    if(event == 1):
        global flag,pt1x,pt1y,img_copy
        #print("Mouse Left clicked")
        flag=1;
        pt1x=x;
        pt1y=y;


    elif(event == 0):
         #print("Cursor moved")
         if(flag==1):
            img_copy = img.copy()
            cv2.rectangle(img_copy, pt1=(pt1x,pt1y), pt2=(x, y), color=(0, 0, 255),thickness=2)  # thickness=-1 for fill the image
            cv2.imshow("window", img_copy)


    elif(event == 4):
        #print("Left click released")
        flag = 0
        cv2.rectangle(img, pt1=(pt1x, pt1y), pt2=(x, y), color=(0, 0, 255),thickness=2)  # thickness=-1 for fill the image
        cv2.imshow("window", img)


#naming window globally
cv2.namedWindow(winname="window")


img_ip = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\fighter_plane.jpg")
img = cv2.resize(img_ip,(640,480))  # for making to required resolution
img_copy=img.copy()
img_stored=img.copy()

cv2.imshow("window",img)
while True:

    #cv2.imshow("window",img)
    cv2.setMouseCallback("window", draw)

    key = cv2.waitKey(1) & 0xFF
    if (key == ord("q")):
        break
    elif(key == ord("r")):
        img = img_stored.copy()
        img_copy = img.copy()
        cv2.imshow("window", img)

cv2.destroyAllWindows()