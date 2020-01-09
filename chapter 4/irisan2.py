import cv2

citra = cv2.imread('./img/peppers.png')
citra[180:490, 170:425] = [255, 0, 0]
cv2.imshow('Irisan', citra)
cv2.waitKey(0)