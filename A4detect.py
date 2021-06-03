import numpy as np
import cv2
#from matplotlib import pyplot as plt
img = cv2.imread('testIm.jpg')
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

approx = cv2.approxPolyDP(big_contour,200,True)
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
coord = np.where(corner > 0.3* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
print(coord)
#corner1
corner_tmp1 = []
i = 0
for x, y in coord:
    corner_tmp1.append(x+y)
    i=i+1
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp1:
    if k<min_k:
        min_k=k
        min_i=i
    i=i+1
corner1 = coord[min_i]
#corner2
corner_tmp2 = []
i = 0
for x, y in coord:
    corner_tmp2.append((600-x)+y)
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
corner3 = coord[min_i]
#corner3
corner_tmp3 = []
i = 0
for x, y in coord:
    corner_tmp3.append(x+(600-y))
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
corner2 = coord[min_i]
#corner4
corner_tmp4 = []
i = 0
for x, y in coord:
    corner_tmp4.append((600-x)+(600-y))
    i=i+1
min_k = 1200
min_i = 0
i = 0
for k in corner_tmp4:
    if k<min_k:
        min_k=k
        min_i=i
    i=i+1
corner4 = coord[min_i]

print(corner1)
print(corner2)
print(corner3)
print(corner4)

#print(coord[1])
#모서리 길이 계산
VerticalLength = corner2[1]-corner1[1]
HorizontalLength = corner4[0]-corner2[0]
print(VerticalLength)
print(HorizontalLength)

# 코너 좌표에 동그리미 그리기 ---③
for x, y in coord:
    cv2.circle(imgray, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)


cv2.imshow('final', imgray)
contour2, y = cv2.findContours(thr, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#final4 = cv2.drawContours(img, contour2, -1, (0, 255, 0), 3)
#cv2.imshow('final2', final)
cv2.imshow('final4', final)
cv2.waitKey(0)