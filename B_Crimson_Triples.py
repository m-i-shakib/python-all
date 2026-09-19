t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0

    for b in range(1, n + 1):
        x = n // b
        ans += x * x

    print(ans)
