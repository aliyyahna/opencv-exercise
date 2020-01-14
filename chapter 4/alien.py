import cv2
import numpy as np

# buat citra berwarna hitam
citra = np.zeros((256, 256, 3), np.uint8)

# buat elips
cv2.ellipse(citra, (128, 128), (100, 50), 0, 0, 360, (255, 255, 255), 5)

# buat busur
cv2.ellipse(citra, (128, 230), (80, 50), 0, -180, 0, (255,255,255), 5)

# buat mata
cv2.circle(citra, (128, 128), 10, (0, 0, 128), 3)

# buat belalai
cv2.line(citra, (128, 80), (128, 40), (255, 255, 255), 3)
cv2.circle(citra, (128, 45), 5, (255, 255, 255), 3)

cv2.imshow('Hasil', citra)
cv2.waitKey(0)