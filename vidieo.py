import cv2,os
import numpy as np
from PIL import Image

path = "C:\\Users\\kam\\OneDrive\\Desktop\\open cv\\vidio_images"
print(path)
number_of_images = len(os.listdir(path))
#finding averige size of imige
for file in os.listdir(path):
    image = Image.open(os.path.join(path,file))
    w,h = image.size
    print(w)
    print(h)
