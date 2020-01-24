import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
jumBaris, jumKolom = citra.shape[:2]

matriks = cv2.getRotationMatrix2D((jumKolom // 2, jumBaris // 2), -15, 1)
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

cv2.imshow('Hasil translasi', hasil)
cv2.waitKey(0)