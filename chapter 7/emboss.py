import cv2
import numpy as np

citra = cv2.imread('simba.png', 0)

kernel = np.float32([[-2, 0, 0],
                    [0, 0, 0],
                    [0, 0, 2]])

terfilter = cv2.filter2D(citra, -1, kernel)

hasil = np.hstack((citra, terfilter))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)