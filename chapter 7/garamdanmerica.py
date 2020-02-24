import cv2
import random
import sys

if len(sys.argv) != 3:
    print('Pemakaian: python ' + 'garamdanmerica.py nama berkas probabilitas')
    sys.exit()

berkas = sys.argv[1]
prob = float(sys.argv[2])
if prob > 1: prop = 0.1

citra = cv2.imread(berkas, 0)
if citra is None:
    print('Tidak dapat membaca berkas', berkas)
    sys.exit()

hasil = citra.copy() #Salin isi citra
jumBaris, jumKolom = hasil.shape[:2]

for baris in range(jumBaris):
    for kolom in range(jumKolom):
        nilaiAcak = random.random()
        if nilaiAcak < prob / 2:
            hasil[baris, kolom] = 0 # merica
        elif nilaiAcak > prob / 2 and\
            nilaiAcak <= prob:
            hasil[baris, kolom] = 255 # garam

cv2.imshow('Hasil rotasi', hasil)
cv2.waitKey()

# simpan citra
cv2.imwrite('simbagdm.png', hasil)