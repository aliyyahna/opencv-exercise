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
        
        FONT = cv2.FONT_HERSHEY_DUPLEX
        UKURAN = 2
        KETEBALAN = 1

        info1, info2 = cv2.getTextSize(berkas, FONT, UKURAN, KETEBALAN)

        posisiX = (jumBaris - info1[0]) // 2
        posisiY = (jumBaris - info1[1]) // 2 + info1[1]

        print(jumBaris, jumKolom, posisiX, posisiY)
        print(info1, info2)

        cv2.putText(citra, berkas, (posisiX, posisiY), FONT, UKURAN, (255, 255, 255), KETEBALAN)

        cv2.imshow('Hasil', citra)
        cv2.waitKey(0)