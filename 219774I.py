t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**18
    for i in range(n):
        for j in range(i + 1, n):
            value = a[i] + a[j] + (j - i)
            if value < ans:
                ans = value
    print(ans)