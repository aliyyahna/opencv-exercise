import cv2
import numpy as np

citra = cv2.imread('./img/peppers.png', 0)
ekual = cv2.equalizeHist(citra)
hasil = np.hstack((citra, ekual))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)