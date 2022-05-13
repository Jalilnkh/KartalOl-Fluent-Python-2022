#%%
from configparser import Interpolation
import cv2 
from scipy.spatial import distance
from sklearn.decomposition import PCA
import numpy as np
img_enroll = cv2.imread('enroll.jpg')
sift = cv2.SIFT_create()
kp = sift.detect(img_enroll)
kp_color, des_enroll = sift.detectAndCompute(img_enroll, None)
# %%
gen_img = cv2.imread('gen1.jpg')
sift= cv2.SIFT_create()
kp = sift.detect(gen_img)
kp_gray, des_gen = sift.detectAndCompute(gen_img, None)
# %%
imp_img = cv2.imread('gen2.jpg')
sift= cv2.SIFT_create()
kp = sift.detect(imp_img)
kp_gray, des_imp = sift.detectAndCompute(imp_img, None)
# %%
from lshash import LSHash
HASH_SIZE = 16  # hash size
NUM_HASH_TABLE = 5  # number of tables
FEATURE_DIMENSION = 8  # Dimension of Feature vector
pca = PCA(n_components=20)
lbp_imgl = pca.fit(des_enroll).explained_variance_ratio_
lbp_imgl1 = pca.fit(des_gen).explained_variance_ratio_
lbp_imgl2 = pca.fit(des_imp).explained_variance_ratio_
#%%
FEATURE_DIMENSION = 20
lsh=0
lsh = LSHash(
            hash_size=HASH_SIZE,
            input_dim=FEATURE_DIMENSION,
            num_hashtables=NUM_HASH_TABLE
            )
lsh.index(lbp_imgl)

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
results0
# %%
results1
# %%
results2
# %%