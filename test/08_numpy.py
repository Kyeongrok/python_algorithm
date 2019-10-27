import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import RandomState
from numpy.linalg import svd, matrix_rank

X = np.array(
    [
        [1,1,1,0,0],
        [3, 3, 3, 0, 0],
        [4, 4, 4, 0, 0],
        [5, 5, 5, 0, 0],
        [0, 2, 0, 4, 4],
        [0, 0, 0, 5, 5],
        [0, 1, 0, 2, 2],
    ]
)

u, d, v = svd(X, full_matrices=False)

rank = matrix_rank(X)
u = u[:,:rank]
d = d[:rank]
v = v[:rank, :]

print(u,d,v)