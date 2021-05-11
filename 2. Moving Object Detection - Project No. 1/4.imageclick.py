import cv2
import time
cam = cv2.VideoCapture(0) #Initialize the Camera. 0 value means Laptop Primary Camera, 1 and 2 for External Cameras
time.sleep(1) #Time Delay
_,img = cam.read() #1 value is lat like structure i.e. true or false i.e. Variable is unknown and img variable will get the camera frame value
cv2.imwrite("Clicked Image.jpg",img) #Clicked photo will be save in the directory
cam.release() #If you don't write this then it will give error like Camera is already in use.
