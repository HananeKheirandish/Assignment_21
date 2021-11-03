import numpy as np

import cv2

img = np.arange(0, 65025, 1, np.uint8)
img = np.reshape(img, (255, 255))

height, width = img.shape

for i in range(height):
  for j in range(width):
    img[i, j] = 255 - i

cv2.imwrite('new_6.jpg', img)

cv2.waitKey()