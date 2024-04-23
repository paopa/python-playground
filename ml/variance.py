import numpy as np

"""
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

"""

speed = [32, 111, 138, 28, 59, 77, 97]

x = np.var(speed)

print(x)

x = np.sqrt(x)

print(x)

assert x == np.std(speed)
