#click on image, to draw different shapes

import cv2
import numpy as np

#defining draw function
def draw(event,x,y,flags,param):
    #pass #nothing will hapeen
    #print("Mouse triggered") #moving cursor or click on image gives output "mouse triggered in terminal
    #print(event) #according to different click of left click right click, scroll, moving cursor , different digit genrated, here 1 for left click is considering
    if(event == 1):
        #print("Mouse Left clicked")
        cv2.circle(img, center=(x, y), radius=30, color=(0, 255, 255), thickness=2)
        # cv2.ellipse(img, (x - 30, y), (50, 20), 0, 0, 360, (0, 255, 255), 2)

    elif(event == 2):
        #print("Mouse Right clicked")
        cv2.rectangle(img, pt1=(x-30,y-30), pt2=(x+30, y+30), color=(0, 0, 255),thickness=2)  # thickness=-1 for fill the image


    elif(event == 10):
        #print("Mouse Scrolled")
        cv2.circle(img, center=(x, y), radius=30, color=(255, 0, 255), thickness=-1)


#naming window globally
cv2.namedWindow(winname="window")


#img=np.zeros((512,512,3)) #creating image for background of resolution 512x512, with black in color
img_ip = cv2.imread(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\cherry_blossom.jpg")
img = cv2.resize(img_ip,(640,480))  # for making to required resolution


while True:

    cv2.imshow("window",img)
    cv2.setMouseCallback("window", draw)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()