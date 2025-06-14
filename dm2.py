import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Step 1: Generate sample data
X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# Step 2: Apply DBSCAN
db = DBSCAN(eps=0.2, min_samples=5)
labels = db.fit_predict(X)

# Step 3: Plot the results
plt.figure(figsize=(8, 5))
plt.title("DBSCAN Clustering")
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma', s=40)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
