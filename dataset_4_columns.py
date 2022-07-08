from cProfile import label
import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt

# Definition of the function to generate the data ( Normal distribution )

p1 = abs(np.random.normal(0.4, 0.1, 100))  # mean, standard deviation, number of samples
p2 = abs(np.random.normal(0.8, 4, 100))  # mean, standard deviation, number of samples
p3 = abs(np.random.normal(34, 10, 100))  # mean, standard deviation, number of samples
p4 = abs(np.random.normal(54, 10, 100))  # mean, standard deviation, number of samples


x = np.c_[p1, p2, p3, p4]  # concatenate the arrays
y = [int(random.random() * 4) for i in range(100)]  # generate the labels

data = pd.DataFrame(x, columns=["p1", "p2", "p3", "p4"])  # create a dataframe

data["p1"] = p1  # add the labels to the dataframe
data["p2"] = p2
data["p3"] = p3
data["p4"] = p4
###############################################################################
plt.subplot(2, 2, 1)  # create a subplot
plt.title("Column 1")  # set the title
plt.scatter(y, p1, color="blue", label="p1")  # plot the data

#

plt.subplot(2, 2, 2)  # create a subplot
plt.title("Column 2")  # set the title
plt.scatter(y, p2, color="green", label="p2")  # plot the data

#

plt.subplot(2, 2, 3)  # create a subplot
plt.title("Column 3")  # set the title
plt.scatter(y, p3, color="red", label="p3")  # plot the data

#

plt.subplot(2, 2, 4)  # create a subplot
plt.title("Column 4")  # set the title
plt.scatter(y, p4, color="yellow", label="p4")  # plot the data

plt.savefig("data_visualiztion.png")  # save the figure

plt.show()  # show the figure
