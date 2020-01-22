import cv2
import numpy as np

# buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)
alfa = np.zeros((512, 512), np.uint8)

spaceman = cv2.imread('./img/Spaceman-colour.png', -1)
jumBaris = spaceman.shape[0]
jumKolom = spaceman.shape[1]

citra[0:jumBaris, 0:jumKolom, :] = spaceman[:, :, 0:3]
alfa[0:jumBaris, 0:jumKolom] = spaceman[:, :, 3]
cadar = cv2.merge((alfa, alfa, alfa))
kebalikan = cv2.bitwise_not(cadar)

goldhill = cv2.imread('./img/goldhill.png')

hasil_and = cv2.bitwise_and(goldhill, kebalikan)
cv2.imshow('Hasil and', hasil_and)
print(hasil_and.shape)

hasil_add = cv2.add(hasil_and, citra)
cv2.imshow('Hasil add', hasil_add)

cv2.waitKey(0)