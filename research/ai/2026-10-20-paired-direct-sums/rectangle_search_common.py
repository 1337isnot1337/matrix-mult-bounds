"""Native source coordinates and the stated near-full rectangle target."""
from itertools import product
import numpy as np
import narrow_source_search as base


def target_data(n, b, kind, defect=1):
    if kind != 'rectangle':
        raise ValueError('This maintained helper implements rectangle targets only.')
    outer = n-defect
    if outer < 1:
        raise ValueError('The target outer dimension must be positive.')
    target = np.zeros((outer*outer, outer*b, b*outer))
    projection = np.zeros((outer*outer, n*n), dtype=np.int64)
    for i, k in product(range(outer), repeat=2):
        projection[outer*i+k, n*i+k] = 1
    for i, j, k in product(range(outer), range(b), range(outer)):
        target[outer*i+k, b*i+j, outer*j+k] = 1
    return target, projection, b*(n*n-outer*outer)
