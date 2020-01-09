import cv2
import sys
import numpy as np 

if len(sys.argv) != 3:
    print('Masukkan nama berkas gambar dan nilai ambang')
else:
    berkas = sys.argv[1]
    ambang = int(sys.argv[2])
    citra = cv2.imread(berkas, cv2.IMREAD_GRAYSCALE)
    if citra is None:
        print('Tidak dapat membaca berkas', berkas)
    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        hasil = np.zeros((jumBaris, jumKolom), np.uint8)
        for brs in range(jumBaris):
            for kol in range(jumKolom):
                if citra[brs, kol] >= ambang:
                    hasil[brs, kol] = 255

        cv2.imshow('Asli', citra)
        cv2.imshow('Hasil', hasil)
        cv2.waitKey(0)