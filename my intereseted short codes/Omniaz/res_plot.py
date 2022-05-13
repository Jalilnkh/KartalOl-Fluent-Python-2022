#%%
import matplotlib.pyplot as plt

hog = [[0.028, 0.025, 0.03, 0.09, 0.18, 0.27],
[80.3, 20.4, 5.29, 1.33, 0.33, 0.13]]
lbp = [[0.1, 0.08, 0.08, 0.11, 0.13, 0.18],
[38.8, 9.36, 2.32, 0.66, 0.17, 0.07]]
img_size = [512, 256, 128, 64, 32, 16]

plt.plot(lbp[1], lbp[0],'*-')
plt.plot(hog[1], hog[0],'*-')
plt.xlabel('Response time (s)')
plt.ylabel('Equal Error Rate(%)')
plt.grid()
plt.legend(["LBP+DSIFT", "HOG+DISFT"])
plt.show()
# %%
