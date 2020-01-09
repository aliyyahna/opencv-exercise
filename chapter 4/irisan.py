import cv2

citra = cv2.imread('./img/peppers.png')
bagian = citra[180:490, 170:425]
cv2.imshow('Irisan', bagian)
cv2.waitKey(0)