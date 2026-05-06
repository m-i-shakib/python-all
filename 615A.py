import sys
input = sys.stdin.readline
n, m = map(int, input().split())
o = set()
for _ in range(n):
    p = list(map(int, input().split()))
    for b in p[1:]:
        o.add(b)
print("YES" if len(o) == m else "NO")
