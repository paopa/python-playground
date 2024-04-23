import numpy as np

"""
Percentiles are used in statistics to give you a number that describes the value 
that a given percent of the values are lower than.

as an example, the 20th percentile is the value (or score) below which 20 percent 
of the observations may be found.
"""

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

order = np.sort(ages)
print(f"len = {len(ages)}, order = {order}")

x = np.percentile(ages, 75)

print(x)
