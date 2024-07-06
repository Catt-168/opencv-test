import cv2 as cv

scale = {
    "color": cv.IMREAD_COLOR, # default flag, 1
    "graySacle": cv.IMREAD_GRAYSCALE, # grayScale, 0
    "unchanged": cv.IMREAD_UNCHANGED # include alpha channel, -1
}

img1 = cv.imread('images/cat.jpg', scale["color"]) # read img
img2 = cv.imread('images/cat.jpg', scale["graySacle"]) # read img
img3 = cv.imread('images/cat.jpg', scale["unchanged"]) # read img

cv.imshow('Color',img1) # open new window, title & pixel matrix
cv.imshow('GrayScale',img2) # open new window, title & pixel matrix
cv.imshow('Unchanged',img3) # open new window, title & pixel matrix

cv.waitKey(0) # keyboard binding funciton, setTimeout or key to be pressed
# cv.destroyAllWindows()