import cv2
print("Package Imported")

img= cv2.imread("resource/lena.png")
cv2.imshow("Image",img)
cv2.waitKey(0) #delay () mili sec