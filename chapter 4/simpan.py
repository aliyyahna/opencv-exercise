import cv2
import sys

citra = cv2.imread('./img/goldhill.png', 0)

hasil = 255 - citra
cv2.imwrite('hasil.png', hasil)

print('Citra telah disimpan di hasil.png')
