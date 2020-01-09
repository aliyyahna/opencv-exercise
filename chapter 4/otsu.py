import cv2

citra = cv2.imread('./img/airplane.png', cv2.IMREAD_GRAYSCALE)
ambang, biner = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Asli', citra)
cv2.imshow('Otsu - nilai ambang = ' + str(int(ambang)), biner)
cv2.waitKey(0)