import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
냄비의 원을 noisy없이 검출하기 위해서 selectROI활용해서 검출하는방법으로 진행해야할 듯함
'''

src = cv2.imread("pot3.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contour, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contour))
print(contour[0].shape)
x, y, w, h = cv2.boundingRect(contour[2])
print(x, y, w, h)
ROI = src[y:y+h, x:x+w]

cv2.imshow("dst", th)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("dst", ROI)
cv2.waitKey(0)
cv2.destroyAllWindows()


# circles = cv2.HoughCircles(th, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 80, maxRadius = 120)
# print(circles.shape)

# for i in circles[0]:
#     cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), 5)

# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread('pot2.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, th = cv2.threshold(gray, 127, 255, 0)
#blur = cv2.GaussianBlur(img, (5,5), 0)
#bilateral = cv2.bilateralFilter(img, 5, 175, 175)
# edges = cv2.Canny(img,100,200)
# contours, hierarchy = cv2.findContours(th, 2, 1)
# cnt = contours
# bir_contour = list()
# max = 0
# for i in cnt:
#     area = cv2.contourArea(i)
#     if(area > max):
#         max = area
#         big_contour = i

# final = cv2.drawContours(img, big_contour, -1, (0, 255, 0), 3)
# cv2.imshow('final', final)
# cv2.waitKey(0)

# cv2.imshow('original image', img)
# cv2.waitKey(0)

# cv2.imshow('gaussian image', blur)
# cv2.waitKey(0)

# cv2.imshow('bilateral image', bilateral)
# cv2.waitKey(0)

# cv2.imshow('edges image', edges)
# cv2.waitKey(0)

# contours, hierarchy = cv2.findContours(th, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# contours_list = list()
# for i, contour in enumerate(contours):
#     img = cv2.imread('pot2.jpg')
#     approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
#     area = cv2.contourArea(contour)
#     # print(i, hierarchy[0][i])
    
#     if ((len(approx) > 5) & (area > 30)):
#         contours_list.append(contour)
#         # cv2.drawContours(img, contour, -1, (255, 0, 0), 1)
#         # cv2.imshow('each', img)
#         # cv2.waitKey(0)

# cv2.drawContours(img, contours_list, -1, (255, 0, 0), 2)
# cv2.imshow('Circle detect', img)
# cv2.waitKey(0)

# for i in range(len(contours)):
#     cv2.drawContours(img, [contours[i]], 0, (0, 0, 255), 2)
#     cv2.putText(img, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
#     print(i, hierarchy[0][i])

# cv2.imshow("src", img)
# cv2.waitKey(0)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()