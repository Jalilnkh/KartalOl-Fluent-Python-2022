#%%
import cv2 as cv
img = cv.imread('1258.jpg',0)
# Initiate FAST detector
star = cv.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print( brief.descriptorSize() )
print( des.flatten())
print(kp)
# %%
sift = cv.BRISK_create()
kp, des = sift.detectAndCompute(img,None)
print( des.shape)
#print(kp)
# %%
