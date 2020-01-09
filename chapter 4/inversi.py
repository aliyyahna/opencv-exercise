import cv2
import sys
import numpy as np

if len(sys.argv) == 1:
    print('Masukkan nama berkas gambar')
else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_GRAYSCALE)
    if citra is None:
        print('Tidak dapat membaca berkas', berkas)
    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        hasil = np.zeros((jumBaris, jumKolom), np.uint8)

        for brs in range(jumBaris):
            for kol in range(jumKolom):
                hasil[brs, kol] = 255 - citra[brs, kol]

        cv2.imshow('Asli', citra)
        cv2.imshow('Hasil', hasil)
        cv2.waitKey(0)