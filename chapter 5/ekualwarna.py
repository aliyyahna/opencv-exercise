import cv2
import numpy as np

citra = cv2.imread('./img/baboon.png')

lab = cv2.cvtColor(citra, cv2.COLOR_BGR2LAB)

kanalLAB = cv2.split(lab)

kanalLAB[0] = cv2.equalizeHist(kanalLAB[0])

lab = cv2.merge(kanalLAB)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

hasil = np.hstack((citra, bgr))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)