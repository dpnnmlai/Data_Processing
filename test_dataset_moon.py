from sklearn.datasets import make_moons
from matplotlib import pyplot as plt
from matplotlib import style


X, y = make_moons(n_samples=2000, noise=0.08, random_state=0)
plt.scatter(X[:, 0], X[:, 1], marker="o", c=y, s=50)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")

plt.show()
plt.clf()
