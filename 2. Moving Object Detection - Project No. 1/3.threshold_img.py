import cv2
img=cv2.imread('FRIENDS.jpeg')
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussBlur = cv2.GaussianBlur(grayImg,(21,21),0)
thresholdImg = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1] #dst = cv2.threshold(src, threshold, maxValueForThreshold,binary,type)[1] You can try by changing the value...Used To make binary color image
cv2.imwrite('threshold.jpeg',thresholdImg)


#cv2.thershold is going to written multiple values.Hence,
#thresholdImg = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
# _,thresholdImg = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)
#We can use this both. 1 variable will content exact thing which we want i.e. Image and another will contain unknown value