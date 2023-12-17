import cv2
import os
import time

mypath= 'data/images' #Rasbperry Pi: '/home/pi/desktop/data/images'
cameraNo=0
cameraBrightness=100
moduleVal=10
minBlur=500
grayImage=False
saveData=True
showimage=True
imgWidth=180
imgHeight=120


global countFolder
cap= cv2.VideoCapture(cameraNo)
cap.set(3,640)
cap.set(4,480)
cap.set(10,cameraBrightness)

count=0
countSave=0

def saveDataFunc():
    global countFolder
    countFolder=0
    while os.path.exists(mypath+ str(countFolder)):
        countFolder=countFolder + 1
    os.makedirs(mypath + str(countFolder))

if saveData:saveDataFunc()

while True:
    success, img = cap.read()
    img= cv2.resize(img,(imgWidth,imgHeight))
    if grayImage: img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % moduleVal ==0 and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(mypath + str(countFolder)+'/'+str(countSave)+" "+ str(int(blur))+" "+str(nowTime)+".png",img)
            countSave+=1
    if showimage:
        cv2.imshow("Image",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



