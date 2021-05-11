import cv2
img = cv2.imread('FRIENDS.jpeg')
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0) #dst = cv2.GaussianBlur(src, (kernel),borderType). #Usually Gaussian Blur will be odd.  You can try changing the values of (21,21) and 0
cv2.imwrite("GaussianBlur.jpeg",gaussianBlurImg) #Save the gaussian blur image