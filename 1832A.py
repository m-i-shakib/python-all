import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if len(set(s)) == 1:
        print("NO")
        continue
    mx = max(s.count(ch) for ch in set(s))
    if n % 2 == 1 and mx == n - 1:
        print("NO")
        continue
    print("YES")
