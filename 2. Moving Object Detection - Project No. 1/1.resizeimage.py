import cv2
import imutils #Use for Basic Operations
img = cv2.imread('FRIENDS.jpeg') 
resizedImg = imutils.resize(img, width=500) #For resizing image with the help of imutils liabrary.
cv2.imwrite('resizedImage.jpeg', resizedImg) #Saving the resized image
