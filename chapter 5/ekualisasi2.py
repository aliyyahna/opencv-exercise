import cv2
import numpy as np
from matplotlib import pyplot as plt

citra = cv2.imread('./img/peppers.png', 0)
ekual = cv2.equalizeHist(citra)

# tampilkan gambar asal dan hasil
plt.subplot(121)
plt.imshow(citra, cmap = plt.get_cmap('gray'),
                  vmin = 0, vmax = 255)
plt.xticks([]), plt.yticks([])
plt.title('Citra semula')

plt.subplot(122)
plt.imshow(ekual, cmap = plt.get_cmap('gray'),
                  vmin = 0, vmax = 255)
plt.xticks([]), plt.yticks([])
plt.title('Citra hasil')

plt.show()