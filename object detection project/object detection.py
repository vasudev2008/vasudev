import imutils
import cv2
redLower=()
redUpper=()
cam=VideoCapture(0)
while True:
    (grabbed,frame)=cam.read()
    frame=imutils.resize(frame,width=1000)
    blurred=cv2.gaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        m=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius>10:
            cv2.circle(frame,(int(x),int(y),int(radius),(0,0,0),2)
                       print(center,radius)
            if radius>250:
                       print("stop")
            elif center[0]<150:
                print("Right")
                
            elif radius<250:
                print("front")
            else:
                print("stop")


     cv2.waitKey(10)
     if key==ord("Ese"):
         break
     cam.release()
     cv2.destroyAllWindows()
     


                
