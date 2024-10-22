import cv2
import gray
import numpy as np
import sqlite3

from watchfiles import watch

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);

def insertorupdate(ID,Name,age):  #sqlite database
    conn = sqlite3.connect("sqlite.db")   #connection to database
    cmd = "SELECT*FROM STUDENTS WHERE ID="+str(ID);     #
    cursor=conn.execute(cmd);   # cursor to excute the command
    isRecordExist=0;
    for row in cursor:
        isRecordExist = 1;
    if isRecordExist==1:
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE ID=?",(Name,ID))
        conn.execute("UPDATE STUDENTS SET age=? WHERE ID=?", (age, ID))
    else:
        conn.execute("INSERT INTO STUDENTS (ID,Name,age) values(?,?,?)",(ID,Name,age))
    conn.commit()
    conn.close()

# inserting user defined values
ID = input("enter user id")
Name= input("enter the name:")
age = input("enter the age:")

insertorupdate(ID,Name,age)

# detecting the faces in web camera

sampleNum = 0;
while True:
    ret,img = cam.read(); # for opening the camera
    grey= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting the colorful img to greyscae img
    faces = faceDetect.detectMultiScale(grey,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1 # if detected it increments
        cv2.imwrite("Dataset/user."+str(ID)+"."+str(sampleNum)+".jpg",grey[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)   #delaytime
    cv2.imshow("Face",img)
    cv2.waitKey(1);
    if sampleNum>20:
        break;

cam.release() # close the camera
cv2.destroyAllWindows()   #closing the windows





