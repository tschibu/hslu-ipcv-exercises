# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""

"""

# =============================================================================
# Imports
# =============================================================================
import cv2
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# Matplot-Params
# Change size from Plots
plt.rcParams['font.size'] = 6
plt.rcParams['figure.dpi']= 100
plt.rcParams['lines.linewidth']= 1

# read img file
image = cv2.imread("data/lena_std.tiff")

# plot image
plt.imshow(image)
plt.show()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()

print(image_rgb[0, 0]) # RGB value at pixel (0,0)
print(image_rgb[0, 0, 0]) # Red value (same pixel)

# y=250:280, x=250:360
image_rgb[250:280, 250:360] = [255, 255, 255]
plt.imshow(image_rgb)
plt.show()

#
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# bw
plt.subplot(1, 2, 1)
plt.imshow(image_bw)
plt.subplot(1, 2, 2)
plt.imshow(image_rgb)

# gray
plt.subplot(1, 2, 1)
plt.imshow(image_gray, 'gray')
plt.subplot(1, 2, 2)
plt.imshow(image_rgb)