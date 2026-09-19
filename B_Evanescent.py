t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1

    best = 0

    for i in range(1, n - 1):
        gain = (s[i - 1] != s[i]) + (s[i] != s[i + 1]) - (s[i - 1] != s[i + 1])
        best = max(best, gain)

    print(ans - best)
