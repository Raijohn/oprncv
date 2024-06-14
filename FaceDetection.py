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
for i in range(30):
    success,frame = video.read()
    #if not success:
    #    continue
    GreyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = classafire.detectMultiScale(GreyFrame,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        currentFrame = GreyFrame[y:y+h,x:x+w]
        finallImage = cv2.resize(currentFrame,(width,height))
        cv2.imwrite(path+"\\"+str(i)+".png",finallImage)
    cv2.imshow("frame",frame)
    cv2.waitKey(10)
    print(faces)
