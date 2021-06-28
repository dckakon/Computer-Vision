import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap=cv2.VideoCapture(0)
cap.set(3,640)# 3- width
cap.set(4,480) #4 height

segmentor=SelfiSegmentation()
fps=cvzone.FPS()

while True:
    success, img=cap.read()
    imgOut=segmentor.removeBG(img,(0,255,0),threshold=0.6)

    #imgStacked=cvzone.stackImages([img,imgOut],2,1) # 2 column, scale 1

    #cv2.imshow("imgOut",imgStacked)
    cv2.imshow("imgOut", imgOut)
    cv2.waitKey(1)