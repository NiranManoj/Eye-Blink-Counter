import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY=LivePlot(640,360,[20,40],invert=True)
plotX=LivePlot(640,360,[20,40],invert=True)
ratioList1=[]
ratioList2=[]
count1=0
counter1=0
count2=0
counter2=0

color=(255,0,255)
color2=(255, 192, 203)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

idList = [22,23,24,26,110,157,158,159,160,161,130,243,257,362,374,263]


while True:
    #if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):

    success, img = cap.read()
    img = cv2.resize(img, (640,360))
    
    img, faces =detector.findFaceMesh(img, draw=False)
    

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img,face[id],5,color)
        
        leftUp = face[159]
        leftDown = face[23]
        leftLeft=face[130]
        leftRight=face[243]
        rightUp= face[257]
        rightDown=face[374]
        rightLeft=face[362]
        rightRight=face[263]

        lengthvert1,_=detector.findDistance(leftUp,leftDown)
        lengthhor1,_=detector.findDistance(leftLeft,leftRight)
        cv2.line(img,leftUp,leftDown,color2,3)
        cv2.line(img,leftLeft,leftRight,color2,3)
        a=100*(lengthvert1/lengthhor1)
        ratioList1.append(a)
        if len(ratioList1)>3:
            ratioList1.pop(0)
        ratavg=sum(ratioList1)/len(ratioList1)

        if ratavg<25 and counter1==0:
            count1+=1
            counter1=1
            color=(0,200,0)
        
        if counter1!=0:
            counter1+=1
            if counter1>10:
                counter1 =0
                color=(255,0,255)

        lengthvert2,_=detector.findDistance(rightUp,rightDown)
        lengthhor2,_=detector.findDistance(rightLeft,rightRight)
        cv2.line(img,rightUp,rightDown,color2,3)
        cv2.line(img,rightLeft,rightRight,color2,3)
        b=100*(lengthvert2/lengthhor2)
        ratioList2.append(b)
        if len(ratioList2)>3:
            ratioList2.pop(0)
        ratavg1=sum(ratioList2)/len(ratioList2)

        if ratavg<25 and counter2==0:
            count2+=1
            counter2=1
            color=(0,200,0)
        
        if counter2!=0:
            counter2+=1
            if counter2>10:
                counter2 =0
                color=(255,0,255)

        cvzone.putTextRect(img,f'Blink Count: {count2}',(50,100),colorR=color)
        cvzone.putTextRect(img,f'Blink Count: {count1}',(50,100),colorR=color)
        imgplot2=plotX.update(b)
        imgplot1=plotY.update(a)
        imgstack=cvzone.stackImages([img, imgplot1, imgplot2],1,1)

    else:
        imgstack=cv2.resize(img, (640,360))

    cv2.imshow('Image', imgstack)

    c = cv2.waitKey(1)

