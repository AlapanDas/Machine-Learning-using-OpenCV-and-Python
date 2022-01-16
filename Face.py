import cv2
from matplotlib.image import imread
face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(r'C:\Users\clash\Documents\ML in Python\Pro.mp4')
#img=cv2.imread('ML in Python\img.jpg')
while cap.isOpened():
    _, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.1,)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,x+h),(25,0,0),5)
        roi_gray=gray[y:y+h, x:x+w]
        roi_colour=img[y:y+h, x:x+w]
        eyes=eye.detectMultiScale(roi_gray)
        for( ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_colour, (ey,ey), (ex+ew,ex+eh), (0,205,0), 5)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break   

cap.release()