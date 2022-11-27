from numba import njit
import numpy as np


@njit(cache=True)
def factorial(n):
    r = np.float128(1)
    for i in range(1, n + 1):
        r *= i
    return r


if __name__ == '__main__':
    print(factorial(100))
