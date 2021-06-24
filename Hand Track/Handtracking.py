import cv2
import mediapipe as mp
import time

camera=cv2.VideoCapture(0)

mpHands=mp.solutions.hands #formal key
hands=mpHands.Hands()  #object

mpDraw=mp.solutions.drawing_utils

prev_frame_time = 0

new_frame_time = 0

while True:
    success,img=camera.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                height,width,channel=img.shape
                cx,cy=int(lm.x*width),int(lm.y*height)
                print(id, cx,cy)
                #if id==4:

                cv2.circle(img,(cx,cy),7,(255,0,255),cv2.FILLED)


            mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)

    new_frame_time = time.time()


    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    cv2.putText(img,str(int(fps)),(18,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
    #cv2.destroyAllWindows()
