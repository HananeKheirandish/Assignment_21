import cv2

img = cv2.imread('5.png', 0)

height, width = img.shape

for i in range(height):
  for j in range(width):
    if 70 < i+j < 100:
      img[i, j] = 0

cv2.imwrite('new_5.png', img)

cv2.waitKey()