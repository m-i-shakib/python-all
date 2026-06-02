t = int(input())
for _ in range(t):
    n, c, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for power in a:
        if power > c:
            break
        use = min(k, c - power)
        power += use
        k -= use
        c += power
    print(c)