import cv2
import numpy as np
import time #required to control fps of video, which by default playing quickly


cap = cv2.VideoCapture('output.mp4') #by defaulf system webcam have code 0



while True:
    ret, frame = cap.read()

    #print(ret) # print True for successfully read, False if no such webcam deceted
    vid_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    time.sleep(1/20) #now will play in 1/20 fps

    cv2.imshow("webcam",frame)  #ret wont display, it just popup an window, # frame is an numpy array
    cv2.imshow("webcam_grey",vid_grey) #for convert to grey scale


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
