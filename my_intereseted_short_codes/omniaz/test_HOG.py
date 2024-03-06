#%% 
#importing required libraries
from skimage.transform import resize
from skimage.feature import hog
import matplotlib.pyplot as plt
import cv2

# reading the image
img = cv2.imread('1.jpg')
plt.axis("off")
plt.imshow(img)
print(img.shape)

# resizing image
resized_img = resize(img, (128*4, 64*4))
plt.axis("off")
plt.imshow(resized_img)
print(resized_img.shape)


#creating hog features
fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")
# %%
feature = fd[fd>(max(fd)/2)]
print(feature)
# %%
