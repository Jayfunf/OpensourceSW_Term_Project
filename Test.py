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

#final = cv2.drawContours(img, big_contour, -1, (0, 255, 0), 3)
#final = cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
contour_img = cv2.drawContours(img_tmp, [approx], -1, (0, 255, 0), 3)
imgray = cv2.cvtColor(img_tmp,cv2.COLOR_BGR2GRAY)
ret,thr = cv2.threshold(imgray,127,255,0)


# 해리스 코너 검출 ---①
corner = cv2.cornerHarris(imgray, 2, 3, 0.04)
# 변화량 결과의 최대값 10% 이상의 좌표 구하기 ---②
coord = np.where(corner > 0.5* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
print(coord)
# 코너 좌표에 동그리미 그리기 ---③
for x, y in coord:
    cv2.circle(imgray, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)


cv2.imshow('final', imgray)
contour2, y = cv2.findContours(thr, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
final4 = cv2.drawContours(img, contour2, -1, (0, 255, 0), 3)
#cv2.imshow('final2', final)
cv2.imshow('final4', final4)
cv2.waitKey(0)