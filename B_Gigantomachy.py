import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = a[0] + n - 1
    y = b[0] + m - 1

    print(1 if x >= y else 2)
