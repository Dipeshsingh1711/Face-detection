import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('c:/py/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
img_counter = 0
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  
    cv2.imshow('video',frame)
    k = cv2.waitKey(30) & 0xff
    
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
cap.release()
cv2.destroyAllWindows()