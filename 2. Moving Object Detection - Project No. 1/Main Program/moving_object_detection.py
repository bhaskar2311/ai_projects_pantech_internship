#First Task - Obtain Camera Feed
#Second Task - Capture First Image to Fix it as Background Image
#Third Task- Compare First Image(Background Image) and Current Image

import cv2
import time
import imutils #To resize for having better image view

cam = cv2.VideoCapture(0) #Initialize the Camera. 0 value means Laptop Primary Camera, 1 and 2 for External Cameras
time.sleep(1) #This is not necessary though. Optional.

firstFrame = None
area = 500 #Area is helpful obtaining how much change is occuring. e.g. In Home, If screen or cloth is there and it swings in front of camera then it should not detect as moving object
#We have to detect big objects like hand,animal or person paasing by etc.

while True:
	_,img = cam.read()
	text = "Normal" #Text For First Frame
	img = imutils.resize(img, width=500) #Resize image if you want in real time
	grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert into gray bcoz it is not require to do it in color image. Binary Image is enough.It will run fast and there will be less load on RAM
	gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0) #After Gaussian Blur we are going to do the thresholding which is very suitable for gaussian image
	if firstFrame is None: #When we get the first frame as none then we are going to assign the gaussianImg as FirstFrame
		firstFrame = gaussianImg # There was nothing inside firstFrame so we just assgined Gaussian Image over here
		continue #This loop will run only one time
	imgDiff = cv2.absdiff(firstFrame, gaussianImg) #With this we will find the diff. betn. Current Frame and First Frame. Compare each and every time.
	threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] #Black and White image.It may contain holes or dots.
	threshImg = cv2.dilate(threshImg, None, iterations=2) #Bcoz of dilate holes inside threshold image will be removed. Dilate increases the thickness.
	cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, 
		cv2.CHAIN_APPROX_SIMPLE) #Contours helful to find neighbourhood pixels so they can connect and we can find how much area is differed and we can plot the rectangle around moving object
        #E.g Hands...there is gap betn fingers but still it will recognize as 1 object
        #We will apply conoturs on copy of threshold image so we can use original threshold image later
	cnts = imutils.grab_contours(cnts) #store the contours values.Boundary around moving object.
	for c in cnts:  #Pass each and every count to detect whether there is movement or not
		if cv2.contourArea(c) < area: #If countours are less than area then only it is going to draw the rectangle
			continue
		(x, y, w, h) = cv2.boundingRect(c) #We will get the coordinates of object by this
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) #Drawing the Rectangle
		text = "Moving Object detected" 
	print(text)
	cv2.putText(img, text, (10, 20), 
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  #Don't put this in for loop bcoz if contour value not present it will not go in the loop and will give TEXT=NORMAL
	cv2.imshow("VideoStream", img)
	# cv2.imshow("Thresh", threshImg)
	# cv2.imshow("Image Difference", imgDiff)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cam.release()
cv2.destroyAllWindows()
