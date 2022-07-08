from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mu = 0.4  # mean of the distribution

sigma = 0.1  # standard deviation of the distribution

np.random.seed(0)  # set the seed for reproducibility

X = np.random.normal(mu * np.ones(100), sigma * np.ones(100))  # generate the data

Y = np.random.normal(mu * np.ones(100), sigma * np.ones(100))  # generate the data

plt.scatter(X, Y, color="blue")
plt.show()
