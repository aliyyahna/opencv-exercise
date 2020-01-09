import cv2

citra = cv2.imread('./img/goldhill.png', 0)
cv2.imshow('Citra asli', citra)

hasil = citra + 50
cv2.imshow('Citra hasil', hasil)

cv2.waitKey(0)