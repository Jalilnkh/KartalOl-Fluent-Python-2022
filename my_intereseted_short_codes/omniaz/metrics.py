#%%
from sklearn.metrics import precision_score, recall_score

# %%
# Example data
# True labels of the instances
y_true = [0, 1, 1, 1, 0, 1, 0, 0, 1, 1]
# Predicted labels by the classifier
y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
#%%
# Calculate Precision
precision = precision_score(y_true, y_pred)
print(f"Precision: {precision:.2f}")

# Calculate Recall
recall = recall_score(y_true, y_pred)
print(f"Recall: {recall:.2f}")
# %%
