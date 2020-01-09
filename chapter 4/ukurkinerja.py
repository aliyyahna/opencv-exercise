import cv2
import numpy as np 

citra = cv2.imread('./img/lena.bmp', cv2.IMREAD_GRAYSCALE)

# proses
awal = cv2.getTickCount()

jumBaris = citra.shape[0]
jumKolom = citra.shape[1]
hasil = np.zeros((jumBaris, jumKolom), np.uint8)

for brs in range(jumBaris):
    for kol in range(jumKolom):
        hasil[brs, kol] = 255 - citra[brs, kol]
    
akhir = cv2.getTickCount()
selangWaktu = (akhir - awal) / cv2.getTickFrequency()
print('Waktu untuk proses 1:', selangWaktu, 'detik')

# proses 2
awal = cv2.getTickCount()

hasil = 255 - citra

akhir = cv2.getTickCount()
selangWaktu = (akhir - awal) / cv2.getTickFrequency()
print('Waktu untuk proses 2:', selangWaktu, 'detik')