import cv2
import sys
import matplotlib.pyplot as plt

if len(sys.argv) == 1:
    print('Masukkan nama berkas gambar')
else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra is None:
        print('Tidak dapat membaca berkas', berkas)
    else:
        # cek sebagai citra berwarna atau bukan
        if len(citra.shape) > 2:
            nkali = 3
        else:
            nkali = 1

        warna = ('b', 'g', 'r')
        for kanal in range(nkali):
            histo = cv2.calcHist([citra], [kanal], None, [256], [0, 256])
            plt.plot(histo, color = warna[kanal])

        plt.title('Histogram' + berkas)
        plt.show()