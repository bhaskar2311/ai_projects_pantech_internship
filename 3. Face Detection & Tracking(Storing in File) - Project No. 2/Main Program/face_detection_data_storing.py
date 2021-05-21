import cv2
import os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = "dataset"  
sub_data = "bhaskar"     

path = os.path.join(datasets, sub_data)  #It will go to dataset\bhaskar
if not os.path.isdir(path):
    os.mkdir(path)   #If there is no such path then it will create it

(width, height) = (130, 100)
face_cascade = cv2.CascadeClassifier(haar_file)
cam = cv2.VideoCapture(0)  #Laptop Camera is 0,External Cams Try 1,2 etc.

count = 1
while count < 31:
    print(count)
    _,img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face = grayImg[y:y + h, x:x + w]  #Y to Y+h   This will give Face Image Only
        face_resize = cv2.resize(face, (width, height))  #This will resize and then we can save
        cv2.imwrite('%s/%s.jpg' % (path,count), face_resize) #This will save gray images in DB
    count += 1
	#Above Lopp will save 30 images

    cv2.imshow('OpenCV', img)
    key = cv2.waitKey(1)
    if key == 27:  
        break
print("Dataset obtained successfully")
cam.release()
cv2.destroyAllWindows()
