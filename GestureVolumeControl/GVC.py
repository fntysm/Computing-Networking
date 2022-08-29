import cv2
import numpy as np
import math
import HandTracker
import time

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
cam = cv2.VideoCapture(0)
Hands = HandTracker.HandAI(detectConf=0.75)
previousTime = 0
vol = 0
volPer = 0
volBar = 400
while True:
    success, record = cam.read()
    # getting the landmarks list to identify the thumb and the index (the fingers needed in this operation)
    record, lmList = Hands.detectHands(record)
    if len(lmList) != 0:
        # cv2.circle(cam, dimensions, radius, color, cv2.FILLED)
        thumb = lmList[4][1]
        index = lmList[8][1]
        w, h, c = record.shape
        xt, yt = int(thumb.x*w), int(thumb.y*h)
        xi, yi = int(index.x*w), int(index.y*h)
        cx, cy = (xt+xi)//2, (yt+yi)//2
        # the thumb
        cv2.circle(record, (xt, yt), 15, (255, 0, 0), cv2.FILLED)
        # the index
        cv2.circle(record, (xi, yi), 15, (255, 0, 0), cv2.FILLED)
        # the center
        cv2.circle(record, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
        cv2.line(record, (xt, yt), (xi, yi), (255,0,0), 3)
        length = math.hypot(xi-xt,yi-yt)
        # to convert the hand length to the volume range
        vol = np.interp(length,[50,300],[minVol,maxVol])
        volBar = np.interp(length, [50,300], [400, 150])
        volPer = np.interp(length, [50,300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

    cv2.rectangle(record, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(record, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(record, f'{int(volPer)}%', (90, 150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0), 3)
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(record, f'FPS: {int(fps)}', (90, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 0), 3)
    # the camera window
    cv2.imshow("camera currently displaying", record)
    # to maintain displaying before exit
    cv2.waitKey(1)


