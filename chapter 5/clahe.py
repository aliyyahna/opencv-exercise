import cv2
import numpy as np

citra = cv2.imread('./img/baboon.png', 0)
clahe = cv2.createCLAHE(clipLimit = 12, tileGridSize = (8, 8))

ekual = clahe.apply(citra)
hasil = np.hstack((citra, ekual))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)