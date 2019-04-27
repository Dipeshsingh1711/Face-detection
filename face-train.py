import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath('C:\Py\images'))
image_dir = os.path.join(BASE_DIR,"images")

face_cascade = cv2.CascadeClassifier('C:\Py\data\haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
current_id=0
label_ids={}
y_labels = []
x_train = []
#--------------------------------------------------------------------------------------
 #importing google_images_download module 
"""from google_images_download import google_images_download 

 #creating object 
response = google_images_download.googleimagesdownload() 
queries =['sidhu moose wala' ] 
for query in queries: 
    arguments = {"keywords": query,"format": "jpg","limit":90,"print_urls":True, "size": "medium","aspect_ratio": "panoramic","output_directory":'C:\Py\images'} 
    paths = response.download(arguments) """
#----------------------------------------------------------------------------------------
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ","_").lower()
            print(label,path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image,"uint8")
            print(image_array)
            
            faces = face_cascade.detectMultiScale(image_array,scaleFactor = 1.5,minNeighbors = 5)
            
            for (x,y,w,h) in faces:
                print(x,y,w,h)
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
                
with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")