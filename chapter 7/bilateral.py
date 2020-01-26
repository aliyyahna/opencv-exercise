import cv2
import numpy as np

citra = cv2.imread('simba.png')

blur1 = cv2.bilateralFilter(citra, 10, 75, 75)
blur2 = cv2.bilateralFilter(citra, 10, 150, 100)

hasil = np.hstack((citra, blur1, blur2))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)