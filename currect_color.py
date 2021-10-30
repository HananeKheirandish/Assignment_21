import cv2

img_1 = cv2.imread('1.jpg', 0)
img_2 = cv2.imread('2.jpg', 0)

img_1[:,:] = 255 - img_1[:,:]
img_2[:,:] = 255 - img_2[:,:]

cv2.imwrite('new_1.jpg', img_1)
cv2.imwrite('new_2.jpg', img_2)

cv2.waitKey()