#%%

import torch
from torch import optim, nn
from torchvision import models, transforms
model = models.vgg16(pretrained=True)

#%%
class FeatureExtractor(nn.Module):
  def __init__(self, model):
    super(FeatureExtractor, self).__init__()
		# Extract VGG-16 Feature Layers
    self.features = list(model.features)
    self.features = nn.Sequential(*self.features)
		# Extract VGG-16 Average Pooling Layer
    self.pooling = model.avgpool
		# Convert the image into one-dimensional vector
    self.flatten = nn.Flatten()
		# Extract the first part of fully-connected layer from VGG16
    self.fc = model.classifier[0]
  
  def forward(self, x):
		# It will take the input 'x' until it returns the feature vector called 'out'
    out = self.features(x)
    out = self.pooling(out)
    out = self.flatten(out)
    out = self.fc(out) 
    return out 

# Initialize the model
model = models.vgg16(pretrained=True)
new_model = FeatureExtractor(model)

# Change the device to GPU
device = torch.device('cuda:0' if torch.cuda.is_available() else "cpu")
new_model = new_model.to(device)
#%%
import numpy as np

# Transform the image, so it becomes readable with the model
transform = transforms.Compose([
  transforms.ToPILImage(),
  transforms.CenterCrop(512),
  transforms.Resize(224),
  transforms.ToTensor()                              
])

# Will contain the feature
features = []
#%% 
import cv2

# # Read the file
img = cv2.imread('1.jpg')
# Transform the image
img = transform(img)
# Reshape the image. PyTorch model reads 4-dimensional tensor
# [batch_size, channels, width, height]
img = img.reshape(1, 3, 224, 224)
img = img.to(device)
# We only extract features, so we don't need gradient
with torch.no_grad():
    # Extract the feature from the image
    feature = new_model(img)
# Convert to NumPy Array, Reshape it, and save it to features variable
features.append(feature.cpu().detach().numpy().reshape(-1))

# Convert to NumPy Array
features = np.array(features)
# %%
features
# %%
len(features[0])
# %%
from lshash import LSHash

lsh = LSHash(6, 8)
df = [[0.929,  0.9404, 0.82372,  0.3335, 1.0,   0.654, 0.1,  0.72],
      [0.9239, 0.94,   1.0 ,     0.596,  0.973, 0.338, 0.20, 0.1 ]]
lsh.index(df[1])
lsh.query(df[0],distance_func='cosine')

# %%
lsh = 0
# %%
x = -0.02
y = -0.003
z = -0.3
d = (x-y) / (z-y)
# %%
d
# %%
a= [1, 2 ,3]
b = []
b = a + b
b
# %%
