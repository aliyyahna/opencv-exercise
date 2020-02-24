import cv2
import random
import sys

if len(sys.argv) != 3:
    print('Pemakaian: python ' + 'drgaussian.py namaberkas sigma')
    sys.exit()

berkas = sys.argv[1]
sigma = float(sys.argv[2])
mu = 0

citra = cv2.imread(berkas, 0)
if citra is None:
    print('Tidak dapat membaca berkas', berkas)
    sys.exit()

hasil = citra.copy() #salin isi citra
jumBaris, jumKolom = hasil.shape[:2]

for baris in range(jumBaris):
    for kolom in range(jumKolom):
        nilaiBaru = hasil[baris, kolom] + \
                    random.gauss(mu, sigma)
        if nilaiBaru > 255:
            nilaiBaru = 255
        else:
            if nilaiBaru < 0:
                nilaiBaru = 0

        hasil[baris, kolom] = int(nilaiBaru)

cv2.imshow('Hasil rotasi', hasil)
cv2.waitKey()

#simpan citra
cv2.imwrite('simbagauss.png', hasil)
