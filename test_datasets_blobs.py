from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from matplotlib import style


style.use("ggplot")

X, y = make_blobs(
    n_samples=150, n_features=2, centers=3, cluster_std=0.5, random_state=0
)

plt.scatter(X[:, 0], X[:, 1], marker="o", c=y, s=50)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")


plt.show()
plt.clf()
