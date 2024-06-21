import cv2,os,time
import numpy as np

All_faces = "faces"

name_labels = {}
images = []
id = 0
labels = []

for root,sub_folders,files in os.walk(All_faces):
    for sub_folder in sub_folders:
        name_labels[id]=sub_folder
        path = os.path.join(All_faces,sub_folder)
        for file in os.listdir(path):
            image_path = os.path.join(path,file)
            images.append(cv2.imread(image_path,cv2.IMREAD_GRAYSCALE))
            labels.append(id)
    id = id + 1
        
print(name_labels) 
print(images)
print(labels)  
images = np.array(images)
labels = np.array(labels)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)