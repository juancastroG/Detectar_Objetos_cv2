import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
usbDetector = cv2.CascadeClassifier('cascade_Usb.xml')
while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    object = usbDetector.detectMultiScale(gray,
      scaleFactor=120,
        minNeighbors=4000,
    
    )
    for (x,y,w,h) in object:
        cv2.putText(frame,'USB',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()