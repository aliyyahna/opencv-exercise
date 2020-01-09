import cv2

citra = cv2.imread('./img/airplane.png', cv2.IMREAD_GRAYSCALE)
ambang, binerA = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY)
ambang, binerB = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Asli', citra)
cv2.imshow('THRESH BINARY', binerA)
cv2.imshow('THRESH BINARY INV', binerB)
cv2.waitKey(0)