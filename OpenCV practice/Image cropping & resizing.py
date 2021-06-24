import cv2
import numpy as np

img= cv2.imread("resource/lambo.jpg")
print(img.shape) #height,width, BGR

imgResize=cv2.resize(img,(1000, 500))
print(imgResize.shape)


imgCropped= img[0:200,200:500] #matrix[ height, width], not opencv function

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)
