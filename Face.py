import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')     #Importing Haarcascade file here.............

cap = cv.VideoCapture(0)     #openig webcam I'm going to detect live if wnat to detect in image already in your local pc comment this ad 8, 9
#line of code and uncamment the bellow line.

while True:
    _, img = cap.read()

    #img=cv.read("paht")
    img = cv.flip(img , 1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      #changing BGR to GRAYScale image..

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)           #apling ML to haarcascade file and image............

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              #finding pixel to draw line...................


    cv.imshow('img', img)                                               #Output image via showing image...................

    k = cv.waitKey(30)# & 0xff                                       #claose windows if it is ok................................
    if k==27:
        break
        
cap.release()
