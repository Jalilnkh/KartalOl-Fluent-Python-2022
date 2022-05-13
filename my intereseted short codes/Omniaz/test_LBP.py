#%%
from skimage.feature import local_binary_pattern
from skimage.io import imread
from skimage.feature import hog
from skimage.transform import resize
import cv2
from scipy.spatial import distance
import numpy as np 
# settings for LBP
radius = 2
n_points = 8 * radius
METHOD = 'uniform'
image = cv2.imread('enroll.jpg')
lbp_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image1 = cv2.imread('gen1.jpg')
lbp_img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.imread('imp1.jpg')
lbp_img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# resizing image
lbp_imgl =[]
lbp_imgl1 =[]
lbp_imgl2 =[]

print(type(image))
lbp = local_binary_pattern(lbp_img, n_points, radius, METHOD)
lbp1 = local_binary_pattern(lbp_img1, n_points, radius, METHOD)
lbp2 = local_binary_pattern(lbp_img2, n_points, radius, METHOD)
for single_list in lbp:
    lbp_imgl.extend(single_list)
for single_list in lbp1:
        lbp_imgl1.extend(single_list)
for single_list in lbp2:
        lbp_imgl2.extend(single_list)

# %%
from lshash import LSHash
HASH_SIZE = 16  # hash size
NUM_HASH_TABLE = 15  # number of tables
FEATURE_DIMENSION = 8  # Dimension of Feature vector

len_val = min([len(lbp_imgl),len(lbp_imgl2),len(lbp_imgl1)])  

lbp_imgl = lbp_imgl[:len_val]
lbp_imgl2 = lbp_imgl2[:len_val]
lbp_imgl = lbp_imgl[:len_val]
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
results2 = lsh.query(
                    lbp_imgl2,
                    distance_func='cosine',
                    ) 
# %%
results0[0][1]
# %%
results1[0][1]
# %%
results2[0][1]
# %%
