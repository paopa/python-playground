
import numpy as np
import matplotlib.pyplot as plt

"""
Gaussian data distribution is also called normal data distribution.

it represents items that occur around a mean value, with the highest number of items occurring around the mean value.

"""
x = np.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()
