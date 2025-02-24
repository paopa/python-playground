import numpy as np
from scipy.signal import convolve2d

source = np.array(list("1110001110001110011001100")).astype(np.int32).reshape(5, 5)

print("Source:")
print(source)

kernel = np.array(list("101010101")).astype(np.int32).reshape(3, 3)

print("Kernel:")
print(kernel)


feature_map = convolve2d(source, kernel, mode="valid")


print("Feature Map:")
print(feature_map)
