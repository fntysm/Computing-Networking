import cv2
import mediapipe as mp
import time


class FaceAI():
    def __init__(self, minDetectConf=0.5, modelSelection=1):
        self.minDetectConf = minDetectConf
        self.modelSelection = modelSelection
        self.mpFaceDetection = mp.solutions.face_detection
        self.FaceDetector = self.mpFaceDetection.FaceDetection()
        self.mpDraw = mp.solutions.drawing_utils
    def faceDetection(self, record):
        results = self.FaceDetector.process(cv2.cvtColor(record, cv2.COLOR_BGR2RGB))
        if results.detections:
            for id, detection in results.detections:
                print(id, detection)
def FaceDet():
    cam = cv2.VideoCapture(0)
    previousTime = 0
    FaceD = FaceAI()
    while True:
        success, record = cam.read()
        FaceD.faceDetection(record)
        currentTime = time.time()
        fps = 1 / (currentTime-previousTime)
        previousTime = currentTime
        cv2.putText(record, f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
        cv2.imshow("WEBCAM IS OPEN", record)
        cv2.waitKey(1)

if __name__ == "__main__":
    FaceDet()