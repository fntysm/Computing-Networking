import mediapipe as mp
import cv2
import time
# the following couple lines of code is the setup of a webcam
cam = cv2.VideoCapture(0)
# standard mediapipe code to write
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils
previousTime = 0
while True:
    success, record = cam.read()
    # sending our RGB image to the "hands" object
    recordRGB = cv2.cvtColor(record, cv2.COLOR_BGR2RGB)
    # processing after converting the BGR image to RGB
    results = hands.process(recordRGB)
    # to check if something on camera is detected
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        # if we detected hand(s)
        for eachHand in results.multi_hand_landmarks:
            for id, lm in enumerate(eachHand.landmark):
                print(id, lm)
                height, width, channel = record.shape
                # to find the position
                cx, cy = int(lm.x*width), int(lm.y*height)
                cv2.putText(record, str(id+1),(cx,cy),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),2)
            mpDraw.draw_landmarks(record, eachHand, mp_hands.HAND_CONNECTIONS)
    currentTime = time.time()
    fps = 1 / (currentTime-previousTime)
    previousTime = currentTime
    cv2.putText(record, "Z's hand tracking",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),2)
    cv2.putText(record,str(int(fps)),(90,80),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,0,255),3)
    # the camera window
    cv2.imshow("camera currently displaying", record)
    # to maintain displaying before exit
    cv2.waitKey(1)
