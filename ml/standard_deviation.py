import numpy as np

"""
The standard deviation is a measure of how spread out the values are.

the lower the standard deviation, the closer the values are to the mean.
the higher the standard deviation, the further the values are from the mean.

"""

speed = [86, 87, 88, 86, 87, 85, 86]

x = np.std(speed)

print(x)

speed = [32, 111, 138, 28, 59, 77, 97]

x = np.std(speed)

print(x)
