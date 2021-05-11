import cv2
image = cv2.imread('Bhaskar.jpeg') #Read Image
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Color Conversion
cv2.imwrite('gray_image.jpeg',greyImage) #Save i.e. Write on image
cv2.imshow('Color_image',image) #This will show you colored images i.e. Original Image
cv2.imshow('Grey_image',greyImage) #This will show you gray image which we recently converted
cv2.waitKey(0) #It will present on the screen for infinite time (0: Infinite Time , 1000: 1 sec)
cv2.destroyAllWindows() #Necessary to destro all windows.