import cv2
import numpy as np


cap = cv2.VideoCapture(0) #by defaulf system webcam have code 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))


while True:
    ret, frame = cap.read()
    out.write(frame)

    #print(ret) # print True for successfully read, False if no such webcam deceted
    vid_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow("webcam",frame)  #ret wont display, it just popup an window, # frame is an numpy array
    cv2.imshow("webcam_grey",vid_grey) #for convert to grey scale


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()
