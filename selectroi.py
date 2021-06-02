import cv2
import numpy as np

img = cv2.imread('pot.jpg')
x1, y1, w1, h1 = cv2.selectROI('image', img, False)
print('pot head')
print(f'x :{x1} y :{y1} w :{w1} h :{h1}')

if w1 and h1:
    pot_head = cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (0, 204, 204), 3)
    cv2.imshow('drag', pot_head)

x2, y2, w2, h2 = cv2.selectROI('image', img, False)
print('pot')
print(f'x :{x2} y :{y2} w :{w2} z :{h2}')

cv2.setMouseCallback('img', img)
cv2.waitKey(0)