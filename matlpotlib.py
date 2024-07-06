import cv2
from matplotlib import pyplot as plt # as alias

# litmus color

img = cv2.imread('images/cat.jpg', cv2.IMREAD_UNCHANGED)

x = [50, 100,150, 200] 
y = [30, 60,90, 120] 
xlabels = ['X-axis-1', 'X-axis-2', 'X-axis-3', 'X-axis-4'] 
ylabels = ['Y-axis-1', 'Y-axis-2', 'Y-axis-3', 'Y-axis-4'] 


plt.imshow(img)
# plt.xticks(x,xlabels) # ticks, labels, **kwargs 
# plt.yticks(y,ylabels) # y
plt.xticks([]) # ticks, labels, **kwargs 
plt.yticks([]) # ticks, labels, **kwargs 
plt.show()