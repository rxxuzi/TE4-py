import numpy as np


def and_numpy(x1, x2):
    weights = np.array([-0.5, 1, 1])
    inputs = np.array([1, x1, x2])
    dot_product = np.dot(weights, inputs)
    return int(dot_product > 0)


# Test the AND function
and_results = [and_numpy(0, 0), and_numpy(1, 0), and_numpy(0, 1), and_numpy(1, 1)]

print(and_results)
