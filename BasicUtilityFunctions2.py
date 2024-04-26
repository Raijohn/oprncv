import cv2

PIKACHU = cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
cv2.imshow("pikachupng",PIKACHU)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#changing color space to grayscale
TURNPIKACHUGRAY = cv2.cvtColor(PIKACHU,cv2.COLOR_BGR2GRAY)
cv2.imshow("graypikachupng",TURNPIKACHUGRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()

#gaussian blur
GAUSSIANBLUR = cv2.GaussianBlur(PIKACHU,(5,5),0)
cv2.imshow("gausianblurpng",GAUSSIANBLUR)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#Median blur
MEDIANBLUR = cv2.medianBlur(PIKACHU,7)
cv2.imshow("medianblurpng",MEDIANBLUR)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#Bilatral blur
BILATERALBLUR = cv2.bilateralFilter(PIKACHU,7,80,80)
cv2.imshow("bilatralblurpng",BILATERALBLUR)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotation
row,col = PIKACHU.shape[0:2]
ROTATIONmetrix = cv2.getRotationMatrix2D((col/2,row/2),90,1)
ROTATEDPIKACHU = cv2.warpAffine(PIKACHU,ROTATIONmetrix,(row,col))
cv2.imshow("rotatedpikachupng",ROTATEDPIKACHU)
cv2.waitKey(0)
cv2.destroyAllWindows()