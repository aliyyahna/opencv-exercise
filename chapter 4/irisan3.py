import cv2

citra = cv2.imread('./img/goldhill.png', cv2.IMREAD_UNCHANGED)
bagianA = citra[0:100, ...]
bagianB = citra[..., 250:]

cv2.imshow('Bagian A', bagianA)
cv2.imshow('Bagian B', bagianB)
cv2.waitKey(0)