import cv2 
img = cv2.imread('Bhaskar.jpeg') #Read image
cv2.imshow('Bhaskar',img)  #Show image
cv2.imwrite('BhaskarNew.jpeg',img) #Chnage name of image and save
cv2.waitKey(0) #Display Timer. 0 is for infinite , 1000 is for 1 second display of image
cv2.destroyAllWindows()
