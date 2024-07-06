import cv2
from matplotlib import pyplot as plt # as alias

img = cv2.imread('images/cat.jpg', cv2.IMREAD_COLOR)

b, g, r = cv2.split(img) # img b,g,r
img2 = cv2.merge([r,g,b]) # b, r Merge

plt.imshow(img2)
plt.xticks([]) # x
plt.yticks([]) # y
plt.show()