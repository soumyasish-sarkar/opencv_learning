import cv2
import numpy as np

# Create white background
pure_bw_img_created = np.ones((512,512,3), dtype=np.uint8) * 255

# House base (rectangle)
cv2.rectangle(pure_bw_img_created, pt1=(170,250), pt2=(330,400), color=(0,0,0), thickness=-1)

# Roof (triangle)
roof_points = np.array([[150,250],[250,150],[350,250]], np.int32)
roof_points = roof_points.reshape((-1,1,2))
cv2.fillPoly(pure_bw_img_created, [roof_points], color=(0,0,0))

# Door
cv2.rectangle(pure_bw_img_created, pt1=(230,290), pt2=(270,395), color=(255,255,255), thickness=-1)

# Windows
cv2.rectangle(pure_bw_img_created, pt1=(180,290), pt2=(220,330), color=(255,255,255), thickness=-1)
cv2.rectangle(pure_bw_img_created, pt1=(280,290), pt2=(320,330), color=(255,255,255), thickness=-1)

# Sun (circle)
cv2.circle(pure_bw_img_created, center=(470,40), radius=30, color=(0,0,0), thickness=-1)


# Text
cv2.putText(pure_bw_img_created, text="Black & White House", org=(140,480),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(0,0,0), thickness=2)

# Save image
save_path = r"C:\Users\soumyasish-sarkar\PycharmProjects\opencv_learning\image\bw_house.png"
cv2.imwrite(save_path, pure_bw_img_created)

# Show image
cv2.imshow("image", pure_bw_img_created)
cv2.waitKey(0)
cv2.destroyAllWindows()
