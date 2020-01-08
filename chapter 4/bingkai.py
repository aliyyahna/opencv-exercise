import cv2

citra = cv2.imread('./img/goldhill.png')
hasil = citra.copy() # salin isi citra

# pengolahan citra
TEBAL = 20
HITAM = 0

jumBaris = hasil.shape[0]
jumKolom = hasil.shape[1]

# bingkai di atas
for baris in range(TEBAL):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

# bingkai di bawah
for baris in range(jumBaris - TEBAL - 1, jumBaris):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

# bingkai di kiri
for baris in range(TEBAL, jumBaris - TEBAL - 1):
    for kolom in range(TEBAL):
        hasil[baris, kolom] = HITAM

# bingkai di kanan
for baris in range(TEBAL, jumBaris - TEBAL - 1):
    for kolom in range(jumKolom - TEBAL - 1, jumKolom):
        hasil[baris, kolom] = HITAM

cv2.imshow('Gambar asal', citra)
cv2.imshow('Gambar hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()