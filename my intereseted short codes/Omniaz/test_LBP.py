#%%
from skimage.feature import local_binary_pattern
from skimage.feature import hog
from sklearn.decomposition import PCA
import cv2
from scipy.spatial import distance
import numpy as np 
# settings for LBP
radius = 2
n_points = 8 * radius
METHOD = 'uniform'
# resizing image
# %%
from lshash import LSHash
HASH_SIZE = 16  # hash size
NUM_HASH_TABLE = 3  # number of tables
FEATURE_DIMENSION = 8  # Dimension of Feature vector
# %%
from dsift import DsiftExtractor
def fea_ext(image):

        model = cv2.SIFT_create()
        image = cv2.resize(image, (128, 128), interpolation=cv2.INTER_CUBIC)
        _, feature = model.detectAndCompute(image, None)
        hog_val, _ = hog(image, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
        radius = 2
        n_points = 8 * radius
        lbp_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp_img = cv2.resize(lbp_img, (128,128), interpolation=cv2.INTER_CUBIC)
        lbp = local_binary_pattern(lbp_img, n_points, radius, 'uniform')
        lbp =lbp.flatten()
        extractor = DsiftExtractor(8,16,1)
        image = np.mean(np.double(image),axis=2)
        feaArr,_ = extractor.process_image(image)
        #des_len = int(len(des.flatten())/16)
        #des = des.flatten()[:des_len*16]
        #des = des.reshape((16, des_len))
        des =feaArr.flatten()
        return  np.hstack([lbp, hog_val])
        #return  des
#%%
from torch import nn
import time
from torchvision import models, transforms
import torch

def _mk_extractor():
    model = models.efficientnet_b7(pretrained=True)
    print(model)
    model.eval()
    return model.features[:8]
feature_extractor = _mk_extractor()

def __dnn(image):
    from torchvision.transforms import transforms
    array = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    array = cv2.resize(array, (64, 64), interpolation=cv2.INTER_CUBIC)
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
    ])
    array = transform(array).unsqueeze(0)
    with torch.no_grad():
        data = feature_extractor(array)
    #data = torch.max_pool2d(data, kernel_size=3)
    x = data.squeeze(0).flatten().numpy()
    return x
model_name = 'vgg16'
#%%
image = cv2.imread('dataset/enroll.jpg')
import os
FEATURE_DIMENSION = 2560
NUM_HASH_TABLE = 5
lsh = 0
lsh = LSHash(
            hash_size=5,
            input_dim=FEATURE_DIMENSION,
            num_hashtables=NUM_HASH_TABLE,
            matrices_filename='matrices-fun.npz',
            overwrite=True
            )
fea1 = __dnn(image)
fea2 = fea_ext(image)
print(len(fea1))
print(len(fea2))
#%%
path = 'enroll_dataset'
clsDict = {}
for root, dirs, files in os.walk(path):
        if files:
            clsDict[root.split('/')[-1]] = []
            for filename in files:
                img = cv2.imread(os.path.join(root, filename))
                if filename.split('.')[0] == 'enroll':
                        fea1 = __dnn(img)
                        #fea1 = fea_ext(img)
                        lsh.index(fea1, extra_data=os.path.join(root, filename))
                        print(root.split('/')[-1])
                        clsDict[root.split('/')[-1]].append(fea1)
                        print(root.split('/')[-1],"=>",",".join([
                        lsh._hash(lsh.uniform_planes[i], fea1) for i in range(lsh.num_hashtables) 
                                ]))
#%%
FP = 0
TP = 0
total = 0
for root, dirs, files in os.walk(path):
        if files:
            for filename in files:
                if filename.split('.')[0] != 'enroll':
                        total = total +1
                        img1 = cv2.imread(os.path.join(root, filename))
                        fea2 = __dnn(img1)
                        #fea2 = fea_ext(img1)
                        results0 = lsh.query(
                                fea2,
                                distance_func='cosine'
                                )
                        try:
                                if os.path.join(root, filename).split('/')[-2] == min(results0,
                                 key=lambda x: x[1])[0][1].split('/')[-2]:
                                        print('test ->',root.split('/')[-1],"=>", ",".join(
                                        [lsh._hash(lsh.uniform_planes[i], fea2) for i in range(lsh.num_hashtables)]), min(results0, key=lambda x: x[1])[1])
                                        print('enroll ->',min(results0, key=lambda x: x[1])[0][1].split('/')[-2],
                                        "=>",
                                        ",".join([lsh._hash(lsh.uniform_planes[i], clsDict[min(results0,
                                        key=lambda x: x[1])[0][1].split('/')[-2]][0]) for i in range(lsh.num_hashtables)]))
                                        TP = TP + 1
                                else:
                                        print('wrong test ->',root.split('/')[-1],"=>", ",".join(
                                        [lsh._hash(lsh.uniform_planes[i], fea2) for i in range(lsh.num_hashtables)]), min(results0, key=lambda x: x[1])[1])
                                        print('enroll ->',min(results0, key=lambda x: x[1])[0][1].split('/')[-2],
                                        "=>",
                                        ",".join([lsh._hash(lsh.uniform_planes[i], clsDict[min(results0,
                                        key=lambda x: x[1])[0][1].split('/')[-2]][0]) for i in range(lsh.num_hashtables)]))
                                        FP = FP + 1
                        except:
                                print('img')
#%%
print('FP -->',FP, 'TP ->', TP, 'total img -->', total)

# %%
