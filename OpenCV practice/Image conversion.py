import cv2
import numpy as np

img=cv2.imread("resource/lena.png")
kernel=np.ones((5,5),np.uint8)  #.uint8-unsigned integer - value (0-255)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR to Gray scale
imgBlur= cv2.GaussianBlur(imgGray,(55,55),0) #Blur image,it has to be odd number
imgCanny= cv2.Canny(img,150,200) #canny image
imgDialation =cv2.dilate(imgCanny,kernel,iterations=1)  #edge thinkness for canny iage
imgEroded= cv2.erode(imgDialation,kernel, iterations=1) #opposite of erode

#cv2.imshow("Gray image",imgGray)
#cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)