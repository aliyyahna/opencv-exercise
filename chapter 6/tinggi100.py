import cv2

citra = cv2.imread('taipei101.png')

jumBaris, jumKolom = citra.shape[:2]
rasio = jumKolom / jumBaris
tinggiBaris = 100

hasil = cv2.resize(citra, (int(rasio * tinggiBaris), tinggiBaris))

cv2.imshow('Asal', citra)
cv2.imshow('Hasil', hasil)

cv2.waitKey(0)
