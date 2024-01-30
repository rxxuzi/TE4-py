import numpy as np


def nand_numpy(x1, x2):
    weights = np.array([-1.5, 1, 1])
    inputs = np.array([1, x1, x2])

    # ドット積を計算し、NAND条件を適用する。
    dot_product = np.dot(weights, inputs)
    return int(dot_product <= 0)


# Test
nand_results = [nand_numpy(0, 0), nand_numpy(1, 0), nand_numpy(0, 1), nand_numpy(1, 1)]

print()
print(nand_results)
