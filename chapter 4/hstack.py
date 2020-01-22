import cv2
import numpy as np

citraA = cv2.imread('./img/baboon.png')
citraB = cv2.imread('./img/lena.bmp')

hasil = np.hstack((citraA, citraB))

cv2.imshow('Hasil', hasil)

cv2.waitKey(0)