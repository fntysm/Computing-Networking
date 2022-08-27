import cv2
import mediapipe as mp


class PoseAI:
    def __init__(self, mode=False, upper=False, smooth=True, detectConf=0.5, trackConf=0.5):
        self.mode = mode
        self.upper = upper
        self.smooth = smooth
        self.detectConf = detectConf
        self.trackConf = trackConf
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpDraw = mp.solutions.drawing_utils

    def captureBody(self, webcam):
        # sending our RGB image to the "pose" object
        recordRGB = cv2.cvtColor(webcam, cv2.COLOR_BGR2RGB)
        # processing after converting the BGR image to RGB
        results = self.pose.process(recordRGB)
        if results.pose_landmarks:
            # if we detected a body
            for id, lm in enumerate(results.pose_landmarks.landmark):
                print(id, lm)
                height, width, channel = webcam.shape
                # to find the position
                cx, cy = int(lm.x * width), int(lm.y * height)
                cv2.putText(webcam, str(id + 1), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
            self.mpDraw.draw_landmarks(webcam, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)


def PoseEstimation():
    cam = cv2.VideoCapture(0)
    bodyExist = PoseAI()
    while True:
        success, webcam = cam.read()
        bodyExist.captureBody(webcam)
        cv2.imshow("WEBCAM IS OPEN", webcam)
        cv2.waitKey(1)
