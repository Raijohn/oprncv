import cv2
#reading and displaying an image
PIKACHU = cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
cv2.imshow("pikachupng",PIKACHU)
cv2.waitKey(0)
cv2.destroyAllWindows()
#reading a grayscale image
PIKACHUgray = cv2.imread("pikachu.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("pikachupng",PIKACHUgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#save an image
cv2.imwrite("PIKACHUgray.png",PIKACHUgray)
print(PIKACHUgray)
#split B G R channels
B,G,R=cv2.split(PIKACHU)
cv2.imshow("B",B)
cv2.waitKey(0)
cv2.imshow("G",G)
cv2.waitKey(0)
cv2.imshow("R",R)
cv2.waitKey(0)
cv2.destroyAllWindows()