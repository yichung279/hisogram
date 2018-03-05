import cv2
import numpy as np

img = cv2.imread('test.jpg',0)
equ = cv2.equalizeHist(img)
cv2.imwrite('result.jpg', equ)
