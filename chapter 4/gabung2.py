import cv2

lena = cv2.imread('./img/lena.bmp')
baboon = cv2.imread('./img/baboon.png')
hasil = cv2.add(baboon, lena)

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
