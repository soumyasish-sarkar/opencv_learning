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
        global flag,pt1x,pt1y
        #print("Mouse Left clicked")
        flag=1;
        pt1x=x;
        pt1y=y;


    elif(event == 0):
        #print("Cursor moved")
        if(flag==1):
            cv2.rectangle(img, pt1=(pt1x,pt1y), pt2=(x, y), color=(0, 0, 255),thickness=1)  # thickness=-1 for fill the image

    elif(event == 4):
        #print("Mouse Scrolled")
        flag = 0




#naming window globally
cv2.namedWindow(winname="window")


#img=np.zeros((512,512,3)) #creating image for background of resolution 512x512, with black in color
img_ip = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\walking.jpg")
img = cv2.resize(img_ip,(640,480))  # for making to required resolution


while True:

    cv2.imshow("window",img)
    cv2.setMouseCallback("window", draw)
    #print(pt1x,pt1y)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()