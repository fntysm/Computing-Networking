import cv2
import mediapipe as mp
import time

WHITE_COLOR = (224, 224, 224)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 128, 0)
BLUE_COLOR = (255, 0, 0)

class FaceAI():
    def __init__(self, minDetectConf=0.5, modelSelection=1):
        self.minDetectConf = minDetectConf
        self.modelSelection = modelSelection
        self.mpFaceDetection = mp.solutions.face_detection
        self.FaceDetector = self.mpFaceDetection.FaceDetection()
        self.mpDraw = mp.solutions.drawing_utils
    def faceDetection(self, record):
        results = self.FaceDetector.process(cv2.cvtColor(record, cv2.COLOR_BGR2RGB))
        circleDrawingSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))
        lineDrawingSpec = self.mpDraw.DrawingSpec(thickness=1, color=(0, 255, 0))
        if results.detections:
            for id, detection in enumerate(results.detections):
                # drawing by ourselves
                # self.mpDraw.draw_detection(record, detection, circleDrawingSpec, lineDrawingSpec)
                x = detection.location_data.relative_bounding_box.xmin
                y = detection.location_data.relative_bounding_box.ymin
                width = detection.location_data.relative_bounding_box.width
                height = detection.location_data.relative_bounding_box.height
                w, h, c = record.shape
                # defining the bounding box
                bbox = int(x*w),int(y*h),int(width*w),int(height*h)
                cv2.rectangle(record, bbox, GREEN_COLOR,2)
                cv2.putText(record, f'{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,
                            3, (0, 255, 0), 2)
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