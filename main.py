import cv2
import numpy as np


image = cv2.imread('rover.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([170,0,0])
upper = np.array([180,255,255])

detect = cv2.inRange(hsv, lower, upper)

contours,_ = cv2.findContours(detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for contour in contours:
    if cv2.contourArea(contour) > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

        print("X : ", x)
        print("Y : ", y)

        M = cv2.moments(contour)
        print(M)
        if(M['m00'] != 0):
            c_x = int(M['m10'] / M['m00'])
            c_y = int(M['m01'] / M['m00'])

            cv2.circle(image, (c_x, c_y), 2, (255, 255,0), -1)

cv2.imshow("image", image)
cv2.imshow("detect", detect)

cv2.waitKey(0)

cv2.destroyAllWindows()