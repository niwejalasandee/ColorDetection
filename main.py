import cv2

from PIL import Image

from util import get_limits

yellow=[0, 255, 255] 

cap= cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() #ret=tells whether frame is successfully captured
                            #frame=actual image captured by frame
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask= cv2.inRange(hsvImage, lowerLimit, upperLimit) #to get color range for 1 color

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame= cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 5)

    print(bbox)

    cv2.imshow('frame', frame) #imshow=image show,display image in window

    if cv2.waitKey(1) & 0xFF == ord('q'): #if presses q key,do something
        break

cap.release() #release camera

cv2.destroyAllWindows() #close all