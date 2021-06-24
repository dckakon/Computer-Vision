import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8) #gray scale
print(img.shape)

#img[200:300,100:300]=255,0,0# to color a particular section
#img[:]=255,0,0 # to color the whole image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #img,(starting point),(last point),(color),thikness(not important)
cv2.rectangle(img,(0,0),(250,250),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),2) #img,center point, radius, color

cv2.putText(img,"OpenCV",(300,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)


cv2.waitKey(0)