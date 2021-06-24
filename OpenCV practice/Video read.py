import cv2

cap=cv2.VideoCapture("resource/01.mp4")

while True:
    success, img=cap.read()  # image , success yes/not
    cv2.imshow("Video",img)

    if cv2.waitKey(100) & 0xFF==ord("q"):
        break