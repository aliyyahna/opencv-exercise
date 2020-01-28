import cv2
import numpy as np

citra = cv2.imread('simba.png')
jumBaris, jumKolom = citra.shape[:2]

citra = cv2.resize(citra, (int(0.5 * jumBaris), int(0.5 * jumKolom)))

kernelA = np.float32([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])
kernelB = np.float32([[-1, -1, -1],
                    [-1, 10, -1],
                    [-1, -1, -1]])
kernelC = np.float32([[1, -1, 1],
                    [-1, 13, -1],
                    [-1, -1, -1]])

filterA = cv2.filter2D(citra, -1, kernelA)
filterB = cv2.filter2D(citra, -1, kernelB)
filterC = cv2.filter2D(citra, -1, kernelC)

baris1 = np.hstack((citra, filterA))
baris2 = np.hstack((filterB, filterC))

hasil = np.vstack((baris1, baris2))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)