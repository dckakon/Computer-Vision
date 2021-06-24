import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands = mp.solutions.hands  # formal key
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,
                                        self.detectionCon,self.trackCon)  # object
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self,img, handNo=0, draw= True ):
        lmList=[]

        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                #print(id, cx, cy)
                lmList.append([id,cx,cy])
                #if id==4:
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)


        return lmList



def main():
    prev_frame_time = 0
    new_frame_time = 0
    camera = cv2.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img = camera.read()
        img= detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])

        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time

        cv2.putText(img, "fps="+str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

        cv2.imshow("Image", img) #640 by 480 image
        cv2.waitKey(1)

if __name__=="__main__":
    main()