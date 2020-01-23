import cv2

citra = cv2.imread('taipei101.png')
jumBaris, jumKolom = citra.shape[:2]

hasil = cv2.resize(citra, (int(0.5 * jumBaris), int(0.5 * jumKolom)))

cv2.imshow('Asal', citra)
cv2.imshow('Hasil', hasil)

cv2.waitKey(0)