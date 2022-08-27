import mediapipe as mp
import cv2
import time
# the following couple lines of code is the setup of a webcam
cam = cv2.VideoCapture(0)
# standard mediapipe code to write
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils
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
            mpDraw.draw_landmarks(record, eachHand, mp_hands.HAND_CONNECTIONS)
    # the camera window
    cv2.imshow("camera currently displaying", record)
    # to maintain displaying before exit
    cv2.waitKey(1)
