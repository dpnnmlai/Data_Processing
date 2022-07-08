from sklearn.datasets import make_circles
from matplotlib import pyplot as plt
from matplotlib import style


style.use("fivethirtyeight")

X, y = make_circles(n_samples=1000, noise=0.1, random_state=0)
plt.scatter(X[:, 0], X[:, 1], marker="o", c=y, s=50)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")


plt.show()
plt.clf()
