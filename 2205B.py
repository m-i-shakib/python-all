import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    ans = 1
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            ans *= p
            while temp % p == 0:
                temp //= p
        p += 1
    if temp > 1:
        ans *= temp
    print(ans)