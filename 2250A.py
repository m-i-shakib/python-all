t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    if n % 2 == 1:
        print("NO")
        continue

    L = 0
    R = 10**18

    for i in range(n):
        if i % 2 == 0:
            R = min(R, w[i])
        else:
            L = max(L, w[i])

    if L + 2 <= R:
        print("YES")
    else:
        print("NO")
