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
    info = citra.shape
    if len(info) == 2:
        print('Citra berskala keabu-abuan')
    else:
        print('Citra berwarna')