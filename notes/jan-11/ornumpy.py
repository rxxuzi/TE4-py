import numpy as np


def or_numpy(x1, x2):
    weights = np.array([-0.5, 1, 1])
    inputs = np.array([1, x1, x2])
    dot_product = np.dot(weights, inputs)
    return int(dot_product > 0)


# Test the OR function
or_results = [or_numpy(0, 0), or_numpy(1, 0), or_numpy(0, 1), or_numpy(1, 1)]

print(or_results)
