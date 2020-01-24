import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
jumBaris, jumKolom = citra.shape[:2]

matriks = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

cv2.imshow('Hasil penyekalaan', hasil)
cv2.waitKey(0)