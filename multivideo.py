import cv2
import numpy as np
capture= cv2.VideoCapture(1)
capture1= cv2.VideoCapture(-2)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, frame1= capture.read()
    height = frame1.shape[0]
    width = frame1.shape[1]
    frame1 = cv2.resize(frame1 , (int(width*0.5), int(height*0.5)))
    ret, frame2= capture1.read()
    height = frame2.shape[0]
    width = frame2.shape[1]
    frame2 = cv2.resize(frame2 , (int(width*0.5), int(height*0.5)))
    cv2.imshow("frame1",frame1)
    cv2.imshow("frame2",frame2)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
capture.release()
capture1.release()
cv2.destroyAllWindows()
