import numpy as np


def xor_numpy(a, b):
    def nand_numpy(x1, x2):
        weights = np.array([-1.5, 1, 1])
        inputs = np.array([1, x1, x2])
        dot_product = np.dot(weights, inputs)
        return int(dot_product <= 0)

    a1 = nand_numpy(a, nand_numpy(a, b))
    b2 = nand_numpy(b, nand_numpy(a, b))
    return nand_numpy(a1, b2)


# Test the XOR function
xor_results = [
    xor_numpy(0, 0),
    xor_numpy(1, 0),
    xor_numpy(0, 1),
    xor_numpy(1, 1)
]

print(xor_results)
