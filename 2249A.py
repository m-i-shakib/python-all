import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]

    for m in range(n, 0, -1):
        j = 1

        for l, r, u, v in a:
            x = m - j + 1

            if (j < l or j > r) and (x < u or x > v):
                j += 1

                if j > m:
                    print(m)
                    return

    print(0)


t = int(input())

for _ in range(t):
    solve()
