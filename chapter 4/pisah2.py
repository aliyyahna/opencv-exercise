import cv2

citra = cv2.imread('./img/peppers.png')

biru = citra[:, :, 0]
hijau = citra[:, :, 1]
merah = citra[:, :, 2]

cv2.imshow('Kanal biru', biru)
cv2.imshow('Kanal hijau', hijau)
cv2.imshow('Kanal merah', merah)

cv2.waitKey(0)