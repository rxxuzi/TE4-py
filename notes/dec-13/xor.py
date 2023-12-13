import math

def nand(x1, x2):
    x0 = 1
    w0, w1, w2 = -1.5, 1, 1
    if x0 * w0 + x1 * w1 + x2 * w2 > 0:
        return 0
    else:
        return 1


def xor(a, b):
    a1 = nand(a, nand(a, b))
    b2 = nand(b, nand(a, b))
    return nand(a1, b2)

print(xor(0, 0))
print(xor(1, 0))
print(xor(0, 1))
print(xor(1, 1))
