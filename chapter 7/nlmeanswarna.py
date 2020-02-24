import cv2
import numpy as np
import sys

citra = cv2.imread('simbagdm.png', 0)
if citra is None:
    print('Berkas citra tak dapat membaca')
    sys.exit()

terfilter = cv2.fastNlMeansDenoisingColored(citra, None, 30)

hasil = np.hstack((citra, terfilter))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)