import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
jumBaris, jumKolom = citra.shape[:2]
hasil = cv2.flip(citra, 0)
gab = np.hstack((citra, hasil))

cv2.imshow('Hasil pencerminan', gab)
cv2.waitKey(0)