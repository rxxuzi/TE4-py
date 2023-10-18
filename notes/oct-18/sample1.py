from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


primes = [str(x) for x in range(1, 101) if is_prime(x)]

