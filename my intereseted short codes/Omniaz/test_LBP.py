#%%
from skimage.feature import local_binary_pattern
from skimage.io import imread
import cv2
# settings for LBP
radius = 3
n_points = 8 * radius
METHOD = 'uniform'

image = cv2.imread('1.jpg', 0)
print(type(image))
lbp = local_binary_pattern(image, n_points, radius, METHOD)

print(lbp)
# %%
