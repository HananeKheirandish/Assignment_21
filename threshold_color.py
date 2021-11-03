import cv2

img = cv2.imread('4.jpg', 0)

height, width = img.shape
threshold = 105

for i in range(height):
  for j in range(width):
    if img[i,j] <= threshold:
      img[i,j] = 0

cv2.imwrite('new_4.jpg', img)

cv2.waitKey()