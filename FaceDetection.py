import os,cv2

mainfolder = "faces"
subfolder = "ray"

width = 100
height = 130
path = os.path.join(mainfolder,subfolder)
if not os.path.isdir(path):
    os.makedirs(path)
    print("created")
classafire = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)
for i in range(100):
    success,frame = video.read()
    if not success:
        continue
    GreyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = classafire.detectMultiScale(GreyFrame,1.3,5)
    cv2.imshow("frame",frame)
    print(faces)