import cv2

citra = cv2.imread('./img/peppers.png')
bagian = citra[40:500, 60:200]
cv2.imshow('Irisan', bagian)
cv2.waitKey(0)