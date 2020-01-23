import cv2
import numpy as np

citra = cv2.imread('./img/peppers.png')
lab = cv2.cvtColor(citra, cv2.COLOR_BGR2LAB)

kanalLAB = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))

kanalLAB[0] = clahe.apply(kanalLAB[0])

lab = cv2.merge(kanalLAB)
bgr = cv2.merge(kanalLAB)
hasil = np.hstack((citra, bgr))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)