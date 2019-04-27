import numpy as np
import cv2
import pickle


face_cascade = cv2.CascadeClassifier('C:\Py\data\haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")    

cap = cv2.VideoCapture(0)

labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}

while True:
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 3, minNeighbors = 5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color=(255,255,100)
            stroke=1
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        img_item="my-image1.jpg"
        cv2.imwrite(img_item,roi_gray)
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,225,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()