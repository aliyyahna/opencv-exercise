import cv2
from matplotlib import pyplot as plt

citra1 = cv2.imread('./img/baboon.png')
citra2 = cv2.imread('./img/lena.bmp')
citra3 = cv2.imread('./img/goldhill.png')
citra4 = cv2.imread('./img/boat.png')

# ubah bgr menjadi rgb
rgb1 = citra1[..., : : -1]
rgb2 = citra2[..., : : -1]
rgb3 = citra3[..., : : -1]
rgb4 = citra4[..., : : -1]

# tampilkan gambar
plt.subplot(221)
plt.imshow(rgb1)
plt.xticks([]), plt.yticks([])
plt.title('Baboon')

plt.subplot(222)
plt.imshow(rgb2)
plt.xticks([]), plt.yticks([])
plt.title('Lena')

plt.subplot(223)
plt.imshow(rgb3)
plt.xticks([]), plt.yticks([])
plt.title('Goldhill')

plt.subplot(224)
plt.imshow(rgb4)
plt.xticks([]), plt.yticks([])
plt.title('Boat')

plt.show()