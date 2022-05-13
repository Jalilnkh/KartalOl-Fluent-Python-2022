#%% 
#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from scipy.spatial import distance
import matplotlib.pyplot as plt
import cv2
import numpy as np
# reading the image
img = imread('enroll.jpg')
img1 = imread('gen1.jpg')

plt.axis("off")
plt.imshow(img)
print(img.shape)

# resizing image
resized_img = resize(img, (448, 448))
resized_img1 = resize(img1, (448, 448))

plt.axis("off")
plt.imshow(resized_img)
print(resized_img.shape)
PCAD = 128
COLUMNOFCODEBOOK = 32
DESDIM = 128
#creating hog features
fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
fd1, hog_image1 = hog(resized_img1, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")
print(len(fd))
len_val = min([len(fd),len(fd1)])  

ad = distance.cosine(fd[:len_val], fd1[:len_val])
ad
# %%
feature = fd[fd>(max(fd)/2)]
print(feature)
# %%

plt.imshow(hog_image1, cmap="gray")
# %%
from lshash import LSHash
HASH_SIZE = 16  # hash size
NUM_HASH_TABLE = 5  # number of tables


lbp_imgl = fd[:len_val]
lbp_imgl1 = fd1[:len_val]
FEATURE_DIMENSION = len_val
lsh = LSHash(
                        hash_size=HASH_SIZE,
                        input_dim=FEATURE_DIMENSION,
                        num_hashtables=NUM_HASH_TABLE
                        )
lsh.index(np.array(lbp_imgl))

results0 = lsh.query(
                        lbp_imgl,
                        distance_func='cosine',
                    )
results1 = lsh.query(
                        lbp_imgl1,
                        distance_func='cosine',
                    )
# %%
results0[0][1]

# %%
results1
# %%
