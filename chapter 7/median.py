import cv2
import numpy as np

citra = cv2.imread('simba.png')

blur1 = cv2.medianBlur(citra, 5)
blur2 = cv2.medianBlur(citra, 45)

hasil = np.hstack((citra, blur1, blur2))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)