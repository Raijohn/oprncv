import cv2
import numpy as np

MOON = cv2.imread("moon.jpg",cv2.IMREAD_COLOR)
HOUS = cv2.imread("hous.jpg",cv2.IMREAD_COLOR)
cv2.imshow("moonjpg",MOON)
cv2.waitKey(0)
cv2.imshow("housjpg",HOUS)
cv2.waitKey(0)
cv2.destroyAllWindows()
#adding images
images = cv2.add(MOON,HOUS)
cv2.imshow("imagesjpg",images)
cv2.waitKey(0)
cv2.destroyAllWindows()

#subtracting images
subtract_images = cv2.subtract(MOON,HOUS)
cv2.imshow("subtract_imagesjpg",subtract_images)
cv2.waitKey(0)
cv2.destroyAllWindows()

#weighted addition
add_weight = cv2.addWeighted(MOON,0.7,HOUS,0.4,0)
cv2.imshow("add_weightjpg",add_weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
#resizing
resize_images = cv2.resize(MOON,(500,400))
cv2.imshow("resize",resize_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
#erosion
PIKACHU = cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
K = np.ones((5,5))
erode_image = cv2.erode(PIKACHU,K)
cv2.imshow("erode",erode_image)
cv2.waitKey(0)
cv2.destroyAllWindows()  
#adding boreder
boreder_image = cv2.copyMakeBorder(PIKACHU,10,10,10,10,cv2.BORDER_CONSTANT,value = (255,0,0))
cv2.imshow("boreder",boreder_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
boreder_image_reflect = cv2.copyMakeBorder(PIKACHU,1000,1000,1000,1000,cv2.BORDER_REFLECT)
cv2.imshow("boreder_reflect",boreder_image_reflect)
cv2.waitKey(0)
cv2.destroyAllWindows() 
#edge detection
edge_image = cv2.Canny(PIKACHU,125,175)
cv2.imshow("edge",edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 