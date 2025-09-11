import cv2
import numpy as np

org_v = cv2.VideoCapture(r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\lecture.mp4")
sub_m = cv2.createBackgroundSubtractorMOG2()
while True:
    r, frame = org_v.read()
    if r == True:
        frame = cv2.resize(frame, (700, 500))
        sub_v = sub_m.apply(frame)
        cv2.imshow("background_substructed", sub_v)
        cv2.imshow("original", frame)
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break

org_v.release()
cv2.destroyAllWindows()