import mediapipe as mp
import cv2
import time

class HandAI:
    def __init__(self, mode=False, maxHands=2, detectConf=0.5, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectConf = detectConf
        self.trackConf = trackConf
        # standard mediapipe code to write
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def detectHands(self, record):
        # sending our RGB image to the "hands" object
        recordRGB = cv2.cvtColor(record, cv2.COLOR_BGR2RGB)
        # processing after converting the BGR image to RGB
        self.results = self.hands.process(recordRGB)
        # to check if something on camera is detected
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            # if we detected hand(s)
            for eachHand in self.results.multi_hand_landmarks:
                for id, lm in enumerate(eachHand.landmark):
                    print(id, lm)
                    height, width, channel = record.shape
                    # to find the position
                    cx, cy = int(lm.x * width), int(lm.y * height)
                    cv2.putText(record, str(id + 1), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,128), 2)
                self.mpDraw.draw_landmarks(record, eachHand, self.mp_hands.HAND_CONNECTIONS)
        return record
def HandMain():
    cam = cv2.VideoCapture(0)
    Hands = HandAI()
    previousTime = 0
    while True:
        success, record = cam.read()
        record = Hands.detectHands(record)
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime
        cv2.putText(record, str(int(fps)), (90, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255), 3)
        # the camera window
        cv2.imshow("camera currently displaying", record)
        # to maintain displaying before exit
        cv2.waitKey(1)

if __name__ == "__main__":
    HandMain()