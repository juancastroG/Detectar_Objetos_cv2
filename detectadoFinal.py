import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 0: si es la camara principal, 1: si es la camara secundaria
mouseDetector = cv2.CascadeClassifier('cascade_M.xml')
usbDetector = cv2.CascadeClassifier('cascade_Usb.xml')
while True:
    #En estas lineas tomamos los frames dados por la camara
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Este objeto es para el mouse
    object = mouseDetector.detectMultiScale(gray,
    scaleFactor = 3,
    minNeighbors = 400,
    minSize = (100,120))

    #Este objeto es para la usb
    object_usb = usbDetector.detectMultiScale(gray,
        scaleFactor=280,
        minNeighbors=7500)

#Buscamos el Mouse en los frames
    for (x,y,w,h) in object:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Mouse',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)

#Buscamos la usb en los frames
    for (x,y,w,h) in object_usb:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Usb',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()