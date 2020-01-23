import cv2
from matplotlib import pyplot as plt

citra1 = cv2.imread('./img/baboon.png')
citra2 = cv2.imread('./img/lena.bmp')

# ubah bgr menjadi rgb
rgb1 = citra1[..., : : -1]
rgb2 = citra2[..., : : -1]

# tampilkan gambar
plt.subplot(121)
plt.imshow(rgb1)
plt.xticks([]), plt.yticks([])
plt.title('Kolom 1')

plt.subplot(122)
plt.imshow(rgb2)
plt.xticks([]), plt.yticks([])
plt.title('Kolom 2')

plt.show()