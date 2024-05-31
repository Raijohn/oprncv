import cv2,os
import numpy as np
from PIL import Image

path = "C:\\Users\\kam\\OneDrive\\Desktop\\open cv\\vidio_images"
os.chdir(path)
print(path)
number_of_images = len(os.listdir(path))
totalW = 0
totalH = 0
#finding averige size of image
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image = Image.open(os.path.join(path,file))
        w,h = image.size
        totalW = totalH + w
        totalH = totalH + h

avaregeW = totalW // number_of_images
print(avaregeW)

avaregeH = totalH // number_of_images
print(avaregeH)
#resising te images to avarege size
images = []
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image = Image.open(os.path.join(path,file))
        resized_image = image.resize((avaregeW,avaregeH))
        resized_image.save(file,"JPEG")
        images.append(file)

#vidieo genaration
image_colage = "image_colage.avi"
the_video = cv2.VideoWriter(image_colage,0,0.5,(avaregeW,avaregeH),)
for image in images:
    add = cv2.imread(os.path.join(path,image))
    the_video.write(add)

    
    
