import cv2;

citra = cv2.imread('./img/baboon.png', cv2.IMREAD_GRAYSCALE)
if not citra is None:
    cv2.imshow('Image', citra)
    cv2.waitKey(0)