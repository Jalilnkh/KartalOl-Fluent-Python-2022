#%%
import cv2 
img = cv2.imread('1.jpg',0)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None)
kp_color, des_color = sift.detectAndCompute(img,None)

cv2.imwrite('1.jpg',img2)


# %%
img = cv2.imread('1.jpg',1)
sift= cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None)

kp_gray, des_gray = sift.detectAndCompute(img,None)
cv2.imwrite("1.jpg",img2)
# %%
print(des_color.flatten() == des_gray.flatten())
# %%
