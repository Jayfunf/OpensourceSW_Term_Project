import cv2

image = cv2.imread('test1.jpeg')  #이미지 불러오기
cv2.imshow('test',image) #이미지 출력
cv2.waitKey(0)