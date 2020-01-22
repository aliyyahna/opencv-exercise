import cv2
import numpy as np

citra = cv2.imread('./img/peppers.png')

# buat citra berwarna hitam
jumBaris = citra.shape[0]
jumKolom = citra.shape[1]

# matriks berisi nol
nol = np.zeros((jumBaris, jumKolom), np.uint8)

biru, hijau, merah = cv2.split(citra)
citraB = cv2.merge((biru, nol, nol))
citraH = cv2.merge((nol, hijau, nol))
citraM = cv2.merge((nol, nol, merah))

cv2.imshow('Kanal biru', citraB)
cv2.imshow('Kanal hijau', citraH)
cv2.imshow('Kanal merah', citraM)

cv2.waitKey(0)