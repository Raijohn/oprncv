import cv2,os,time
import numpy as np

All_faces = "faces"

name_labels = {}
images = []
id = 0
labels = []
width = 100
height = 130

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
video = cv2.VideoCapture(0)

classifire = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

h = 0
while True:
    succes,frame = video.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = classifire.detectMultiScale(frame_gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        currentFrame = frame_gray[y:y+h,x:x+w]
        finallFrame = cv2.resize(currentFrame,(width,height))
        prediction,confidence = model.predict(finallFrame)
        cv2.putText(frame,str(name_labels[prediction])+","+str(round(confidence))+"%",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),1)
    cv2.imshow("fram",frame)
    Key = cv2.waitKey(10)
    if Key == 27:
        break
