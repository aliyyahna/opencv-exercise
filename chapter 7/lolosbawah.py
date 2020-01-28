import cv2
import numpy as np

citra = cv2.imread('goldhill.png', 0)

kernel = np.float32([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) / 9

terfilter = cv2.filter2D(citra, -1, kernel)

hasil = np.hstack((citra, terfilter))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)