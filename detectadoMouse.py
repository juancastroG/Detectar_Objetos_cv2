import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
mouseDetector = cv2.CascadeClassifier('cascade_M.xml')
while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    object = mouseDetector.detectMultiScale(gray,
    scaleFactor = 3,
    minNeighbors = 400,
    minSize = (100,120))
    for (x,y,w,h) in object:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Mouse',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()