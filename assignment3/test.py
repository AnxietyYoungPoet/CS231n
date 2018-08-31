import numpy as np


def f(x):
  ones = np.ones((3, 4))
  print(x[:, 0, :])
  print(x[:, 0, :] + ones)
  x[:, 0, :] += ones
  print(x[:, 0, :])


dout = np.random.randn(3, 3)
print(dout[[[0, 1], [2, 1]], :])
