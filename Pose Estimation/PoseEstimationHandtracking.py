import cv2
import mediapipe as mp #framework for pose estimation
import time

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()

mpHands=mp.solutions.hands #formal key
hands=mpHands.Hands()  #object

cap=cv2.VideoCapture("PoseVideos/Penalty01.mp4")
pTime=0
while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    Presults = pose.process(imgRGB)
    Hresults = hands.process(imgRGB)
    #print(results.pose_landmarks)

    if Presults.pose_landmarks:
        mpDraw.draw_landmarks(img,Presults.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(Presults.pose_landmarks.landmark):
            h, w, c =img.shape
            print(id, lm)
            cx,cy= int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx,cy),5 , (255,0,0),cv2.FILLED)

    if Hresults.multi_hand_landmarks:
        for handLms in Hresults.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                print(id, cx, cy)
                # if id==4:

                cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

