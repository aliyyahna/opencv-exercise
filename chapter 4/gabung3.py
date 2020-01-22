import cv2

lena = cv2.imread('./img/lena.bmp')
baboon = cv2.imread('./img/baboon.png')

hasilA = cv2.addWeighted(baboon, 0.5, lena, 0.5, 0)
cv2.imshow('Alfa: 0.5, beta: 0.5, gamma: 0.5', hasilA)

hasilB = cv2.addWeighted(baboon, 0.7, lena, 0.3, 0)
cv2.imshow('Alfa: 0.7, beta: 0.3, gamma: 0', hasilB)

hasilC = cv2.addWeighted(baboon, 0.3, lena, 0.7, 0)
cv2.imshow('Alfa: 0.3, beta: 0.7, gamma: 0', hasilA)

cv2.waitKey(0)
