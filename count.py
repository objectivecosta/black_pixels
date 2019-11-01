import cv2
import sys
import numpy as np

path = sys.argv[1]

img = cv2.imread(path)
pixels = img.reshape(-1, 3)

total_count = 0
black_count = 0
almost_black_count = 0

for pixel in pixels:
    total_count = total_count + 1
    if pixel[0] == pixel[1] == pixel[2] == 0:
        black_count = black_count + 1

    if pixel[0] <= 8 and pixel[1] <= 8 and pixel[2] <= 8:
        almost_black_count = almost_black_count + 1

print("Total Pixel Count: {}".format(total_count))
print("Black Pixel Count: {}".format(black_count))
print("Almost Black Pixel Count: {}".format(almost_black_count))
print("")
print("Black Pixel Percentage: {}".format(black_count/total_count))
print("Almost Black Pixel Percentage: {}".format(almost_black_count/total_count))
