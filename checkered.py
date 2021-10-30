import numpy as np

import cv2

img = np.arange(0, 640000, 1, np.uint8)
img = np.reshape(img, (800, 800))

for i in range(0,800,100):
    for j in range(0,800,100):
        if ((i+j)/4)%2==0:
            img[i:i+100,j:j+100]=255
        else:
            img[i:i+100,j:j+100]=0
    
cv2.imshow('checkered', img)
cv2.imwrite('checkered.jpg', img)
cv2.waitKey()