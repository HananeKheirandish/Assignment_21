import numpy as np

import cv2

img = np.arange(0, 90000, 1, np.uint8)
img = np.reshape(img, (300, 300))

img[::] = 255

img[60:220, 90:105] = 0
img[135:150, 105:170] = 0
img[60:220, 170:185] = 0

cv2.imwrite('7.jpg', img)

cv2.waitKey()