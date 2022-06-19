#%% 
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

def load_nifti(input_nifti_file):
    return nib.load(input_nifti_file)


def compute_white_volume(image):
    pass


def compute_yolk_volume(image):
    pass


def compute_aircell_volume(image):
    pass

#%%
# Step 1 - Load data
input_nifti = 'mri_single_egg.nii'

nifti_egg = load_nifti(input_nifti_file=input_nifti)
# Step 2 - Visualize the data (for yourself)
nifti_egg.shape
nifti_data = nifti_egg.get_data()

nifti_data_2d = nifti_data.reshape(np.prod(nifti_data.shape[:-1]), nifti_data.shape[-1])
plt.imshow(nifti_data[:, 20, :], interpolation='nearest')
#%%
# Step 3 - Build an algorithm to compute volumes of yolk, white and air cell
egg_yolk = nifti_data[:,:,19]
plt.imshow(egg_yolk)
# plt.imshow(egg_yolk)
# Step 4 - Report volumes
# %%
egg_yolk = np.where()