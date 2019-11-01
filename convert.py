import cv2
import sys
import numpy as np

def transform_pixel(pixel):
    if pixel[0] <= 8 and pixel[1] <= 8 and pixel[2] <= 8:
        return [0, 0, 0]
    else:
        return pixel

path = sys.argv[1]

img = cv2.imread(path)
img_black = img

print("Image Size Shape: {}".format(img.shape))

row_index = 0
column_index = 0

for row in img:
    for column in row:
        img_black[row_index][column_index] = transform_pixel(img[row_index][column_index])
        column_index = column_index + 1
    column_index = 0
    row_index = row_index + 1

cv2.imwrite("{}.black.png".format(path), img_black)