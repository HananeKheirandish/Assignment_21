import cv2

img = cv2.imread('3.jpg', 0)

img = img[::-1, ::-1]

cv2.imwrite('new_3.jpg', img)

cv2.waitKey()