import math


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())

    if is_prime(n + 1):
        print("YES")
    else:
        print("NO")

