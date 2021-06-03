"""
import cv2
import numpy as np

img = cv2.imread('testIMG4.jpg')
img = cv2.resize(img, dsize=(1500, 900), interpolation=cv2.INTER_AREA)
img = cv2.resize(img, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 해리스 코너 검출 ---①
corner = cv2.cornerHarris(gray, 2, 3, 0.04)
# 변화량 결과의 최대값 10% 이상의 좌표 구하기 ---②
coord = np.where(corner > 0.2* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)

# 코너 좌표에 동그리미 그리기 ---③
for x, y in coord:
    cv2.circle(img, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)

# 변화량을 영상으로 표현하기 위해서 0~255로 정규화 ---④
corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# 화면에 출력

corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)
merged = np.hstack((corner_norm, img))
cv2.imshow('Harris Corner', merged)
cv2.waitKey()
cv2.destroyAllWindows()
"""

import numpy as np
import cv2
#from matplotlib import pyplot as plt
img = cv2.imread('testImage4.jpg')
img_tmp = cv2.imread('none.jpg')
img = cv2.resize(img, dsize=(1500, 900), interpolation=cv2.INTER_AREA)
img = cv2.resize(img, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
img_tmp = cv2.resize(img_tmp, dsize=(1500, 900), interpolation=cv2.INTER_AREA)
img_tmp = cv2.resize(img_tmp, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 127, 255, 0)
#blur = cv2.GaussianBlur(img, (5,5), 0)
#bilateral = cv2.bilateralFilter(img, 5, 175, 175)
# edges = cv2.Canny(img,100,200)
contours, hierarchy = cv2.findContours(th, 2, 1)
cnt = contours
bir_contour = list()
max = 0
for i in cnt:
    area = cv2.contourArea(i)
    if(area > max):
        max = area
        big_contour = i

approx = cv2.approxPolyDP(big_contour,50,True)
#final3 = cv2.drawContours(img_tmp, [approx], -1, (0, 255, 0), 3)
#im2, contour2, hierarchy = cv2.findContours(final3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print(im2)
#print(contour2)
#print(hierarchy)

final = cv2.drawContours(img, big_contour, -1, (0, 255, 0), 3)
final = cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
contour_img = cv2.drawContours(img_tmp, [approx], -1, (0, 255, 0), 3)
imgray = cv2.cvtColor(img_tmp,cv2.COLOR_BGR2GRAY)
ret,thr = cv2.threshold(imgray,127,255,0)


# 해리스 코너 검출 ---①
corner = cv2.cornerHarris(imgray, 2, 3, 0.04)
# 변화량 결과의 최대값 10% 이상의 좌표 구하기 ---②
coord = np.where(corner > 0.1* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
print(coord)
#corner1
corner_tmp1 = []
i = 0
for a in approx:
    corner_tmp1.append(a[0][0]+a[0][1])
    i=i+1
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp1:
    if k<min_k:
        min_k=k
        min_i=i
    i=i+1
corner1 = approx[min_i]
#corner2
corner_tmp2 = []
i = 0
for a in approx:
    corner_tmp2.append((600-a[0][0])+a[0][1])
    i=i+1
print(corner_tmp2)
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp2:
    #print(k)
    #print(min_k)
    if k<min_k:
        min_k=k
        min_i=i
    i=i+1
corner3 = approx[min_i]
#corner3
corner_tmp3 = []
i = 0
for a in approx:
    corner_tmp3.append(a[0][0]+(600-a[0][1]))
    i=i+1
print(corner_tmp3)
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp3:
    if k<min_k:
        min_k=k
        min_i=i
        #print(min_k)
        #print(min_i)
    i=i+1
corner2 = approx[min_i]
#corner4
corner_tmp4 = []
i = 0
for a in approx:
    corner_tmp4.append((600-a[0][0])+(600-a[0][1]))
    i=i+1
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp4:
    if k<min_k:
        min_k=k
        min_i=i
    i=i+1
corner4 = approx[min_i]

print(corner1)
print(corner2)
print(corner3)
print(corner4)

#print(coord[1])
#모서리 길이 계산
#VerticalLength = corner2[1]-corner1[1]
#HorizontalLength = corner4[0]-corner2[0]
#print(VerticalLength)
#print(HorizontalLength)

# 코너 좌표에 동그리미 그리기 ---③
for x, y in coord:
    cv2.circle(imgray, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)


cv2.imshow('final', imgray)
contour2, y = cv2.findContours(thr, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#final4 = cv2.drawContours(img, contour2, -1, (0, 255, 0), 3)
#cv2.imshow('final2', final)
cv2.imshow('final4', final)
cv2.waitKey(0)

"""
import cv2
import numpy as np
import utlis

pathImage = 'testIMG6.jpeg'
heightImg = 640
widthImg  = 480

utlis.initializeTrackbars()
count=0

while (1):

    img = cv2.imread(pathImage)
    img = cv2.resize(img, (widthImg, heightImg)) # RESIZE IMAGE
    imgBlank = np.zeros((heightImg,widthImg, 3), np.uint8) # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
    thres=utlis.valTrackbars() # GET TRACK BAR VALUES FOR THRESHOLDS
    imgThreshold = cv2.Canny(imgBlur,thres[0],thres[1]) # APPLY CANNY BLUR
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2) # APPLY DILATION
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION

    ## FIND ALL COUNTOURS
    imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # DRAW ALL DETECTED CONTOURS

    # FIND THE BIGGEST COUNTOUR
    biggest, maxArea = utlis.biggestContour(contours) # FIND THE BIGGEST CONTOUR
    if biggest.size != 0:
        biggest=utlis.reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
        imgBigContour = utlis.drawRectangle(imgBigContour,biggest,2)
        pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
        pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

        #REMOVE 20 PIXELS FORM EACH SIDE
        imgWarpColored=imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
        imgWarpColored = cv2.resize(imgWarpColored,(widthImg,heightImg))

        # APPLY ADAPTIVE THRESHOLD
        imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
        imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
        imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
        imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre,3)

        # Image Array for Display
        imageArray = ([img,imgGray,imgThreshold,imgContours],
                      [imgBigContour,imgWarpColored, imgWarpGray,imgAdaptiveThre])

    else:
        imageArray = ([img,imgGray,imgThreshold,imgContours],
                      [imgBlank, imgBlank, imgBlank, imgBlank])

    # LABELS FOR DISPLAY
    lables = [["Original","Gray","Threshold","Contours"],
              ["Biggest Contour","Warp Prespective","Warp Gray","Adaptive Threshold"]]

    stackedImage = utlis.stackImages(imageArray,0.75,lables)
    cv2.imshow("Result",stackedImage)

    # SAVE IMAGE WHEN 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Scanned/myImage"+str(count)+".jpg",imgWarpColored)
        cv2.rectangle(stackedImage, ((int(stackedImage.shape[1] / 2) - 230), int(stackedImage.shape[0] / 2) + 50),
                      (1100, 350), (0, 255, 0), cv2.FILLED)
        cv2.putText(stackedImage, "Scan Saved", (int(stackedImage.shape[1] / 2) - 200, int(stackedImage.shape[0] / 2)),
                    cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imshow('Result', stackedImage)
        cv2.waitKey(300)
        count += 1
"""