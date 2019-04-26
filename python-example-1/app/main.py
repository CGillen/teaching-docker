import numpy as np

ints = np.genfromtxt('/data/0.csv', delimiter=',')
floats = np.genfromtxt('/data/1.csv', delimiter=',')
print(ints)
print(floats)
print(ints + floats)
