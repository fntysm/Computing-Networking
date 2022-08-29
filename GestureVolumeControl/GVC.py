import cv2
import numpy as np
import HandTracker
import time

cam = cv2.VideoCapture(0)
Hands = HandTracker.HandAI(detectConf=0.75)
previousTime = 0
while True:
    success, record = cam.read()
    # getting the landmarks list to identify the thumb and the index (the fingers needed in this operation)
    record, lmList = Hands.detectHands(record)
    if len(lmList) != 0:
        # cv2.circle(cam, dimensions, radius, color, cv2.FILLED)
        xt, yt = lmList[4][1].x, lmList[4][1].y
        xi, yi = lmList[8][1].x, lmList[8][1].y
        p1 = tuple((xt, yt))
        p2 = tuple((xi, yi))
        cv2.circle(record, (xt, yt), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(record, (xi, yi), 15, (255, 0, 0), cv2.FILLED)
        cv2.line(record, p1, p2, (255,0,0), 3)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(record, str(int(fps)), (90, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0), 3)
    # the camera window
    cv2.imshow("camera currently displaying", record)
    # to maintain displaying before exit
    cv2.waitKey(1)


