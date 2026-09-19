import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, x, y, z = map(int, input().split())
    without_ai = (n + x + y - 1) // (x + y)
    if x * z >= n:
        with_ai = (n + x - 1) // x
    else:
        remaining = n - x * z
        speed_after_setup = x + 10 * y

        with_ai = z + (
            remaining + speed_after_setup - 1
        ) // speed_after_setup
    print(min(without_ai, with_ai))