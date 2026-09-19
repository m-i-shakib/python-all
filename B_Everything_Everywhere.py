from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(abs(a[i] - a[i + 1]) == gcd(a[i], a[i + 1]) for i in range(n - 1)))
