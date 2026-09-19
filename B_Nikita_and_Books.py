import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    ok = True

    for i in range(n):
        s += a[i]

        if s < (i + 1) * (i + 2) // 2:
            ok = False

    print("YES" if ok else "NO")
