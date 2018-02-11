import numpy as np
import cv2

watch_cascade = cv2.CascadeClassifier('watch.xml')
capture = cv2.VideoCapture(0)

while 1:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    watch = watch_cascade.detectMultiScale(gray, 1.3, 5)
    
   

    for (x,y,w,h) in watch:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
       

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
