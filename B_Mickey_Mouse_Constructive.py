import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    s = x - y

    a = []

    for _ in range(x):
        a.append(1)

    for _ in range(y):
        a.append(-1)

    ans = 0

    for i in range(1, abs(s) + 1):
        if s % i == 0:
            ans += 1

    if s == 0:
        ans = 1

    print(ans)
    print(*a)
