import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

prev_frame_time = 0
new_frame_time = 0
camera = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = camera.read()
    img = detector.findHands(img) #draw=False
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    cv2.putText(img, "fps=" + str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow("Image", img)  # 640 by 480 image
    cv2.waitKey(1)