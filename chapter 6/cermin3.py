import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
jumBaris, jumKolom = citra.shape[:2]

matriks = np.float32([[1, 0, 0], [0, -1, jumBaris]])
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

gab = np.hstack((citra, hasil))

cv2.imshow('Hasil pencerminan', gab)
cv2.waitKey(0)


