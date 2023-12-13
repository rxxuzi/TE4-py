import math


def unit(x1, x2):
    x0 = 1
    w0, w1, w2 = -1.5, 1, 1
    if x0 * w0 + x1 * w1 + x2 * w2 > 0:
        return 1
    else:
        return 0


print(unit(0, 0))
print(unit(1, 0))
print(unit(0, 1))
print(unit(1, 1))
