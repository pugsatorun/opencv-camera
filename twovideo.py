import cv2

captures = []
i = 0

capture = cv2.VideoCapture(-1)
ret, frame = capture.read()
captures.append( capture )
capture = cv2.VideoCapture(-3)
ret, frame = capture.read()
captures.append( capture )

while(True):
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):
        break

    for capture in enumerate( captures ):
        ret, frame = capture.read()
        cv2.imshow( 'frame' + str(i), frame )
        i += 1

capture.release()
cv2.destroyAllWindows()
