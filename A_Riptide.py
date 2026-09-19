t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    ans = 0

    while len(set(a)) == 3:
        a.sort()
        a[0] += 1
        a[2] -= 1
        ans += 1

    print(ans)
