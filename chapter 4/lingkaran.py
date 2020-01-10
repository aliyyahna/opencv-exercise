import cv2
import sys

if len(sys.argv) == 1:
    print('Masukkan nama berkas gambar')
else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra is None:
        print('Tidak dapat membaca berkas', berkas)
    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        xTengah = jumKolom // 2
        yTengah = jumBaris // 2

    # buat lingkaran
    cv2.circle(citra, (xTengah, yTengah), 100, [255,255,255], 10)

    cv2.imshow('Hasil', citra)
    cv2.waitKey(0)