t = int(input())

for _ in range(t):
    n = int(input())

    ans = []

    for i in range(1, n + 1, 2):
        ans.append(i + 1)
        ans.append(i)

    print(*ans)
