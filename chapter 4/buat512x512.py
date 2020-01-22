import cv2
import numpy as np

# buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)

spaceman = cv2.imread('./img/Spaceman-colour.png', -1)
jumBaris = spaceman.shape[0]
jumKolom = spaceman.shape[1]

citra[0:jumBaris, 0:jumKolom, :] = spaceman[:, :, 0:3]
cv2.imshow('Hasil', citra)

cv2.waitKey(0)