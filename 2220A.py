t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) != n:
        print(-1)
    else:
        a.sort(reverse=True)
        print(*a)