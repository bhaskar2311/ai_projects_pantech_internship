import cv2  

alg = "haarcascade_frontalface_default.xml"   #Haarcascade XML file/liabrary is a algorithm stored in XML file.With help of this we can able to detect face easily.

haar_cascade = cv2.CascadeClassifier(alg) #Function Cascade Classifier use to load the xml file into a variable

cam = cv2.VideoCapture(0)  #Laptop Camera is 0,External Cams Try 1,2 etc.

while True:
     #Bcoz of continuos video capture
    _,img = cam.read()  #Read the camera and store in variable
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #onvert into gray iamge for better and fast image processing
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)  #face = face_cascade.detectMultiScale(src, scalefactor,minNeighbors)
    #Above Function will give you x,y,w,h values. Then we can draw rectangle easily by using this values
    for (x,y,w,h) in face:
        cv2.rectangle(img , (x , y),(x+w , y+h) , (0,255,0) , 2 ) #Draw Rectangle around the Face
    cv2.imshow("FaceDetection",img) #Face Detection with Rectangle around face
    key = cv2.waitKey(1) #& 0xFF (If you keep wait key 0 then it will click only first frame)
    if key == 27 :  #27 is nothing but 'Esc' Button
        break
cam.release()
cv2.destroyAllWindows()

