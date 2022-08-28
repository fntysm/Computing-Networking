import cv2
import mediapipe as mp

class FaceAI():
    def __init__(self, mode=False, maxFace=2):
        self.mode = mode
        self.maxFace = maxFace
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.FaceMesh = self.mpFaceMesh.FaceMesh(self.mode, self.maxFace)

    def FaceMeshAI(self, record):
        D1Spec = self.mpDraw.DrawingSpec(thickness=1, color=(0, 255, 0))
        D2Spec = self.mpDraw.DrawingSpec(thickness=1, color=(255, 0, 0))
        results = self.FaceMesh.process(cv2.cvtColor(record, cv2.COLOR_BGR2RGB))
        if results.multi_face_landmarks:
            for face in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(record, face, self.mpFaceMesh.FACEMESH_TESSELATION, D1Spec, D2Spec)
def FaceMeshMain():
    cam = cv2.VideoCapture(0)
    Faces = FaceAI()
    while True:
        success, record = cam.read()
        Faces.FaceMeshAI(record)
        cv2.imshow("FACE MESH CAM", record)
        cv2.waitKey(1)

if __name__ == "__main__":
    FaceMeshMain()