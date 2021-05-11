import cv2
vs = cv2.VideoCapture(0) #Initialize the Camera. 0 value means Laptop Primary Camera, 1 and 2 for External Cameras
while True: #Infinite loop for running continuously
	_,img = vs.read() #1 value is lat like structure i.e. true or false i.e. Variable is unknown and img variable will get the camera frame value
	cv2.imshow('VideoStream', img) #This will show the camera feed in the window and Name will be shown 
	key = cv2.waitKey(1) & 0xFF #wait key 1 will return you 32 bit value on key press and 0xFF will give you only 8 bit data
	if key == ord("q"): #When you click 'q' then it wil break the loop and camera feed stops bcoz of release function.
		break
vs.release() #If you don't write this then it will give error like Camera is already in use.
cv2.destroyAllWindows()
