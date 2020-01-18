import cv2

citra = cv2.imread('./img/baboon.png')

# buat tulisan
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX + \
        cv2.FONT_ITALIC
cv2.putText(citra, 'Baboon', (10, 500), font, 4, (0, 0, 0), 10)


cv2.imshow('Hasil', citra)
cv2.waitKey(0)