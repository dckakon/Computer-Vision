import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3- width
cap.set(4, 480)  # 4 height
cap.set(cv2.CAP_PROP_FPS,60) #to increase fps

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

imBG=cv2.imread("images/bg01.jpg")

listImg=os.listdir("images")
print(listImg)
imgList=[]

for imgPath in listImg:
    img=cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg=0

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.4)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)  # 2 column, scale 1
    _,imgStacked=fpsReader.update(imgStacked)

    cv2.imshow("imgOut", imgStacked)

    key = cv2.waitKey(1)
    if key == ord('a'):
        indexImg=0
    elif key == ord('d'):
        indexImg=1
    elif key == ord('q'):
        break
