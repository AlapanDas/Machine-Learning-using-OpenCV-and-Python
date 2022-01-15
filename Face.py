import cv2
from matplotlib.image import imread

face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(r'C:\Users\clash\Desktop\Git\ML in Python\Pro.mp4')

#img=cv2.imread('ML in Python\img.jpg')

while cap.isOpened():
    _, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,x+h),(25,0,0),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break   
cap.release()